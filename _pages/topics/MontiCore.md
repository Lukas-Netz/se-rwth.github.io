---
layout: page
title: MontiCore - Language Workbench
permalink: /topics/MontiCore/
description: 
img: 
importance: 1
keys: [HKR21,]
---

## Overview of Selected Papers

[MontiCore](http://monticore.de/) is a language workbench for the 
efficient development of domain-specific languages. 
[MontiCore](http://monticore.de/) is used as a basic vehicle for our 
ongoing research in the area of model-based software engineering. The 
[MontiCore Language Workbench and Library Handbook 
[HKR21]](http://www.monticore.de/handbook.pdf) features **agile and 
compositional** development of **domain-specific (modeling) languages 
(DSLs)**. These concepts have the potential to greatly impact the 
software engineering process by enabling easy development of 
high-quality, custom-tailored languages to express software models. 
Such models can be analyzed, interpreted, and, in the end, potentially 
transformed into a running software product. 

The MontiCore framework provides necessary application programming 
interfaces along with a special language definition format based on 
grammars. 

MontiCore has been realized particularly with respect to **modularity** 
both concerning the implementation and the development of DSLs. As 
such, DSLs can be realized in a **compositional** way, **reusing**, for 
example, common language definitions. This allows the creation of 
**language libraries** which make it even easier to create the desired 
DSL. Modularity and compositionality of MontiCore's language component 
is based on (1) compositional concrete and abstract syntax, (2) 
compositional definition of context conditions, (3) clear definition of 
model interfaces using symbols of various symbol kinds (far beyond any 
restrictions of programming languages), and (4) compositional analysis 
and generation infrastructure enabling black-box reuse of algorithms on 
sub-languages. 

Therefore, MontiCore comes with a large library of **language 
components** containing various forms of expressions, statements, and 
literals. A second level of language components defines constituents 
for modeling languages, such as **StateCharts, Class Diagrams, Object 
Diagrams, Sequence Diagrams, BDDs and IBDs** from **UML** and **SysML** 
as well as **Feature Diagrams**, etc. The library of **language 
components** also provides possibilities to specify in first-order 
logic (i.e., an extension of the **OCL**), with specific emphasis on 
sets, physical units (**SI units**), both as literals and as types 
including automatic conversions. It provides **regular expressions** as 
language elements defining subtypes for strings providing typesafe 
processing of strings beyond standard programming language 
capabilities. Each of the provided language components comes with 
locally defined symbol kinds that can be exported and mapped to symbol 
kinds of other languages. 

MontiCore has successfully been deployed in a variety of industrial and 
research projects. Among many other general and domain-specific 
languages, the [UML/P family of modeling languages](/topics/UML-P) has 
been realized with MontiCore, and various forms of structured text 
languages for requirements, norms, and even legal texts were defined. 

Based on the facilities the MontiCore Language Workbench provides, 
**automatic derivation** of a **transformation language** for a given 
modeling language, **variability** of the languages, adding **tagging** 
to a given language, or even smart **analysis** techniques, such as 
**semantic differences** have been constructed and successfully 
realized. Below we provide a selection of relevant publications about 
MontiCore and related topics that are based on the MontiCore framework. 
Please also note the MontiCore Website for technical details as well as 
access to MontiCore itself. 

[//]: # (MontiCore Videos)

<div class="container my-5">

<div id="multi-item-example" class="carousel slide carousel-multi-item" data-ride="carousel" mdb-data-touch="true">

<div class="controls-top">
<a class="btn-floating" href="#multi-item-example" data-slide="prev"><i class="fa fa-chevron-left"></i></a>
<a class="btn-floating" href="#multi-item-example" data-slide="next"><i class="fa fa-chevron-right"></i></a>
</div>

<ol class="carousel-indicators">
<li data-target="#multi-item-example" data-slide-to="0" class="active"></li>
<li data-target="#multi-item-example" data-slide-to="1"></li>
<li data-target="#multi-item-example" data-slide-to="2"></li>
</ol>

<div class="carousel-inner" role="listbox">

<div class="carousel-item active">

<div class="row">

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/ybp7gi8Pu70" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>MontiCore - Allgemeine Informationen (Deutsch)</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/YT50xPgm0HI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>MontiCore - General Information (English)</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/9Djs-UxRxRs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>01 Models in Software Engineering</h5>
</div>
</div>
</div>

</div>

</div>

<div class="carousel-item">

<div class="row">

<div class="col-md-4">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/1nh-kQ_OA4E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>02 Overview of UML Diagrams</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/kzM1nDB-H5s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>03 Relationship between Software Language, Modeling Language and DSL</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/Q_sAB-Izkj4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>Simulators for Deep Learning (Seminar)</h5>
</div>
</div>
</div>

</div>

</div>

<div class="carousel-item">

<div class="row">

<div class="col-md-4">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/Ma8dZ_6OXMo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>04 External and Internal Architecture of a Model Processor</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/mHzGSbULPI4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>05 General Architecture of a Compiler</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/dhj2TQNdbYk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>06 Designing a Modeling Language</h5>
</div>
</div>
</div>

</div>

</div>

<div class="carousel-item">

<div class="row">

<div class="col-md-4">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/SMNuKUMXa-s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>07 DSL Design Guidelines</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/2aTDf1li64A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>08 MontiCore Installation Guide</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="560" height="315" src="https://www.youtube.com/embed/ayt9RPZL-dI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>09 Which Folders and Files are Generated by MontiCore</h5>
</div>
</div>
</div>

</div>

</div>

<div class="carousel-item">

<div class="row">

<div class="col-md-4">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/0eYZ307aGs8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>10 Tool Workflow on the Top Level</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/dMgS4zpKjFE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>11 MontiCore Grammar for Language and AST Definitions</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/iOQzjjcAgHU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>12 Abstract Syntax Tree</h5>
</div>
</div>
</div>

</div>

</div>

<div class="carousel-item">

<div class="row">

<div class="col-md-4">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/2EzZ65V5dsM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>13 Context Conditions</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/bJ9ciH2XEqA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>14 Visitor Pattern for AST Traversal</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/g4ELT0pBEao" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>15 Basic Concepts of the FreeMarker Template Engine</h5>
</div>
</div>
</div>

</div>

</div>

<div class="carousel-item">

<div class="row">

<div class="col-md-4">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/qyGOeg_3Ib0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>17 Error Handling</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/QXqA3iB88Zg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>18 Introduction to Language Composition</h5>
</div>
</div>
</div>

<div class="col-md-4 clearfix d-none d-md-block">
<div class="card mb-2">
<iframe width="300px" height="200px" src="https://www.youtube.com/embed/uY4TuYrDKjk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="carousel-caption d-none d-md-block">
    <h5>19 Design Pattern Used in MontiCore</h5>
</div>
</div>
</div>

</div>

</div>

</div>

</div>

</div>

<p><img src="{{ '/assets/img/balken.jpg' | relative_url }}" width = "100%" alt="" title="Trennlinie"></p>

## Related Topics
- [Agile Model-Based Software Engineering](/topics/Agile-MBSE)
- [Compositionality/Modularity of Models & Languages](/topics/Compositionality)
- [Domain-Specific Languages (DSLs)](/topics/Domain-Specific-Languages)
- [Evolution & Transformation of Models](/topics/Evolution)
- [Generative Software Engineering](/topics/Generative-SE)
- [Modeling Software Architecture](/topics/Software-Architecture)
- [MontiCore - Language Workbench](/topics/MontiCore)
- [Semantics of Modeling Languages](/topics/Semantics)
- [Software Language Engineering (SLE)](/topics/Language-Engineering)
- [UML/P](/topics/UML-P)
- [Unified Modeling Language (UML)](/topics/Unified-Modeling-Language)
- [Variability & Software Product Lines (SPL)](/topics/Variability)

<img src="{{ '/assets/img/balken.jpg' | relative_url }}" width = "100%" alt=""
title="Trennlinie">

## Selected Related Publications

<div class="publications">
  {% for k in page.keys %}
    {% bibliography -f all-software-engineering-rwth-references -q @*[key={{k}}]* %}
  {% endfor %}
</div>