---
layout: default
title: Members
description: Members and alumni of the GS Research Group.
permalink: /members/
---

<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Members</p>
    <h1>People make the science possible.</h1>
    <p>Add real biographies, portraits, thesis topics, and alumni destinations as the group grows.</p>
  </div>
</section>

<section class="wrap">
  <div class="section-heading">
    <p class="eyebrow">Current Group</p>
    <h2>Group leader, trainees, and collaborators.</h2>
  </div>
  <div class="people-grid">
    {% for person in site.data.members %}
      <article class="person-card">
        <div class="avatar" aria-hidden="true">{{ person.initials }}</div>
        <div>
          <h3>{{ person.name }}</h3>
          <span class="role">{{ person.role }}</span>
          <p>{{ person.bio }}</p>
        </div>
      </article>
    {% endfor %}
  </div>
</section>

<section class="section-band">
  <div class="wrap content-flow">
    <h2>Alumni</h2>
    <p>Use this section to acknowledge former students, interns, technicians, postdocs, and collaborators. Include current positions when available.</p>
    <ul class="timeline">
      <li><time>2026</time> Alumni name - next position or degree program.</li>
      <li><time>2025</time> Alumni name - contribution to the lab.</li>
      <li><time>2024</time> Alumni name - thesis or project title.</li>
    </ul>
  </div>
</section>
