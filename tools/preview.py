from __future__ import annotations

import datetime as dt
import html
import http.server
import os
from pathlib import Path
import re
import shutil
import socketserver
import threading
import time
from typing import Any, Dict, Iterable, List, Tuple

import yaml


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_preview_site"
PORT = int(os.environ.get("PREVIEW_PORT", "4000"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_front_matter(text: str) -> Tuple[Dict[str, Any], str]:
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return {}, text
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if not match:
        return {}, text
    return yaml.safe_load(match.group(1)) or {}, match.group(2)


def load_yaml(path: Path) -> Any:
    if not path.exists():
        return None
    return yaml.safe_load(read_text(path)) or {}


def date_value(value: Any) -> dt.datetime:
    if isinstance(value, dt.datetime):
        return value
    if isinstance(value, dt.date):
        return dt.datetime.combine(value, dt.time())
    return dt.datetime.fromisoformat(str(value))


def page_url(path: Path, meta: Dict[str, Any]) -> str:
    if meta.get("permalink"):
        return str(meta["permalink"])
    if path.name == "index.md":
        return "/"
    return "/" + path.stem + "/"


def post_url(path: Path, meta: Dict[str, Any]) -> str:
    date = date_value(meta["date"])
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
    return f"/{date:%Y/%m/%d}/{slug}/"


def relative_url(value: str, site: Dict[str, Any]) -> str:
    baseurl = site.get("baseurl") or ""
    if value.startswith(("http://", "https://", "mailto:", "#")):
        return value
    if not value.startswith("/"):
        value = "/" + value
    return baseurl + value


def format_date(value: Any, fmt: str) -> str:
    date = date_value(value)
    fmt = fmt.replace("%-d", str(date.day))
    return date.strftime(fmt)


def get_value(expr: str, context: Dict[str, Any]) -> Any:
    expr = expr.strip()
    if (expr.startswith('"') and expr.endswith('"')) or (expr.startswith("'") and expr.endswith("'")):
        return expr[1:-1]
    parts = expr.split(".")
    value: Any = context
    for part in parts:
        part = part.strip()
        if isinstance(value, dict):
            value = value.get(part)
        else:
            value = getattr(value, part, None)
        if value is None:
            return ""
    return value


def render_expr(expr: str, context: Dict[str, Any]) -> str:
    parts = [part.strip() for part in expr.split("|")]
    value = get_value(parts[0], context)
    for filt in parts[1:]:
        if filt == "relative_url":
            value = relative_url(str(value), context["site"])
        elif filt == "size":
            value = len(value)
        elif filt == "strip_html":
            value = re.sub(r"<[^>]+>", "", str(value))
        elif filt.startswith("truncate:"):
            length = int(filt.split(":", 1)[1].strip())
            text = str(value)
            value = text if len(text) <= length else text[: max(0, length - 3)].rstrip() + "..."
        elif filt == "date_to_xmlschema":
            value = date_value(value).isoformat()
        elif filt.startswith("date:"):
            fmt = filt.split(":", 1)[1].strip().strip('"').strip("'")
            value = format_date(value, fmt)
        elif filt.startswith("default:"):
            fallback = filt.split(":", 1)[1].strip().strip('"').strip("'")
            value = value or get_value(fallback, context) or fallback
    return str(value)


def render_vars(text: str, context: Dict[str, Any]) -> str:
    return re.sub(r"{{\s*(.*?)\s*}}", lambda m: render_expr(m.group(1), context), text, flags=re.S)


def find_matching_endfor(text: str, start: int) -> Tuple[int, int]:
    tag_re = re.compile(r"{%\s*(for\b.*?|endfor)\s*%}", re.S)
    depth = 1
    for match in tag_re.finditer(text, start):
        tag = match.group(1).strip()
        if tag.startswith("for "):
            depth += 1
        elif tag == "endfor":
            depth -= 1
            if depth == 0:
                return match.start(), match.end()
    raise ValueError("Unmatched for tag")


def eval_iterable(expr: str, context: Dict[str, Any]) -> Iterable[Any]:
    return get_value(expr, context) or []


def render_conditionals(text: str, context: Dict[str, Any]) -> str:
    pattern = re.compile(r"{%\s*if\s+([\w.]+)\s*%}(.*?)(?:{%\s*else\s*%}(.*?))?{%\s*endif\s*%}", re.S)
    while True:
        match = pattern.search(text)
        if not match:
            return text
        value = get_value(match.group(1), context)
        replacement = match.group(2) if value else (match.group(3) or "")
        text = text[: match.start()] + render_liquid(replacement, context) + text[match.end() :]


def render_loops(text: str, context: Dict[str, Any]) -> str:
    for_re = re.compile(r"{%\s*for\s+(\w+)\s+in\s+([^%]+?)\s*%}", re.S)
    pos = 0
    rendered = []
    while True:
        match = for_re.search(text, pos)
        if not match:
            rendered.append(text[pos:])
            break
        body_start = match.end()
        body_end, tag_end = find_matching_endfor(text, body_start)
        rendered.append(text[pos : match.start()])
        item_name = match.group(1)
        collection = eval_iterable(match.group(2), context)
        body = text[body_start:body_end]
        pieces = []
        for item in collection:
            child = dict(context)
            child[item_name] = item
            pieces.append(render_liquid(body, child))
        rendered.append("".join(pieces))
        pos = tag_end
    return "".join(rendered)


def render_header(site: Dict[str, Any], page: Dict[str, Any]) -> str:
    current_url = page.get("url", "/")
    links = []
    for item in site.get("nav", []):
        url = item["url"]
        current = current_url == url or (url != "/" and current_url.startswith(url))
        attr = ' aria-current="page"' if current else ""
        links.append(f'<li><a{attr} href="{relative_url(url, site)}">{html.escape(item["title"])}</a></li>')
    return f"""<header class="site-header">
  <nav class="nav-wrap" aria-label="Primary navigation">
    <a class="brand" href="{relative_url('/', site)}">
      <span class="brand-mark">
        <img src="{relative_url('/images/Dexter_neha.png?v=20260525-1', site)}" alt="Singh Lab logo">
      </span>
      <span>{html.escape(site.get('short_title', site.get('title', 'Site')))} <small>{html.escape(site.get('subtitle', ''))}</small></span>
    </a>
    <ul class="nav-links">
      {''.join(links)}
    </ul>
  </nav>
</header>"""


def render_footer(site: Dict[str, Any]) -> str:
    year = dt.datetime.now().year
    return f"""<footer class="footer">
  <div class="wrap">
    <p>{html.escape(site.get('tagline', ''))}.</p>
    <p>&copy; {year} {html.escape(site.get('title', 'Site'))}</p>
    <ul class="footer-links">
      <li><a href="{relative_url('/contact/', site)}">Contact</a></li>
      <li><a href="{site.get('github_url', '#')}" rel="noreferrer">GitHub</a></li>
      <li><a href="{site.get('orcid_url', '#')}" rel="noreferrer">ORCID</a></li>
    </ul>
  </div>
</footer>"""


def render_includes(text: str, context: Dict[str, Any]) -> str:
    text = text.replace("{% include header.html %}", render_header(context["site"], context["page"]))
    text = text.replace("{% include footer.html %}", render_footer(context["site"]))
    return text


def render_liquid(text: str, context: Dict[str, Any]) -> str:
    text = render_loops(text, context)
    text = render_conditionals(text, context)
    text = render_includes(text, context)
    text = render_vars(text, context)
    text = re.sub(r"{%\s*assign\s+.*?%}", "", text)
    return text


def output_path_for_url(url: str) -> Path:
    url = url.strip("/")
    if not url:
        return OUT / "index.html"
    return OUT / url / "index.html"


def build() -> None:
    if OUT.exists():
        for child in OUT.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    else:
        OUT.mkdir(parents=True)

    site = load_yaml(ROOT / "_config.yml")
    site["baseurl"] = ""
    site["time"] = dt.datetime.now()
    site["data"] = {path.stem: load_yaml(path) for path in (ROOT / "_data").glob("*.yml")}

    posts = []
    for path in sorted((ROOT / "_posts").glob("*.md"), reverse=True):
        meta, body = split_front_matter(read_text(path))
        url = post_url(path, meta)
        posts.append(
            {
                **meta,
                "url": url,
                "content": body,
                "excerpt": body.strip().split("\n\n", 1)[0],
            }
        )
    site["posts"] = posts

    default_layout = read_text(ROOT / "_layouts" / "default.html")
    post_layout = read_text(ROOT / "_layouts" / "post.html")

    shutil.copytree(ROOT / "assets", OUT / "assets")
    images = ROOT / "images"
    if images.exists():
        shutil.copytree(images, OUT / "images")

    pages = list(ROOT.glob("*.md"))
    for path in pages:
        if path.name.upper() == "README.md":
            continue
        meta, body = split_front_matter(read_text(path))
        url = page_url(path, meta)
        page = {**meta, "url": url}
        context = {"site": site, "page": page}
        rendered_body = render_liquid(body, context)
        html_text = default_layout.replace("{{ content }}", rendered_body)
        html_text = render_liquid(html_text, context)
        out_path = output_path_for_url(url)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html_text, encoding="utf-8")

    for post in posts:
        context = {"site": site, "page": post}
        rendered_body = render_liquid(post["content"], context)
        post_shell = post_layout.replace("{{ content }}", rendered_body)
        post_shell = render_liquid(post_shell, context)
        html_text = default_layout.replace("{{ content }}", post_shell)
        html_text = render_liquid(html_text, context)
        out_path = output_path_for_url(post["url"])
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html_text, encoding="utf-8")


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def serve() -> None:
    os.chdir(OUT)
    handler = http.server.SimpleHTTPRequestHandler
    with ReusableTCPServer(("127.0.0.1", PORT), handler) as httpd:
        print(f"Preview running at http://127.0.0.1:{PORT}/")
        print("Press Ctrl+C to stop.")
        httpd.serve_forever()


if __name__ == "__main__":
    build()
    serve()
