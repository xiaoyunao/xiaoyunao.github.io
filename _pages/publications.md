---
layout: archive
title: "Publications"
description: "Journal articles and preprints by Yun-Ao Xiao, including first-author research and collaborative work in astronomy."
permalink: /publications/
author_profile: true
---

{% assign published = site.publications | where: "status", "published" | sort: "date" | reverse %}
{% assign first_author = published | where: "role", "first-author" %}
{% assign coauthored = published | where: "role", "co-author" %}
{% assign preprints = site.publications | where: "status", "preprint" | sort: "date" | reverse %}

<p>{{ published.size }} journal articles, including {{ coauthored.size }} co-authored papers, and {{ preprints.size }} preprint. See also my <a href="https://orcid.org/0009-0004-2243-8289">ORCID record</a>.</p>

<h2>First-author publications</h2>
{% for post in first_author %}
  {% include publication-entry.html post=post %}
{% endfor %}

<h2>Co-authored publications</h2>
{% for post in coauthored %}
  {% include publication-entry.html post=post %}
{% endfor %}

{% if preprints.size > 0 %}
<h2>Preprints</h2>
{% for post in preprints %}
  {% include publication-entry.html post=post %}
{% endfor %}
{% endif %}
