---
layout: page
permalink: /code-and-simulations/
title: Code and Simulations
description: Various numerical things I've worked on.
nav: true
nav_order: 3
---

## Lattice simulations of vacuum decay

Vacuum decay of a 2D Klein-Gordon field (feat. oscillons and domain walls).

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="assets/img/fvd-preview.png">
    <source src="assets/video/fvd.mp4" type="video/mp4">
  </video>
</figure>

Analogue vacuum decay in a 2D Bose-Einstein condensate (feat. domain walls and quantum vortices).

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="assets/img/analogue-fvd-preview.png">
    <source src="assets/video/analogue-fvd.mp4" type="video/mp4">
  </video>
</figure>

## Evolution of binaries driven by stochastic gravitational waves

{% if site.data.repositories.github_repos %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.html repository=repo %}
  {% endfor %}
</div>
{% endif %}

## Gravitational-wave background anisotropies
