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

<figure class="video_container" style="text-align:center;">
  <video controls="true" allowfullscreen="true" poster="https://alex-c-jenkins.github.io/assets/img/bubbles-cropped-preview.png" width="80%">
    <source src="https://alex-c-jenkins.github.io/assets/video/bubbles-cropped.mp4" type="video/mp4">
  </video>
</figure>

Analogue vacuum decay in a 2D atomic Bose-Einstein condensate (feat. oscillons, domain walls, and quantum vortices).

<figure class="video_container" style="text-align:center;">
  <video controls="true" allowfullscreen="true" poster="https://alex-c-jenkins.github.io/assets/img/analogue-bubbles-cropped-preview.png" width="80%">
    <source src="https://alex-c-jenkins.github.io/assets/video/analogue-bubbles-cropped.mp4" type="video/mp4">
  </video>
</figure>

<br>

## Binaries driven by stochastic gravitational waves

Do you want to know what happens to your favourite binary system when you bathe it in gravitational waves? Click on the link below!
Or look [here](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.128.101103) and [here](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.105.064021) for the papers.

{% if site.data.repositories.github_repos %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.html repository=repo %}
  {% endfor %}
</div>
{% endif %}

<br>

## Gravitational-wave background anisotropies

Here's a simulated map of the gravitational-wave sky, made by coupling the [Millennium simulation of structure formation](https://wwwmpa.mpa-garching.mpg.de/galform/virgo/millennium/) with a model of the cosmic populations of black holes and neutron stars.
Click [here](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.98.063501) for the paper.

<figure>
  <img src="https://alex-c-jenkins.github.io/assets/img/millennium-sgwb.png" width="100%">
</figure>
