---
layout: default
title: Gallery
description: Gallery and visual highlights from the GS Research Group.
permalink: /gallery/
---

<section class="page-hero">
  <div class="wrap members-intro publications-intro">
    <h1>Images from research, teaching, and group life.</h1>
  </div>
</section>

<section class="wrap section-accent">
  <div class="gallery-grid">
    {% for item in site.data.gallery %}
      <figure class="gallery-card">
        <img src="{{ item.image | relative_url }}" alt="{{ item.alt }}">
        <figcaption>{{ item.caption }}</figcaption>
      </figure>
    {% endfor %}
  </div>
</section>
