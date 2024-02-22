---
title: "The FreeCAD Grant Program"
description:
    "Develop new features in FreeCAD and get paid by the community"
layout: default
mermaid: true
---

# {{page.title}}

The FreeCAD Grant Program aims to foster rapid development of FreeCAD and its ecosystem by hiring developers and non-programming contributors to work on specific projects. Their work is funded by the community, grants are issued by the FreeCAD Project Association that collects donations.

For details on program rules, please refer to the [complete rulebook](/handbook/process/grant-program-rules.md).

The program was introduced in 2024 as a successor to the FPA Development Fund launched in August 2022.

## 2024 Program Timeline

1 Mar 2024 — start collecting applications
29 Mar 2024 — stop accepting applications 
12 Apr 2024 — announce accepted applications, work begins
20 Dec 2024 — program recap

Out-of-program grant applications can be submitted at any time.

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

Grant applications are managed in a [public GitHub repository](FIXME) in the FreeCAD project. To submit a grant application, start creating an issue and choose the application template in the form, then fill all the fields.

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

The grant review committee looks at technical aspects of each grant application. Current members: Yorik van Havre (Arch and Draft maintainer), Chris Hennes (overall maintainer), and Pierre-Louis Boyer (Sketcher contributor).

The FPA general assembly then takes the technical review into consideration and looks at non-technical aspects of the proposal. The general assembly is more diverse, its members are both FreeCAD contributors, educators, and representatives of nonprofits and businesses. The full list of members is here.

### What happens if my situation changes and I can’t continue working on a project?

That depends on how much work you have managed to do. If you are in the middle of a project stage and you have already submitted mergeable or already merged pull requests, the FPA can issue a partial compensation for that stage and terminate the contract. 

Alternatively, you can request a partial compensation and a pause to handle your situation. We do not request you to share your life details with us, but we expect you to warn us in a timely manner.

## Ongoing Grant Projects

The following is a reverse-chronological-order list of ongoing projects funded by the FreeCAD Project Association:

### Mario Passaglia (@marioalexis84): Bugfixing and electromagnetic system simulations using CalculiX

*Funding approved 11 February 2024.*

Mario will be working for 7 months to provide solutions for electromagnetic problems leveraging the CalculiX solver. He will also fix bugs in the FEM workbench. Mario was awarded a grant of 4000 USD.

### Max Wilfinger (@maxwxyz): Bugs triaging

*Funding approved 10 February 2024.*

Max will triage bug reports. The contract is for 1 year, with monthly payouts of $500.

### Bradley Mclean (@bgbsww): Toponaming issue mitigation

*Funding approved 22 January 2024.*

Bradley will be working for two months on integrating fixes for the toponaming issue from RealThunder's branch to upstream FreeCAD. He was awarded a grant of 4800 USD.

### Vincenzo Calligaro (@CalligaroV): Toponaming issue mitigation

*Funding approved 22 January 2024.*

Vincenzo will be working for two months on integrating fixes for the toponaming issue from RealThunder's branch to upstream FreeCAD. He was awarded a grant of 3400 EUR.


### Ajinkya Dahale (@jnxd): Curve Geometry Improvements

*Funding approved 26 November 2023.*

Ajinkya will implement general tangency with B-splines and make it possible to preview B-splines when drawing them. He will also implement Bezier curves, add a curvature constraint, and improve support for joining curves. Ajinkya was awarded a grant of 5000 USD.

### Adrian Insauuralde (@adrianinsaval): Packaging

*Funding approved 13 July 2023.*

Adrian proposed to work on release packaging, by fixing the conda builds and the process to generate packages for the different platforms, and documenting the process in the developers handbook. Adrian is awarded a grant of 1200 USD.

### Amulya Paritosh and Harshita Saraswat: Extension to The Component Library 

*Funding approved 31 October 2023.*

This project aims to complete the work started by Amulya Paritosh during the Google Summer of Code 2023. Amulya and his colleague Harshita Saraswat will do the remainder of the server-side work (authentication and authorization, launching the server on FreeCAD's server) and client-side work (using GitHub API key to upload files, inserting a component from an online library into FreeCAD). This project has an extension: Amulya will also work on dynamic properties for components in the online library. Amulya Paritosh and Harshita Saraswat were awarded a grant of 2500 USD each for the completion of the original project. Amulya was also awarded a 1000 USD grant for the extension project.

### Kurt Kremitzki (@kkremitzki): Improved Infrastructure Performance and Maintenance

*Funding approved 17 November 2023.*

Kurt will transition all existing services to a declarative format using Ansible, then translate that configuration into a set of Dockerfiles and Docker Compose configuration. He will also create a GitHub repository to centralize the management and automation of the infrastructure. Kurt was awarded a grant of 8000 USD.

### Chris Jones (@ipatch): Improvements to Homebrew FreeCAD Setup

*Funding approved 12 September 2023.*

Chris will implement autoconnection of homebrew-freecad to self-hosted runners, create GitHub actions to perform autochecks for changed dependencies and then rebuild them, and add regular bundle builds. He will also look into making homebrew-freedesk compatible with linuxbrew. Chris was awarded a grant of 1000 USD.

## Past Issued Grants

You can find the list of past issued grants in the [Grant Archive](/_programs/grant-program-archive.md).
