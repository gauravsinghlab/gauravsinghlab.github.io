---
layout: default
title: Home
description: Research group website for cellular systems, disease mechanisms, and quantitative biology.
---

<section class="hero" aria-label="GS Research Group">
  <div class="hero-inner">
    <p class="eyebrow">Cellular systems | Disease biology | Quantitative methods</p>
    <h1>GS Research Group</h1>
    <p class="lede">We investigate how cells sense stress, coordinate repair, and change state during development and disease. Our work combines experimental biology, imaging, molecular profiling, and computational analysis.</p>
    <div class="hero-actions">
      <a class="button" href="{{ '/research/' | relative_url }}">Explore Research</a>
      <a class="button secondary" href="{{ '/contact/' | relative_url }}">Join the Group</a>
    </div>
  </div>
</section>

<section class="wrap intro-grid" aria-labelledby="welcome-heading">
  <div class="intro-copy">
    <p class="eyebrow">Welcome</p>
    <h2 id="welcome-heading">A research environment for careful experiments and clear biological questions.</h2>
    <p>Our group studies the mechanisms that connect cellular behavior to tissue-level outcomes. We are especially interested in how biological systems preserve function under stress, how damaged tissues adapt, and how quantitative measurements can reveal hidden regulatory states.</p>
    <p>The site is organized around the same core structure as a modern academic lab page: research themes, people, publications, news, gallery, and contact information.</p>
  </div>
  <div class="stat-strip" aria-label="Research focus summary">
    <div class="stat">
      <strong>{{ site.data.research | size }}</strong>
      <span>Core research themes ready to customize.</span>
    </div>
    <div class="stat">
      <strong>{{ site.nav | size }}</strong>
      <span>Primary site sections for a complete lab presence.</span>
    </div>
    <div class="stat">
      <strong>0</strong>
      <span>Build tools required on GitHub Pages.</span>
    </div>
  </div>
</section>

<section class="section-band">
  <div class="wrap">
    <div class="section-heading">
      <p class="eyebrow">Research Themes</p>
      <h2>Questions that connect mechanism, models, and measurement.</h2>
    </div>
    <div class="card-grid">
      {% for theme in site.data.research %}
        <article class="feature-card">
          <span class="tag">{{ theme.tag }}</span>
          <h3>{{ theme.title }}</h3>
          <p>{{ theme.description }}</p>
        </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="wrap split" aria-labelledby="lab-culture-heading">
  <div class="media-panel">
    <img src="{{ '/assets/images/lab-hero.png' | relative_url }}" alt="Scientific illustration with cells, microscopy textures, and data patterns">
  </div>
  <div>
    <p class="eyebrow">Lab Culture</p>
    <h2 id="lab-culture-heading">Curiosity-driven science with practical attention to rigor.</h2>
    <p>We value reproducible experiments, shared methods, direct mentorship, and open scientific conversation. Students and trainees are encouraged to build strong conceptual foundations while developing the technical fluency needed for modern biological research.</p>
    <div class="button-row">
      <a class="button" href="{{ '/members/' | relative_url }}">Meet the Group</a>
      <a class="button" href="{{ '/publications/' | relative_url }}">Read Publications</a>
    </div>
  </div>
</section>
