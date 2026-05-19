---
layout: default
title: Publications
description: Selected publications from the GS Research Group.
permalink: /publications/
---

<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Publications</p>
    <h1>Peer-reviewed work, preprints, and research outputs.</h1>
    <p>Selected work can be grouped by year with DOI links, preprint links, and highlighted lab-member names.</p>
  </div>
</section>

<section class="wrap">
  {% for group in site.data.publications %}
    <h2 class="year-heading">{{ group.year }}</h2>
    <div class="pub-list">
      {% for publication in group.items %}
        <article class="publication-card">
          <h3>
            {% if publication.url %}
              <a href="{{ publication.url }}" rel="noreferrer">{{ publication.title }}</a>
            {% else %}
              {{ publication.title }}
            {% endif %}
          </h3>
          <p class="meta">{{ publication.meta }}</p>
        </article>
      {% endfor %}
    </div>
  {% endfor %}
</section>
