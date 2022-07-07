---
layout: page
title: Model-Based Assistive Systems
permalink: /research/Model-Based-Assistive-Systems/
description:
img:
importance: 1
keys: [HMR+19,Ma17,Mi13,Mi18,
        MM13,MM15,MS17,
        Mi19,SM18,SM20,ELR+17]
---

## Summary of Most Relevant Topic Papers

The aim of information services and systems is to turn data into useful
information.
Assistive systems are a special type of information system:
they (1) provide situational support for human behaviour (2) based on
information from previously stored and real-time monitored structural context
and behaviour data (3) at the time the person needs or asks for it [[HMR+19]](#HMR+19).

The figure below shows the main components of such an assistive
system according to the architectural patterns for model
centered architecture solutions [[Ma17]](#Ma17) .
Information about human behavior is collected via sensors or smart devices
and processed in an observation engine, which stores the data and models.
The behavior engine compares and connects the current behavior step with
already existing models of behavior.
The support engine decides which next step should be provided as behavior
support for the assisted person. This support can be provided as
step-by-step information multi-modal on different kinds of devices.

<center>
<div class="row" style="width: 70%">
    <div class="col-sm mt-3 mt-md-0">
        {% responsive_image path: assets/img/as_overview.png 
           title: "Main concepts of systems for human assistance" 
           class: "img-fluid rounded z-depth-1" %}
    </div>
</div>
</center>
<br />

For both, information and assistive services and systems, the application of
agile, model-based and generative methods (see 
[Agile Model-Based Software Engineering](/research/Agile-MBSE) and
[Generative Software Engineering](/research/Generative-SE))
fastens the development process,
enables a quick response to requirements changes in a user-centered
engineering process, and ensures consistency-by-design.

Our current work on assistive systems is based on former work within the
Human Behavior Monitoring and Support (HBMS)
project [[Mi13]](#Mi13) [[Mi18]](#Mi18)
in which a domain specific language [[Mi13]](#Mi13) and domain specific modeling
method for assistive systems [[MM15]](#MM15) were developed.

Current work extends these approaches: to enable useful support, it
is important to know more than just the behavior of a person.
Context-aware systems need detailed information about the task context
(including temporal information), the personal and social context, the
environmental context, as well as the spatial context.
We have investigated the modeling of these contexts primary for the active
assisted living and smart home domain [[MS17]](#MS17).
Recent research discusses the context model for user-centered privacy-driven
systems in the IoT domain including special aspects for the use in 
combination with process mining
systems [[Mi19]](#Mi19).

The mark-up of online manuals for non-smart devices [[SM18]](#SM18) 
as well as
websites [[SM19]](#SM19) is one further step to provide human-centered
assistance.
Using these approaches reduces system set-up time and improves flexibility
for changes by automatically integrating device and application
functionality into supporting systems.

Due to the General Data Protection Regulation (GDPR) organizations are
obliged to consider privacy throughout the complete development process.
Our work suggests solutions for privacy-aware environments for cloud
services [[ELR+17]](#ELR+17) as well as privacy preserving information systems
demonstrated on an IoT manufacturing use case [[Mi19]](#Mi19).

{% include trennlinie.html %}

## Key Statements

1. The engineering of interactive assistive systems is challenging as they
   might support critical functionality in dangerous
   environments and have a high need for safety and privacy considerations due
   to the processing of personal data about human behavior. 
2. Using agile, model-based and generative methods fastens the development 
   process, enables a quick response to requirements changes in a 
   user-centered 
   engineering process, and ensures consistency-by-design.
3. There are still challenges to overcome such as the high amount of relevant 
   contextual information needed to set-up such systems or high adaptability 
   requirements to personal needs.

{% include trennlinie.html %}

## Selected Topic-Specific Publications

<div class="publications">
  {% for k in page.keys %}
    {% bibliography -f all-software-engineering-rwth-references -q @*[key={{k}}]* %}
  {% endfor %}
</div>

{% include trennlinie.html %}

## Related Topics
- [Agile Model-Based Software Engineering](/research/Agile-MBSE)
- [Generative Software Engineering](/research/Generative-SE)
- [MontiCore - Language Workbench](/research/MontiCore)
- [UML/P](/research/UML-P)
- [Unified Modeling Language (UML)](/research/Unified-Modeling-Language)
- [Models in Enterprise Information System Development](/research/Enterprise-Information-Systems)
- [Digital Twins and Digital Shadows in Engineering, Operation and Production](/research/Digital-Twins)

{% include trennlinie.html %}

#### Further links:

- [Publications](/publications)
- [Topic sorted list of most interesting publications](/research)
- [Books](/books)
- [Aachener Informatik-Berichte, Software Engineering / Ph.D. Theses](/phdtheses)
- [Website of the SE](https://www.se-rwth.de)
