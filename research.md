---
layout: default
title: Research
description: Research themes and methods for the Gaurav Singh Research Group.
permalink: /research/
---

<section class="page-hero">
  <div class="wrap members-intro page-intro">
    <h1>Current focus</h1>
    <p>Our research is broadly organized around three connected areas.</p>
  </div>
</section>

<section class="wrap content-flow section-accent">
  <h2>1. How do cells sense and regulate mitochondrial membrane fluidity?</h2>
  <p>The inner mitochondrial membrane is where respiration and energy production happen. For this membrane to work well, it must maintain the right physical state - not too rigid, not too fluid. Our <a href="https://doi.org/10.1073/pnas.2213241120" rel="noreferrer">previous</a> work showed that cells actively regulate the fluidity of this membrane in response to respiratory demand. We now ask how cells sense this membrane state, how they restore it after stress, and which lipids, proteins, and signalling pathways regulate it.</p>

  <h2>2. Building tools to measure and perturb membrane physical state</h2>
  <p>Many important biological processes are hard to study because we cannot directly see or control them in living cells. We develop fluorescence-based tools to measure membrane organization, fluidity, redox state, and organelle dynamics. This includes chemical probes, genetically targeted biosensors, fluorescence-lifetime imaging, and new approaches to perturb membrane state with spatial and temporal control.</p>

  <h2>3. Using machine learning to understand and design biological tools</h2>
  <p>We are also interested in using protein language models and related approaches to help design better biosensors, fluorescent proteins, and molecular tools for cell biology. We are also interested in using AI/ML pipelines to analyse microscopy images, extract meaningful biological features, and follow cell-state changes over time.</p>
</section>

<section class="section-band">
  <div class="wrap section-accent">
    <div class="section-heading">
      <h2>Tools for measuring organelle behavior in living systems.</h2>
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
