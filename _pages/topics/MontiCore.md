---
layout: page
title: MontiCore - Language Workbench
permalink: /topics/MontiCore/
description: 
img: 
importance: 1
keys: [HKR21,
    KRV08,HR17,GKR+07,Wei12,BPR+20,GKR+08,Voe11,HRW18,BEK+19,HMR+19,
    BHR+21,Hoe18,KRV10,Kra10,BEH+20,BEK+18b,HJRW20,KRV07a,KRV07b,
    HRR12,Sch12,BDL+18,GKRS06,
    Ber10, HRW15, Kra10, Loo17, PBI+16, Pin14, Rum16]
---

[//]: # Bem: viele Key's absichtlich nicht im Text refernziert

## Introduction 

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


## MontiCore's History 

MontiCore has been developed since 2004
[[GKR+08]](#GKR+08) [[HR17]](#HR17). 
We started its development because at that time the
available tools for model management where often very poor in
functionality and also not extensible, but closed shops. In 2004 the
first version of UML/P was published (and is now available as
[[Rum16]](#Rum16) [[Rum17]](#Rum17)) demonstrating that the conglomerate of languages -
that the UML is made of - can be substantiated with useful
transformation, refinement and refactoring techniques (cf.
[Evolution & Transformation of Models](/topics/Evolution)). 
We were mainly interested in
model-based techniques for code and test code generation as well as
flexible combination of language fragments, such as OCL within
Statecharts or Class Diagrams for typing in Component and Connector
Diagrams. However, hard coded modeling tools where not helpful in
realizing these techniques. This original motivation for providing a
flexible and adaptable toolset through MontiCore can also be found in
the foundational PhD theses of MontiCore [[Kra10]](#Kra10) [[Voe11]](#Voe11).

Later, it became apparent that UML will be complemented by several DSLs that
will be connected to software development or execution in various ways. The
definition of DSLs encounters the same difficulties as the definition of UML
has faced, i.e., they are often built from scratch, reuse is difficult or
not supported, and the same concepts get different syntactic shapes.
Thus, combining DSLs is rather impossible. We therefore extended the focus
of MontiCore to become a general language workbench that allows to define
languages and language fragments and to derive as much as possible from an
integrated, compact definition.

MontiCore provides sophisticated techniques to generate transformation
languages and their transformation engines based on DSLs [[HRW15]](#HRW15),
[[AHRW17]](#AHRW17), [[RRW15]](#RRW15) [[HHR+15]](#HHR+15) [[Wei12]](#Wei12), 
we have explored tagging languages
[[Loo17]](#Loo17) [[MRRW16]](#MRRW16) [[GLRR15]](#GLRR15), 
various forms of the UML and its
derivatives [[Sch12]](#Sch12) [[Wor16]](#Wor16) [[Hab16]](#Hab16) 
[[Rei16]](#Rei16) [[Rot17]](#Rot17) and a variety
DSLs. Despite MontiCore being an academic tool to
explore modeling and meta-modeling techniques, after so years of
development, it has reached an extraordinary strength and is thus
increasingly used in industrial projects, like energy management
[[Pin14]](#Pin14), as well as in scientific projects of entirely different
nature, such as the simulation of urban scenarios for autonomous driving
[[Ber10]](#Ber10) or human brain modeling [[PBI+16]](#PBI+16).

MontiCore, however, does not primarily focus comfort, e.g., graphical
editing, but **advanced functionality** for model-based analysis or
synthesis of software intensive systems as well as efficient textual
editing for experienced users.


{% include trennlinie.html %}

## Selected Topic-Specific Publications

<div class="publications">
  {% for k in page.keys %}
    {% bibliography -f all-software-engineering-rwth-references -q @*[key={{k}}]* %}
  {% endfor %}
</div>

{% include trennlinie.html %}

## Related Topics
- [Agile Model-Based Software Engineering](/topics/Agile-MBSE)
- [Compositionality/Modularity of Models & Languages](/topics/Compositionality)
- [Domain-Specific Languages (DSLs)](/topics/Domain-Specific-Languages)
- [Evolution & Transformation of Models](/topics/Evolution)
- [Generative Software Engineering](/topics/Generative-SE)
- [Modeling Software Architecture](/topics/Software-Architecture)
- [Semantics of Modeling Languages](/topics/Semantics)
- [Software Language Engineering (SLE)](/topics/Language-Engineering)
- [UML/P](/topics/UML-P)
- [Unified Modeling Language (UML)](/topics/Unified-Modeling-Language)
- [Variability & Software Product Lines (SPL)](/topics/Variability)

{% include trennlinie.html %}

#### Further links:

- [Publications](/publications)
- [Topic sorted list of most interesting publications](/topics)
- [Books](/books)
- [Aachener Informatik-Berichte, Software Engineering / Ph.D. Theses](/phdtheses)
- [Website of the SE](https://www.se-rwth.de)
