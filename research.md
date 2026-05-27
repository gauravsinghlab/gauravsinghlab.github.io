---
layout: default
title: Research
description: Research themes and methods for the Gaurav Singh Research Group.
permalink: /research/
---

<section class="page-hero">
  <div class="wrap members-intro publications-intro">
    <h1>Organelle biology, biosensors, and quantitative cell biology.</h1>
    <p>We study how intracellular compartments sense stress, communicate with one another, and shape cellular decisions in living systems.</p>
  </div>
</section>

<section class="wrap content-flow section-accent">
  <h2>Research Direction</h2>
  <p>The Gaurav Singh Research Group investigates how organelles maintain cellular function during changing physiological conditions. Our work focuses on mitochondria, organelle communication, stress adaptation, and the development of reporters that make dynamic intracellular states measurable in living cells.</p>

  <p>We combine microscopy, molecular perturbation, biosensor engineering, and quantitative image analysis to ask how organelle behavior is regulated, how cellular heterogeneity emerges, and how stress responses influence health and disease-relevant biology.</p>

  <h2>Current Questions</h2>
  <ul class="method-list">
    <li><strong>How do organelles adapt during cellular stress?</strong> We examine changes in organelle morphology, distribution, function, and signaling as cells respond to perturbation.</li>
    <li><strong>How do mitochondria communicate with the rest of the cell?</strong> We study mitochondrial dynamics and signaling pathways that connect organelle state to broader cellular outcomes.</li>
    <li><strong>How can biosensors reveal hidden biological states?</strong> We use genetically encoded reporters and live imaging to follow signaling, metabolism, and organelle physiology over time.</li>
    <li><strong>How does cellular heterogeneity arise?</strong> We use quantitative imaging and analysis workflows to measure cell-to-cell variation and identify patterns that are difficult to see from population averages.</li>
  </ul>

  <h2>Approach</h2>
  <p>The lab uses live and fixed-cell microscopy, molecular biology, reporter systems, image analysis, and computational workflows. We place emphasis on measurements that preserve single-cell information and connect visual phenotypes to testable mechanisms.</p>

  <p>Our projects are designed around clear biological questions, reproducible analysis, and careful interpretation of dynamic cellular behavior.</p>
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
