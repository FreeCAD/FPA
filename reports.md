<ul>
  {% for report in site.reports %}
    <li>
      <a href="{{ report.url }}">{{ report.title }}</a>
    </li>
  {% endfor %}
</ul>
