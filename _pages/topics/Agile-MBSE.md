---
layout: page
title: Agile Model-Based Software Engineering
permalink: /topics/Agile-MBSE/
description: 
img: 
importance: 1
keys: [Rum17, Rum16, CEG+14, Rum12, Sch12, Rum11, Kra10, LRS+10, MRR10, 
       HKR+09, FHR08, KRV06, GKR+06a, GKR+06b, Rum04c, Rum03, PR03, Rum02]
---

## Summary of Most Relevant Topic Papers

Many developers and project managers think that the use of models in software 
development yields heavy-weight, tedious development processes. They believe 
that sooner or later, the models are outdated, not co-evolved, buggy and, 
ultimately, no longer helpful, but they believe that agility means to 
concentrate on the program as a core artifact without much extra documentation. 
Agility enables efficient evolution, correction and extension. As such, it seems 
to conflict with modeling.

One of our research hypotheses 
[[Rum04c]](#Rum04c), hence, can be 
phrased like this: **"Using an executable, yet abstract and multi-view modeling 
language for modeling, designing, and programming supports agile development 
process."**

We found that modeling will be used in development projects much more, when its 
benefits become evident early. Therefore, generation or synthesis of code from 
the models needs to be among the first steps of a model-based development 
process. Other beneficial techniques, such as test synthesis or high level 
analysis techniques, are less important. Consequently, executability of modeling 
languages is crucial.

## Execution of UML and DSLs

We discussed the question whether **UML should be executable** in 
[[Rum02]](#Rum02). We found code 
generation a promising approach for larger subsets of the UML language, but also 
identified a number of challenges. We therefore started our research agenda to 
solve these challenges in order to make model-based software engineering (MBSE) 
truly successful in the agile software development. We explored in detail, how 
UML fits for that purpose. Not only the deficiencies of existing UML tools, but 
also the UML language itself need to be adapted to fit the needs of an agile 
software development process.

In [[Rum03]](#Rum03) we discussed 
how modeling of tests helps to increase reuse and efficiency. In 
[[GKR+06b]](#GKR+06b), for example, 
we concentrate on the integration of models and ordinary programming language 
code.

<center>
<div class="row" style="width: 85%">
    <div class="col-sm mt-3 mt-md-0">
        {% responsive_image path: assets/img/model_uml_2.png title: 
        "Modellierung mit UML" class: "img-fluid z-depth-1" 
        href="http://mbse.se-rwth.de/book1/" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% responsive_image path: assets/img/agile_model_uml_2.png title: "Agile 
        Modellierung mit UML" class: "img-fluid z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% responsive_image path: 
        assets/img/Modeling-with-UML--Language-Concepts-Methods.jpg title: 
        "Modeling with UML" class: "img-fluid z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% responsive_image path: 
        assets/img/Agile-Modeling-with-UML--Code-Ceneration-Testing-Refactoring.jpg 
        title: "Agile Modeling with UML" class: "img-fluid z-depth-1" %}
    </div>
</div>
</center>
<br />

In [[Rum12]](#Rum12), 
[[Rum11]](#Rum11), 
[[Rum16]](http://www.se-rwth.de/mbse/), and 
[[Rum17]](http://www.se-rwth.de/mbse/) [(online versions available 
here)](http://www.se-rwth.de/mbse/), the **UML/P**, a variant of the UML 
especially designed for programming, refactoring and evolution, is defined. The 
UML/P embodies class, object, sequence diagrams, Statecharts and OCL in 
combination with Java to model code as well as tests as sketched in the 
following figure.

<center>
<div class="row" style="width: 50%">
    <div class="col-sm mt-3 mt-md-0">
        {% responsive_image path: assets/img/UMLP.jpg title: "UMPL/P" class: 
        "img-fluid rounded z-depth-1" %}
    </div>
</div>
</center>
<br />

Detailed discussions on how to use the UML/P for **code generation**, testing 
and on how to refactor structural models such as class diagrams, as well as 
behavioral models such as Statecharts, can be found in 
[[Rum12]](#Rum12), 
[[Rum11]](#Rum11), 
[[Rum17]](http://www.se-rwth.de/mbse/), and 
[[Rum16]](http://www.se-rwth.de/mbse/). Integrated use of UML/P languages 
demands forms of language integration, such as, using object diagrams in the OCL 
to describe desired or unwanted object structures. These language integration 
mechanisms are presented there as well.

In the last decade, we implemented a **language workbench** called 
[MontiCore](/topics/MontiCore) which is initially 
described in [[GKR+06a]](#GKR+06a). 
On top of that, we realized most of the language components of the UML/P in 
[[Sch12]](#Sch12). This includes a 
precise definition of the textual languages, type checks, checks for other 
context conditions within and between UML sub-languages and a framework for the 
implementation of code generators.

## Specific Concepts Assisting Agile Development
Agile development requires many specific activities, techniques and concepts. 
Links to further research can be found below. Some of this research, e.g., 
includes a general discussion of how to **manage and evolve models** 
[[LRS+10]](#LRS+10) or a precise 
definition for **model composition** as well as model languages 
[[HKR+09]](#HKR+09). 
Compositionality is particularly important and must be designed carefully as it 
allows the tools to analyze and generate incrementally, thus being much more 
agile than today's modeling tools. We also discussed in detail what 
**refactoring** means and how refactoring looks like in the various modeling and 
programming languages 
[[PR03]](#PR03). The UML/P is 
implemented in such a way that models can be specified **free of redundancies** 
even in different levels of abstraction, which enhances refactoring and 
evolution techniques on models. To better understand the effect of an evolved 
design, we discuss the need for semantic differencing in 
[[MRR10]](https://www.se-rwth.de/publications/A-Manifesto-for-Semantic-Model-Differencing.pdf).

When models are the central notation, **model quality** becomes an important 
issue. Therefore, we have described a set of general requirements for model 
quality in [[FHR08]](#FHR08). We 
distinguished between internal and external quality. External quality refers to 
the correctness and completeness of a model with respect to the original that it 
describes, while internal quality refers to the model presentation and thus 
plays the same role as coding guidelines for programming languages.

We assume that the use of **models at runtime** will become a pretty agile and 
efficient development technique. It allows developers to delay design decisions 
to runtime adaptation and configuration of systems. However, reliability then 
becomes an issue. In 
[[CEG+14]](https://www.se-rwth.de/publications/Using-Models-at-Runtime-to-Address-Assurance-for-Self-Adaptive-Systems.pdf) 
we have therefore discussed how to improve reliability while retaining 
adaptivity.

<img src="{{ '/assets/img/balken.jpg' | relative_url }}" width = "100%" alt="" 
title="Trennlinie">

## Key Statements

1. Model-based development becomes interesting, when the model language is the 
central notation and thus replacing the programming language.
2. Tooling for MBSE must include code and test generation as well as type and 
context condition checking already on models. These techniques must be quick and 
thus modular and incremental.
3. Agile concepts, especially as refactoring, evolution, and automatic testing can be 
established with UML/P.
4. Executable UML/P is an extension of UML with Java, implemented using the 
MontiCore language workbench.

<img src="{{ '/assets/img/balken.jpg' | relative_url }}" width = "100%" alt=""
title="Trennlinie">

## Selected Topic-Specific Publications

<div class="publications">
  {% for k in page.keys %}
    {% bibliography -f all-software-engineering-rwth-references -q @*[key={{k}}]* %}
  {% endfor %}
</div>

<img src="{{ '/assets/img/balken.jpg' | relative_url }}" width = "100%" alt=""
title="Trennlinie">

## Related Topics
- [Evolution & Transformation of Models](/topics/Evolution)
- [Generative Software Engineering](/topics/Generative-SE)
- [MontiCore - Language Workbench](/topics/MontiCore)
- [UML/P](/topics/UML-P)
- [Unified Modeling Language (UML)](/topics/Unified-Modeling-Language)
- [Variability & Software Product Lines (SPL)](/topics/Variability)

<img src="{{ '/assets/img/balken.jpg' | relative_url }}" width = "100%" alt="" 
title="Trennlinie">

#### Further links: 

- [Publications](/publications)
- [Topic sorted list of most interesting publications](/research)
- [Books](/books)
- [Aachener Informatik-Berichte, Software Engineering / Ph.D. Theses](/phdtheses)
- [Website of the SE](/main)
