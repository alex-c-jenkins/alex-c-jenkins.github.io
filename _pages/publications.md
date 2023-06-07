---
layout: page
permalink: /publications/
title: Publications
description: Selected papers only. For a full list, please have a look at my <a href="https://inspirehep.net/authors/1656809">INSPIRE-HEP author page</a>.
years: [2023, 2022, 2021, 2020, 2019, 2018]
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f {{ site.scholar.bibliography }} -q @*[year={{y}}]* %}
{% endfor %}

</div>
