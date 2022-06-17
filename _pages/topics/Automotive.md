---
layout: page
title: Automotive
permalink: /topics/Automotive/
description: 
img: 
importance: 1
keys: [GRJA12,GHK+07,GHK+08,
        DGH+19,KMS+18,HKM+13,
        HRRW12,KRR+16,RRS+16,
        RSW+15]
---

## Summary of Most Relevant Topic Papers

Development of software for automotive systems has become increasingly
complex in the past years. Sophisticated driver assistance,
infotainment and Car2X-communication systems as well as advanced active
and passive safety-systems result in complex embedded systems. As these
feature-driven subsystems may be arbitrarily combined by the customer,
a huge amount of distinct variants needs to be managed, developed and
tested. While we are carrying out in numerous projects in the
Automotive domain, here we concentrate on three aspects: Autonomic
driving, modeling of functional and logical architectures and on
variability. To understand all these features in [[GRJA12]](#GRJA12) we
describe a requirements management that connects with features in all
phases of the development process helps to handle complex development
tasks and thus stabilizes the development of automotive systems.


## Modeling Logical Architecture: Function Nets

The conceptual gap between requirements and the logical architecture of
a car is closed in [[GHK+07]](#GHK+07) and [[GHK+08]](#GHK+08). Here, feature views
modeled as a function net are used to implement the mapping between
feature-related requirements and the complete logical architecture of a
car.

In a more elaborate version, we have helped a larger car manufacturer
to design their company specific method, **SMaRDT**, that injects
model-based software development for the logical architecture of a car
and connects it with the requirements and the technical implementation.
Furthermore, we have added automatic testing techniques to ensure model
quality from the beginning in [[DGH+19]](#DGH+19) and [[KMS+18]](#KMS+18).


## Variability of Car Software

Automotive functions that may be derived from a feature view are often
developed in Matlab/Simulink. As variability needs also to be handled
in development artifacts, we extended Matlab/Simulink with
Delta-Modeling techniques (see also XXXautoref{subsec:SPL}). A core Simulink
model represents the base variant that is transformed to another
variant by applying deltas to it. A delta contains modifications that
add, remove or modify existing model elements. This way, features of an
automotive system may be developed modularly without mixing up
variability and functionality in development artifacts [[HKM+13]](#HKM+13).
New delta models that derive new variants may be added bottom-up
without the need for a fully elaborated feature model.

<center>
<div class="row" style="width: 70%">
    <div class="col-sm mt-3 mt-md-0">
        {% responsive_image path: assets/img/DeltaSL.png 
        title: "Screenshot of the Delta-Simulink tool" 
        class: "img-fluid rounded z-depth-1" %}
    </div>
</div>
</center>
<br />

In practice, product lines often origin from a single variant that is
copied and altered to derive a new variant. In [[HRRW12]](#HRRW12), we
provide means to extract a well defined Software Product Line from a
set of copy and paste variants. This way, further variant development
is alleviated, as new variants directly reuse common elements of the
product line.

Ways to identify potential variants of components for potential product
lines are to use similarity analysis on interfaces [[KRR+16]](#KRR+16), or to
execute tests to identify similar behavior [[RRS+16]](#RRS+16). And a third
approach is described in [[RSW+15]](#RSW+15) that uses logical and model
checking techniques to identify commonalities and differences of two
Simulink models describing the same control device in different
variants. All these techniques allow us to understand incompatibilities
or identify the portion of compatibility of two components respectively
their models.


{% include trennlinie.html %}

## Key Statements
1. A consistent requirement management leads to a more stable and predictable 
development of automotive systems.
2. Various functional and architectural variants need to be explicitly managed 
in all phases of the development cycle.
3. Agile development techniques may be used by introducing continuous tests 
based on automatic simulations.
4. The quality of autonomous driving cars and smart assistance systems is 
assured using automatic simulations.

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
- [Cloud Computing & Enterprise Information Systems](/topics/Cloud)
- [Cyber-Physical Systems (CPS)](/topics/Cyber-Physical-Systems)
- [Domain-Specific Languages (DSLs)](/topics/Domain-Specific-Languages)
- [MontiArc - Architectural Modeling](/topics/Software-Architecture)
- [MontiCore - Language Workbench](/topics/MontiCore)
- [Modeling Software Architecture](/topics/Software-Architecture)
- [Robotics](/topics/Robotics)
- [Variability & Software Product Lines (SPL)](/topics/Variability)

{% include trennlinie.html %}

#### Further links:

- [Publications](/publications)
- [Topic sorted list of most interesting publications](/topics)
- [Books](/books)
- [Aachener Informatik-Berichte, Software Engineering / Ph.D. Theses](/phdtheses)
- [Website of the SE](https://www.se-rwth.de)
