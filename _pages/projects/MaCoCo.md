---
layout: page
title: MaCoCo - Management Cockpit for Controlling
permalink: /projects/MaCoCo
nav: false
keys: [GHK+20, ANV+18]
---

**A research project of RWTH Aachen University realized by the Chair of Management Accounting and the 
Chair of Software Engineering**


Within the **MaCoCo (Management Cockpit for Controlling) project** we realize a multi-user enterprise information system
for the 
decentralized management and controlling of organizational processes within the chairs or institutes of a university 
[[GHK+20](#GHK+20).
The project was started in 2016. The key elements of the project focus on finance, staff and project organization.

We follow an agile software development paradigm, which strongly involves future users in the conceptualization process.
Moreover, large parts of the MaCoCo application are generated
[[ANV+18](#ANV+18)
from Domain-Specific Languages (DSLs) developed with 
the [MontiCore (MC) language workbench and code generation framework](http://monticore.de/). 
This combination ensures a highly adaptable system. 

The MaCoCo project is funded by the RWTH Aachen University and jointly realized by the two Chairs 
of Management Accounting and Software Engineering.

## Impressions

<div id="carouselExampleIndicators" class="carousel carousel-dark slide" data-interval="false" data-ride="carousel">
  <ol class="carousel-indicators" style="position: absolute; top: 0;">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="4"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="5"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="6"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="7"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{{ '/assets/img/Dashboard.png' | relative_url }}" class="img-fluid rounded z-depth-1" alt="" title="Dashboard" >
    </div>
    <div class="carousel-item">
      <img src="{{ '/assets/img/Finanzdashboard.png' | relative_url }}" class="img-fluid rounded z-depth-1" alt="" title="Dashboard Finances" >
    </div>
    <div class="carousel-item">
      <img src="{{ '/assets/img/Finanzuebersicht.png' | relative_url }}" class="img-fluid rounded z-depth-1" alt="" title="Overview Finances">
    </div>
    <div class="carousel-item">
      <img src="{{ '/assets/img/Konto-Details.png' | relative_url }}" class="img-fluid rounded z-depth-1" alt="" title="Account Details">
    </div>
    <div class="carousel-item">
      <img src="{{ '/assets/img/Buchungen_zu_Konto.png' | relative_url }}" class="img-fluid rounded z-depth-1" alt="" title="Bookings">
    </div>
    <div class="carousel-item">
      <img src="{{ '/assets/img/Stellenzuweisungen.png' | relative_url }}" class="img-fluid rounded z-depth-1" alt="" title="Job Assignment">
    </div>
    <div class="carousel-item">
      <img src="{{ '/assets/img/Personal_Dashboard.png' | relative_url }}" class="img-fluid rounded z-depth-1" alt="..." title="Employees Dashboard">
    </div>
    <div class="carousel-item">
      <img src="{{ '/assets/img/Planstellen.png' | relative_url }}" class="img-fluid rounded z-depth-1" alt="..." title="Permanent Positions">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
<br>

{% include trennlinie.html %}

## Related Research Topics:
- [Agile Model Based Software Engineering](/topics/Agile-MBSE)
- [Domain Specific Languages (DSLs)](/topics/Domain-Specific-Languages)
- [Generative Software Engineering](/topics/Generative-SE)
- [Software Language Engineering (SLE)](/topics/Language-Engineering)
- [UML/P](/topics/UML-P)
- [Unified Modeling Language (UML)](https://www.se-rwth.de/topics/Unified-Modeling-Language.php)

{% include trennlinie.html %}

## Publications
<div class="publications">
  {% for k in page.keys %}
    {% bibliography -f all-software-engineering-rwth-references -q @*[key={{k}}]* %}
  {% endfor %}
</div>
