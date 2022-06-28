---
layout: page
permalink: /publications/
title: Publications
years: [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 
2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 
1997, 1996, 1995, 1994]
order: 3
nav: true
dropdown: true
children: 
    - title: All Publications
      permalink: /publications/
    - title: divider
    - title: Books
      permalink: /books/
    - title: divider
    - title: Ph.D. Theses
      permalink: /phdtheses/
    - title: divider
    - title: Bibtex
      permalink: /assets/bibliography/all-software-engineering-rwth-references.bib
---

{% include trennlinie.html %}

#### Additional infos on publications: 

* For an easy use and download: [Bibtex file with most 
  papers](/assets/bibliography/all-software-engineering-rwth-references.bib)
* [List of interesting publications aggregated into topics](/research)
* [Books](/books)
* [Ph.D Theses / Aachener Informatik-Berichte, Software Engineering](/phdtheses)
* [SoSyM Editorials](http://www.sosym.org/editorials/)  
* [Complete list of publications](https://www.se-rwth.de/publications/)

{% include trennlinie.html %}

## Selected publications (descendent by time) 

<div class="publications">
  {% for y in page.years %}
    {% include trennlinie.html %}
    <h2 class="year">{{y}}</h2>
    {% bibliography -f all-software-engineering-rwth-references -f additional-bib-entries -q 
    @*[year={{y}}]* %}
  {% endfor %}
</div>


{% include trennlinie.html %}

#### Further links:

- [Publications](/publications)
- [Topic sorted list of most interesting publications](/research)
- [Books](/books)
- [Aachener Informatik-Berichte, Software Engineering / Ph.D. Theses](/phdtheses)
- [Website of the SE](https://www.se-rwth.de)

