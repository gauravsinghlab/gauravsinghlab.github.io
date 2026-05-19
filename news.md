---
layout: default
title: News
description: News and updates from the GS Research Group.
permalink: /news/
---

<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">News</p>
    <h1>Updates from the group.</h1>
    <p>Use concise posts for papers, grants, student awards, conference talks, outreach, openings, and milestones.</p>
  </div>
</section>

<section class="wrap">
  <div class="news-grid">
    {% for post in site.posts %}
      <article class="news-card">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p>{{ post.excerpt | strip_html | truncate: 160 }}</p>
      </article>
    {% endfor %}
  </div>
</section>
