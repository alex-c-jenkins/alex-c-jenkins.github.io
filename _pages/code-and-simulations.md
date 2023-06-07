---
layout: page
permalink: /code-and-simulations/
title: Code and Simulations
description: Various numerical things I've worked on.
nav: true
nav_order: 3
---

## Lattice simulations of vacuum decay

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="assets/img/fvd-preview.png">
    <source src="assets/video/fvd.mp4" type="video/mp4">
  </video>
</figure>

## Evolution of binaries coupled to stochastic gravitational waves

{% if site.data.repositories.github_repos %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.html repository=repo %}
  {% endfor %}
</div>
{% endif %}

## Gravitational-wave background anisotropies
