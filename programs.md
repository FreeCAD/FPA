---
title: "Initiatives"
description:
   "Active FPA Programs and Initiatives"
layout: default
---

# {{page.title}}

{{page.description}}


<ul>
  {% for program in site.programs %}
    <li>
      <h3> {{program.title }}</h3>
      <p>{{program.description}}</p>
      <a href="{{ program.url }}">details</a>
    </li>
  {% endfor %}
</ul>
