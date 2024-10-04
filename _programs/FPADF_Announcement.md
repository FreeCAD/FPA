---
title: "The FreeCAD Grant Program"
description:
    "Develop new features in FreeCAD and get paid by the community"
layout: default
mermaid: true
---

# {{page.title}}

The FreeCAD Grant Program aims to foster rapid development of FreeCAD and its ecosystem by hiring developers and non-programming contributors to work on specific projects. Their work is funded by the community, grants are issued by the FreeCAD Project Association that collects donations. The FPA has reserved 50,000 EUR for the program in 2024.

For details on program rules, please refer to the [complete rulebook](/handbook/process/grant-program-rules).

The program was introduced in 2024 as a successor to the FPA Development Fund launched in August 2022.

## 2024 Program Timeline

* 1 Mar 2024 — start collecting applications
* 29 Mar 2024 — stop accepting applications 
* 12 Apr 2024 — announce accepted applications, work begins
* 20 Dec 2024 — program recap

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

The grant review committee looks at technical aspects of each grant application. Current members: Chris Hennes (@chennes, overall maintainer, committee chair), Yorik van Havre (@yorik, Arch and Draft maintainer), Pierre-Louis Boyer (@PaddleStroke, Sketcher contributor), @user1234, @FreeCutter, @chrisb, @shaise, and @drmacro. Anyone who is interested in joining the grant review committee should reach out to Chris Hennes (chennes@freecad.org, @chennes on Discord, @chris_hennes on Telegram, and @chennes on the FreeCAD Forums).

The FPA general assembly then takes the technical review into consideration and looks at non-technical aspects of the proposal. The general assembly is more diverse, its members are both FreeCAD contributors, educators, and representatives of nonprofits and businesses. The full list of members is here.

### What happens if my situation changes and I can’t continue working on a project?

That depends on how much work you have managed to do. If you are in the middle of a project stage and you have already submitted mergeable or already merged pull requests, the FPA can issue a partial compensation for that stage and terminate the contract. 

Alternatively, you can request a partial compensation and a pause to handle your situation. We do not request you to share your life details with us, but we expect you to warn us in a timely manner.

## Ongoing projects funded by the FPA

### Pieter Hijma (@pieterhijma): Research Variant Parts

*Funding approved 9 September 2024.*

Pieter Hijma will be working on research for variant parts. A number of FreeCAD features require inserting copy-on-change links, such as referencing external geometry in a body for which SubShapeBinders are used in Part Design. The architecture behind the current implementation involves hidden parts and temporary files and is fragile. Pieter will begin the project by elaborating on the current state of affairs in the forum for developers, then propose patches targeting several aspects of the current implementation. He was awarded a grant of EUR 8,000 for the entire project.

### Bradley Mclean (@bgbsww): Documented procedures and code for supporting debugging FreeCAD C++ and Python from CLion and VSCode

*Funding approved 18 September 2024.*

Brad will write documented procedures and/or code for supporting debugging FreeCAD C++ and Python from CLion and VSCode. The project is expected to take approximately 2 weeks. Brad was awarded a grant of USD $1,500 for the project.

### Chris Jones (@ipatch): Update homebrew-freecad tap with a freecad formula that uses Python v3.12 and Qt v6

*Funding approved 27 August 2024.*

Chris will continue his work on homebrew builds of FreeCAD. This time, he will update the homebrew-freecad tap to link against Python v3.12 and Qt v6 when creating the build. The project is expected to take a few weeks to complete. Chris was awarded a grant of USD $2,000 for the project.

### Aleksandr Prokudin (@prokoudine): Blog maintenance

*Funding approved 2 July 2024.*

Aleksandr will post weekly recaps of FreeCAD development and write 2 to 4 additional news posts a month. The contract is for 1 year, with monthly payouts of EUR 500.

### Pieter Hijma (@pieterhijma): Improve C++ API Documentation

*Funding approved 2 July 2024.*

Pieter will refine a documentation standard in collaboration with the community and Anurag Singh (the other API documentation grantee) and apply the standard to files in the App namespace. The project is expected to last 6 months. Pieter was awarded EUR 8,000 for the entire project.

### Anurag Singh (@drLite35): Improve the FreeCAD API documentation

*Funding approved 24 June 2024.*

Anurag will reorganize the existing documentation, enhance docstrings to ensure uniformity and thoroughness, enhance the documentation's visual appeal and usability, automate documentation's generation, and write a contributor guide with instructions for effective documentation. The project is expected to last approx. 5 months. Anurag was awarded USD 4,000 for the entire project.

### Andrianos Karampilis: User manual update

*Funding approved 9 June 2024.*

Andrianos is updating the user manual in the wiki. The goal is to update all 23 chapters of the manual to bring it up to speed with the current state of FreeCAD and explore the possibility of releasing EPUB and PDF versions of the manual. The compensation for this project is USD 2,500.

### Ajinkya Dahale (@jnxd): Refactoring Sketcher

*Funding approved 3 June 2024.*

Ajinkya Dahale will be making Sketcher more manageable to maintain and extend. His project has three deliverables:

- Simplifying methods: rewriting gigantic methods in Sketcher so that geometry special cases would be ideally moved to helper methods for reuse or at least divided into pieces for each case, making an easier reading.
- Tests: this will be done before major refactoring Sketcher to avoid regressions.
- Documentation: complete documentation of methods and a document listing best practices to follow when performing such refactoring elsewhere.

He was awarded a grant of USD $5,000.

### Francisco de Assis Rosa (@Francisco-Rosa): Design new components for the FreeCAD library

*Funding approved 12 May 2024.*

Francisco will be designing furniture and parametric components for the FreeCAD library. Deliverables are “a few dozen pieces of furniture and parametric components (for architectural and engineering projects) for immediate use in FreeCAD”. He was awarded a grant of USD $5,000.

### Mario Passaglia (@marioalexis84): Bugfixing and electromagnetic system simulations using CalculiX

*Funding approved 11 February 2024.*

Mario will be working for 7 months to provide solutions for electromagnetic problems leveraging the CalculiX solver. He will also fix bugs in the FEM workbench. Mario was awarded a grant of USD 4,000.

### Max Wilfinger (@maxwxyz): Bugs triaging

*Funding approved 10 February 2024.*

Max will triage bug reports. The contract is for 1 year, with monthly payouts of USD 500.

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

You can find the list of past issued grants in the [Grant Archive](../programs/grant-program-archive).
