---
layout: page
title: MontiGem - Generating Enterprise Management Systems
permalink: /research/MontiGem/
description:
img:
importance: 1
keys: [AMN+20a,HKR21,GHK+15a,DGH+18,GLRR15]
---
MontiGem [[AMN+20a]](#AMN+20a) is a generator for
data-centric business applications. To a large
extent, it uses standard models from UML/P as sources, namely, Class
Diagrams and OCL. While the standard
semantics of these modeling languages remains untouched, the generator
produces a lot more functionality around these models, because it is
well integrated into the target framework and target infrastructure
which is used to execute the enterprise management system. The
generator thus knows the backend technology stack, with an
application core in Java, storage using a relational database
and the frontend consisting of Typescript respectively JavaScript
components based on Angular and thus running in the browser.

The generator creates the data structure in the frontend and backend
as well as the communication infrastructure to transport data in both
directions. Furthermore, it generates the database tables as well as
all necessary functionality to access, retrieve and store the data in
the database.

As a highlight, the storage paradigm is based on the command pattern
that allows to merge current changes much better and thus allows an
optimistic update scheme.

As an extension, a DSL is used to describe the graphical layout of the user
interface in a comfortable way. Again the GUI sub-language is well
integrated with the class diagram models allowing to directly describe
what to visualize based on the storage structure in the database
(see the figure for some possible
visualizations).

The internal architecture of the MontiGem generator includes the three
typical main processes: reading, transformation and generation, 
while generation produces a lot of
resulting Java classes, Typescript and HTML files and related artifacts.



The
whole generation is designed in a very extensible way: First, a
generator target itself is written in a modular way allowing to reuse
parts in a rather independent way. Secondly, templates are used allowing
developers to add functionality in the systematic manner. They can, e.g.,
add additional methods to all generated classes of certain kind. Thirdly,
the TOP mechanism created in MontiCore [[HKR21]](#HKR21) is applied for all
kinds of creative classes allowing to efficiently add handwritten code
extensions to the generated classes, while fully retaining the
ability to intentionally re-generate everything every time. For that
purpose, all classes are also equipped with builders, which can be
replaced using the TOP mechanism if required.

Thus, handwritten and generated code pieces are well
integrated [[GHK+15a]](#GHK+15a). This enables the continuous regeneration of the
application with changing models and thus the co-evolution of the
models and the handwritten additional functionality during the entire
development process.


The input of the generator for such enterprise management systems can
be expanded to allow the tagging of existing models [[GLRR15]](#GLRR15),
e.g., for the definition of roles and rights, as well as model-based
testing [[DGH+18]](#DGH+18).

MontiGem builds on earlier versions. Together with MontiGem they are
already in use for generating various applications, such as a library
system, a Management Controlling Cockpit and a development artifact
overview system. Current extensions adapt and extend MontiGem for
mobile applications, further graphical representation components as
well as the development of information portals in the Internet of
Things domain.

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
- [Model-Based Assistive Systems](/research/Model-Based-Assistive-Systems)
- [Models in Enterprise Information System Development](/research/Enterprise-Information-Systems)
- [Digital Twins and Digital Shadows in Engineering, Operation and Production](/research/Digital-Twins)

{% include trennlinie.html %}

#### Further links:

- [Publications](/publications)
- [Topic sorted list of most interesting publications](/research)
- [Books](/books)
- [Aachener Informatik-Berichte, Software Engineering / Ph.D. Theses](/phdtheses)
- [Website of the SE](https://www.se-rwth.de)
