---
layout: archive
title: "Education"
permalink: /education/
author_profile: true
---

<p>My academic training is also listed on <a href="https://orcid.org/0009-0004-2243-8289">ORCID</a>.</p>

{% assign education = site.education | sort: "start_year" | reverse %}
{% for post in education %}
<section class="education-entry">
  <h2><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h2>
  {{ post.content | markdownify }}
</section>
{% endfor %}
