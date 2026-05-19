---
layout: default
title: Research
description: Research themes and methods for the GS Research Group.
permalink: /research/
---

<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Research</p>
    <h1>Mechanisms of cellular resilience and tissue-level change.</h1>
    <p>Detailed descriptions of the group's biological systems, disease areas, model organisms, and technology focus can be expanded here.</p>
  </div>
</section>

<section class="wrap content-flow">
  <h2>Research Direction</h2>
  <p>The group asks how cells interpret stress, communicate with their neighbors, and transition between functional states. We connect live measurement with molecular profiling to identify mechanisms that explain repair, dysfunction, and disease progression.</p>

  <h2>Current Questions</h2>
  <ul class="method-list">
    <li><strong>How do cells preserve function under stress?</strong> We track molecular and phenotypic responses to understand which adaptations are protective and which drive pathology.</li>
    <li><strong>What controls cell identity and plasticity?</strong> We study the signals that stabilize, erase, or redirect cellular states during development, injury, and disease.</li>
    <li><strong>How can quantitative measurements guide mechanism?</strong> We combine microscopy, sequencing, and computational methods to build interpretable models of dynamic biological processes.</li>
  </ul>

  <h2>Approach</h2>
  <p>The lab uses a mix of molecular biology, imaging, perturbation experiments, data analysis, and collaborative methods development. The exact toolkit should be updated with your verified methods, facilities, and model systems.</p>
</section>

<section class="section-band">
  <div class="wrap">
    <div class="section-heading">
      <p class="eyebrow">Methods</p>
      <h2>Tools that make biological dynamics measurable.</h2>
    </div>
    <div class="card-grid">
      {% for method in site.data.methods %}
        <article class="feature-card">
          <span class="tag">{{ method.tag }}</span>
          <h3>{{ method.title }}</h3>
          <p>{{ method.description }}</p>
        </article>
      {% endfor %}
    </div>
  </div>
</section>
