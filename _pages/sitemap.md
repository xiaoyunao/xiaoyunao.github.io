---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
sitemap: false
noindex: true
---

Browse my academic homepage, or use the [XML sitemap]({{ '/sitemap.xml' | relative_url }}).

<h2>Main pages</h2>
<ul>
  <li><a href="{{ '/' | relative_url }}">About me and My Research</a></li>
  {% for item in site.data.navigation.main %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a></li>
  {% endfor %}
</ul>

{% assign collections = "publications,education,talks,teaching" | split: "," %}
{% for label in collections %}
<h2>{{ label | capitalize }}</h2>
<ul>
  {% for entry in site[label] %}
  <li><a href="{{ entry.url | relative_url }}">{{ entry.title | escape }}</a></li>
  {% endfor %}
</ul>
{% endfor %}
