---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% assign combined_posts = site.publications | concat: site.submits %}
{% for post in combined_posts reversed %}
  {% include archive-single.html %}
{% endfor %}
