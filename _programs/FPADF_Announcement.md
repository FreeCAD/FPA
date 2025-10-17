---
title: "The FreeCAD Grant Program"
description:
    "Develop new features in FreeCAD and get paid by the community"
layout: default
mermaid: true
---

# {{page.title}}

The FreeCAD Grant Program aims to foster rapid development of FreeCAD and its ecosystem by giving small grants to developers and non-programming contributors to work on specific individual projects. Their work is funded by the community: grants are issued by the FreeCAD Project Association, which collects donations. The FPA has reserved 80,000 EUR for the program in 2025.

For details on program rules, please refer to the [complete rulebook](/handbook/process/grant-program-rules).

The program was introduced in 2024 as a successor to the FPA Development Fund launched in August 2022.

## 2025 Program Timeline

Grants are evaluated and issued quarterly, with one fourth of the total budgeted funding available during each grant period, on the following schedule:

* Q1: March 1 submission deadline, March 15 committee meeting, voting complete by March 31
* Q2: June 1 submission deadline, June 21 committee meeting, voting complete by June 30
* Q3: Sept 1 submission deadline, Sept 20 committee meeting, voting complete by Sept 30
* Q4: Nov 15 submission deadline, Dec 7 committee meeting, voting complete by Dec 19

Grants received after the Nov. 15 deadline will not be considered for the 2025 grant year, but will be held until the 2026 program is announced.

## Potential Projects

The FPA accepts applications to improve both FreeCAD and its ecosystem.

For FreeCAD-related projects an overall preference is given to projects that address major issues that are covered by the [general roadmap](https://freecad.github.io/DevelopersHandbook/roadmap/). We accept and welcome non-roadmap submissions as well.

We also accept "time commitment" grant applications where the contributor would work for a certain amount of time on any tasks related to a particular effort, such as refactoring code. Please refer to the [Fixed Goal vs Time Commitment](https://fpa.freecad.org/handbook/process/grant-program-rules.html#fixed-goal-vs-time-commitment) section of the rulebook.

Ecosystem includes (but is not limited to) FreeCAD infrastructure, as well as projects that are hard dependencies for FreeCAD, such as OCCT and Coin3D libraries. For ecosystem projects, we expect contributors to be in agreement with respective projects on goals and scope of work, as well as on contribution process prior to submitting the grant application.

## Qualifying for The Program

Both individuals and groups of individuals can qualify as grant acceptees. Applicants of all ethnicities, nationalities, sexes, and genders are welcome to apply for participation at the program, however some EU legislation restrictions might apply. Each applicant is expected to be old enough to perform work legally in the country of their residence and sign a contract with the FPA on behalf of themselves.

The program is geared towards individual contributors. However, the FPA grant committee will accept grant applications from a group of contributors as long as the group is either an incorporated company or a group of individuals represented by a single person. Each member of the group needs to qualify for participation.

## Application Requirements

We expect each applicant to have a great understanding of the scope of the proposed work. They should demonstrate the ability to plan their work ahead and deliver results in a timely manner without active mentorship. For details, please refer to the [Passing Criteria](https://fpa.freecad.org/handbook/process/grant-program-rules.html#passing-criteria) section of the rulebook.

## How to Submit a Grant Application

Grant applications are managed in a [public GitHub repository](https://github.com/FreeCAD/FPA-grant-proposals) in the FreeCAD project. To submit a grant application, start creating an issue and choose the application template in the form, then fill all the fields.

## FAQ

### Do I have to be a CAD development superstar to qualify?

Not necessarily. Some of the successful grants have been issued to developers who don’t have a ton of experience developing CAD software. However, they have great problem-solving skills and demonstrated understanding of the underlying math. Grants are also possible for non-programming contributors.

### I’m a student. Should I apply for GSoC or for the grant program?

This largely depends on how comfortable you feel around the FreeCAD code base. For GSoC, we provide some assistance via mentors. For the grant program, we expect contributors to be self-sufficient, all code goes through the same PR review process.

### Is there a “pencils down” deadline for the grant work like at GSoC?

No, we issue grants for projects that wildly vary in scope and complexity. Some projects would be a 1 month effort. Others could last half a year or more.

<!-- ### Do you have examples of really good grant proposals?

Yes. -->

### I missed the queue for the annual program. Now what?

You can apply for an individual grant. The same rules apply: make a great case for your project idea, demonstrate that you are capable of delivering proposed results, submit pull requests and progress updates, get paid for each stage, be a hero to all of us.

### Who reviews applications?

The grant review committee looks at technical aspects of each grant application. Current members: Chris Hennes (@chennes, overall maintainer, committee chair), Yorik van Havre (@yorik, Arch and Draft maintainer), @FreeCutter, @shaise, and @drmacro. Anyone who is interested in joining the grant review committee should reach out to Chris Hennes (chennes@freecad.org, @chennes on Discord, @chris_hennes on Telegram, and @chennes on the FreeCAD Forums).

The FPA general assembly then takes the technical review into consideration and looks at non-technical aspects of the proposal. The general assembly is more diverse, its members are both FreeCAD contributors, educators, and representatives of nonprofits and businesses. The full list of members is here.

### What happens if my situation changes and I can’t continue working on a project?

That depends on how much work you have managed to do. If you are in the middle of a project stage and you have already submitted mergeable or already merged pull requests, the FPA can issue a partial compensation for that stage and terminate the contract. 

Alternatively, you can request a partial compensation and a pause to handle your situation. We do not request you to share your life details with us, but we expect you to warn us in a timely manner.

## Ongoing projects funded by the FPA

### Jo Hinchliffe (concretedog): Promoting Academic and Educational use of FreeCAD via targeted written tutorials

*Funding approved 2 October 2025.*

Jo will write FreeCAD tutorials developing resources that target the promotion of FreeCAD in educational environments. Jo is a regular contributor to the FreeCAD blog and author of two books featuring FreeCAD and KiCad, both published by Raspberry Pi Press. He will be awarded a grant of £2,000 for the project.

### Pierre-Louis Boyer (paddlestroke): Maintenance, improvement and development of new features on the Sketcher and Assembly workbenches

*Funding approved 2 October 2025.*

Pierre-Louis will continue the ongoing work on improving the Assembly and Sketcher workbenches, with a focus on bugfixing. He will receive €3,000 for each project.

### Pierre-Louis Boyer (paddlestroke): TechDraw: Rework annotation tools

*Funding approved 2 October 2025.*

Pierre-Louis will also create a new annotation tool for TechDraw to replace the existing ones. He will receive EUR€2,000 for this project. A prototype is already available:

### Kacper Donat (kadet1090): Design System and Style Guidelines

*Funding approved 2 October 2025.*

Kacper will develop a design system and style guidelines to help the team improve the consistency of the user interface. He will receive a grant of €5,000 for the project.

### David Kaufman (davidgilkaufman): CAM improvements for the Adaptive operation

*Funding approved 2 October 2025.*

David will improve the Adaptive clearing operation in CAM: enable successful generation at small stepovers, improve automatic diameter selection for entry helix, and add “rest machining” support for adaptive toolpaths. He will receive a grant of $4,250 for the project.

### Francisco Rosa (Francisco-Rosa): Sky domes, sun radiations analysis module

*Funding approved 2 October 2025.*

Francisco will work on his Solar workbench. Expected new features are: creating sun radiation analysis in FreeCAD, and new functions to modify geometry (radius, position, north, etc.) and values (radiation, irradiation, analysis period, and location). He will receive a grant of $2,000.

### Amritpal Singkh (@amrit3701): Enhanced Authentication, Branding Customization, and TrueNAS Integration for Lens Platform

*Funding approved 2 October 2025.*

Amritpal Singkh will resume his work on Ondsel Lens and implement the following features: authentication with Google and OAuth, branding and customization options, FC-Worker update to FreeCAD 1.0.2, and TrueNAS SCALE integration. Amritpal will be awarded a grant of $12,250 from the separate “Ondsel Onwards” fund.

### Pierre-Louis Boyer (paddlestroke): Pattern tools refactor, unification and additional functionality

*Funding approved 8 July 2025.*

Pierre intends to refactor, unify, and enhance existing linear/polar pattern tools in multiple workbenches. He has been awarded a grant of €2,000. The first pull request has already been submitted.

### Brad Eric Hollister: Configuration Space Visualization for Computer-Aided Geometric Design

*Funding approved 8 July 2025.*

This method allows for the visualization of contact curves between pairs of parts. Brad’s job is to implement an exporter in Python that will translate parts and assemblies designed in FreeCAD into the HIPAIR input language. The visualization will be done outside FreeCAD, at least as part of this grant work. Brad has been awarded $500 USD (€430) for the project.

### Marcus Pollio (marcuspollio): Websites improvements initiative — Step 1

*Funding approved 8 July 2025.*

Marcus has been actively working on the redesign and unification of the website for almost a year now. This particular project’s deliverables are features parity between the old and the new website and unification of the Homepage, the News blog, and the Developers Handbook. Marcus has been awarded a grant of €4,000 for this project. 

### Abhiram Masda: CAM/BIM: 2D Nesting Tool for FreeCAD

*Funding approved 8 July 2025.*

Abhiram will either improve the existing nesting algorithm or integrate a more efficient open-source library to reduce material waste and improve layout quality. Abhiram was awarded a grant of ₹150,000 INR (€1,650).

### Max Wilfinger (maxwxyz): Research ISO GPS / GD&T for an overall concept as implementation in FreeCAD

*Funding approved 8 July 2025.*

Max reworked and narrowed down his original proposal from Q1 2025 to researching standards and industry workflows, developing an overall workflow for FreeCAD, and structuring the project for future implementation. No coding is expected to be done as part of this grant work. Max was awarded a grant of €3,000 for the project.

### Jackson Oursland: Assembly Solver Interface Abstraction and Alternative Solver Implementation

*Funding approved 8 July 2025.*

Jackson intends to abstract the use of solvers in the Assembly workbench aiming to add support for the MuJoCo solver (work in progress). Other possibilities include support for the Project Chrono solver. Jackson was awarded a grant of USD $2,000.

### Pieter Hijma: Update OSH Automated Documentation for FreeCAD 1.0

*Funding approved 8 July 2025.*

Pieter will update his OSH Automated Documentation (osh-autodoc) workbench to support FreeCAD 1.0+ (this assumes fixing several issues), the custom PDF compiler, and the documentation. He was awarded a grant of €2,000 for the project.

### Ajinkya Dahale (AjinkyaDahale): New curves for Sketcher

*Funding approved 31 March 2025.*

Ajinkya will develop two new types of curves in Sketcher: restricted and offset curves. Restricted curves are useful when we only need a portion of an external curve that can change. Offset curves are dependent on a parent curve to allow offset for a larger set of curves (independent offset curves already exist in FreeCAD, this is different). Ajinkya was awarded a grant of EUR 2000 for the project.

### Mario Passaglia (@marioalexis84): Maintenance, improvement and development of new features on the FEM workbench

*Funding approved 31 March 2025.*

Mario will continue his work on the FEM workbench. He will fix bugs, maintain and reorganize the code, and take care of various shortcomings in the mesh object, such as the impossibility of handling multiple meshes, time-consuming algorithms to search mesh elements, and the lack of mesh quality checking. Mario was awarded a grant of USD 3000 for the project.

### João Matos (@tritao) and Benjamin Nauck (@hyarion):

*Funding approved 31 March 2025.*

João and Benjamin will modernize FreeCAD’s rendering and selection systems to fix various performance issues on large projects. They will decouple the selection picking and selection rendering system, abstract the raw legacy OpenGL calls into a rendering abstraction layer, and add a modern renderer to Coin. João and Benjamin were awarded a grant of EUR 4000.

### João Matos (@tritao) and Benjamin Nauck (@hyarion): Multithreading architecture improvements in FreeCAD

*Funding approved 31 March 2025.*

They will focus on enhancing the base infrastructure to enable asynchronous operations and deliver asynchronous recomputation of the document and its objects, a multi-threaded signal system, Python async support, and UI enhancements to manage modal or background tasks. They were awarded a grant of EUR 2000 for this project.

### Chris Jones (@ipatch):

*Funding approved 31 March 2025.*

Chris will fix building FreeCAD on macOS with Homebrew. Chris was awarded a grant of USD 1000 for the project.

### Ajinkya Dahale (@jnxd): Refactoring Sketcher, Part 2

*Funding approved 30 January 2025.*

Ajinkya Dahale will continue refactoring Sketcher. The main deliverables are the same as the first time: more methods simplification, testing, and documentation. This will not direct affect features or usability, but it will help other developers contribute to the program.

On top of that, Ajinkya plans to spend more time merging his previous changes into the main development branch (he was holding those off due to v1.0 feature freeze), splitting 10K LOC long classes into smaller, more manageable ones, and helping others review pull requests.

He was awarded a grant of EUR 4000 for the entire project.

### Kacper Donat (@kadet1090): Unified Transparent Previews

*Funding approved 28 November 2024.*

Kacper will work on a new feature preview system that can be used in Part and Part Design. Whenever you need to apply Pad or Loft or any other command, you will get a transparent preview of what you are getting right in the viewport. This is the first part of a larger project intended to unify Part and Part Design. He was awarded a grant of EUR 1,500 for the project.

### Joe Sardos (@Obelisk): Modernize, revise FreeCAD Art Guidelines and Icons

*Funding approved 11 November 2024.*

Joe will write new FreeCAD Art Guidelines along with providing replacement icons to follow the new guidelines. The current art guidelines are well thought-out and provide for reproducible style, however fall short of following current design trends for visual communication and rely heavily on bold and brash color combinations. The idea behind this prohect is to replace the guidelines, document them, work with the FreeCAD community across several platforms to find both style and form that have a general widespread acceptance, and replace them in their entirety. Total expected duration of the project is 3 months (or until complete). Joe was awarded USD 1,750 for the work.

### Jackson Oursland (@oursland): CI Hosting Research Proposal

*Funding approved 4 October 2024.*

Jackson will research various options for FreeCAD to get fast CI runners. Currently, we have free runners from GitHub, but they are relatively slow and concurrency-limited. So Jackson will look into three general options: paid runners on GitHub, self-hosted runners in the cloud (AWS, Azure, GCS, maybe others), and self-hosted runners on premise. Jackson was awarded $500 for the research.

### Adrian Insaurralde (@adrianinsaval): Packaging

*Funding approved 13 July 2023.*

Adrian proposed to work on release packaging, by fixing the conda builds and the process to generate packages for the different platforms, and documenting the process in the developers handbook. Adrian was awarded a grant of 1200 USD.

2024: The contract has been renewed for another year.

### Amulya Paritosh and Harshita Saraswat: Extension to The Component Library

*Funding approved 31 October 2023.*

This project aims to complete the work started by Amulya Paritosh during the Google Summer of Code 2023. Amulya and his colleague Harshita Saraswat will do the remainder of the server-side work (authentication and authorization, launching the server on FreeCAD's server) and client-side work (using GitHub API key to upload files, inserting a component from an online library into FreeCAD). This project has an extension: Amulya will also work on dynamic properties for components in the online library. Amulya Paritosh and Harshita Saraswat were awarded a grant of 2500 USD each for the completion of the original project. Amulya was also awarded a 1000 USD grant for the extension project.

### Kurt Kremitzki (@kkremitzki): Improved Infrastructure Performance and Maintenance

*Funding approved 17 November 2023.*

Kurt will transition all existing services to a declarative format using Ansible, then translate that configuration into a set of Dockerfiles and Docker Compose configuration. He will also create a GitHub repository to centralize the management and automation of the infrastructure. Kurt was awarded a grant of 8000 USD.

## Past Issued Grants

You can find the list of past issued grants in the [Grant Archive](../programs/grant-program-archive).
