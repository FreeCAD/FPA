---
title: "The FreeCAD Grant Program Archive"
description:
    "Grants issued to FreeCAD contributors in the past"
layout: default
mermaid: true
---

# {{page.title}}

The following is a reverse-chronological-order list of past projects funded by the FreeCAD Project Association:

## 2025

### David Kaufman (davidgilkaufman): CAM improvements for machining metals

*Funding approved 8 July 2025.*

David aims to improve control of feed rates, submit LeadInOut dressup fixes and improvements, and fix the RampEntry dressup performance. David has been awarded a grant of USD $3,500 for the project. He has already submitted his first pull request for review.

### Pierre-Louis Boyer (paddlestroke): PartDesign: Extrude in two directions

*Funding approved 8 July 2025.*

Pierre has already submitted a pull request that implements this feature (which will fix two issues in the tracker, #20845 and #16175). He has been awarded a grant of €500 for the project.

### Pierre-Louis Boyer (paddlestroke): Maintenance, improvement, and development of new features on the Assembly workbench

*Funding approved 8 July 2025.*

 This project is similar to past grants issued to Mario Passaglia (FEM workbench) and is expected to involve both bugfixing and development of new features. FPA’s recommendation for Pierre is to focus on fixes. He has been awarded a grant of €3,000 for working 10 hours a week on this for the next 3 months.

### Pierre-Louis Boyer (paddlestroke): Maintenance, improvement, and development of new features on the Sketcher workbench

*Funding approved 8 July 2025.*

This project is structured exactly like the Assembly project above: fixes and improvements in Sketcher, 10 hours a week for the next 3 months, for €3,000 total.

### Amritpal Singh (@amrit3701): Make Lens Platform Self-Deployable and Cloud-Agnostic

*Funding approved 31 March 2025.*

Amritpal will resume his work on Ondsel Lens, a FreeCAD-centered online PDM system developed by Ondsel. He will decouple it from Amazon S3 and Lambda to make it self-hosted on any infrastructure. Amritpal was awarded a grant of USD 6500 out of the Ondsel Onward fund contributed by an anonymous sponsor.

## 2024

### Pieter Hijma (@pieterhijma): Improve User Experience of VarSets
 
*Funding approved 9 November 2024.*

Peter will work on improving the user experience of VarSets. The work will include guiding the discussion on the more complicated topics, adding new features that are requested from users, and improving on various small issues. The work is scheduled to be done between January and April 2025. Pieter was awarded EUR 8,000 for the work.

### Turan Furkan Topak (@Reqrefusion): Recommendations and proposal for the improvement of documentation

*Funding approved 9 November 2024.*

Turan will improve the documentation wiki. He will apply fixes for some of the existing issues, improve the search feature, implement responsive design, opening direct user registration after making our Mediwiki instance vandal-safe, improve the editor, set up the ebooks generations for offline use, and improve various other things. Reqrefusion was awarded USD 3,000 for the work.

### Oficine Robotica: teaser video for v1.0

*Funding approved 12 October 2024.*

Oficice Robotica received a grant of $500 for creating a teaser video to demonstrate new features in the upcoming v1.0 release. The video was part of the press release.

### FlachyJoe: bugfixes

*Funding approved 11 October 2024.*

FlachyJoe received an honorary grant of $1000 for working on bug fixes in this development cycle. Most recently he fixed a ton of bugs in Part Design, specifically in the Helix code.

### Chris Jones (@ipatch): Update homebrew-freecad tap with a freecad formula that uses Python v3.12 and Qt v6

*Funding approved 27 August 2024.*

Chris will continue his work on homebrew builds of FreeCAD. This time, he will update the homebrew-freecad tap to link against Python v3.12 and Qt v6 when creating the build. The project is expected to take a few weeks to complete. Chris was awarded a grant of USD $2,000 for the project.

### Bradley Mclean (@bgbsww): Documented procedures and code for supporting debugging FreeCAD C++ and Python from CLion and VSCode

*Funding approved 18 September 2024.*

Brad will write documented procedures and/or code for supporting debugging FreeCAD C++ and Python from CLion and VSCode. The project is expected to take approximately 2 weeks. Brad was awarded a grant of USD $1,500 for the project.

### Pieter Hijma (@pieterhijma): Research Variant Parts

*Funding approved 9 September 2024.*

Pieter Hijma will be working on research for variant parts. A number of FreeCAD features require inserting copy-on-change links, such as referencing external geometry in a body for which SubShapeBinders are used in Part Design. The architecture behind the current implementation involves hidden parts and temporary files and is fragile. Pieter will begin the project by elaborating on the current state of affairs in the forum for developers, then propose patches targeting several aspects of the current implementation. He was awarded a grant of EUR 8,000 for the entire project.

### Pieter Hijma (@pieterhijma): Improve C++ API Documentation

*Funding approved 2 July 2024.*

Pieter will refine a documentation standard in collaboration with the community and Anurag Singh (the other API documentation grantee) and apply the standard to files in the App namespace. The project is expected to last 6 months. Pieter was awarded EUR 8,000 for the entire project.

### Bradley Mclean (@bgbsww): Toponaming issue mitigation

*Funding approved 2 July 2024.*

Bradley will continue to address bugs and missing code as discovered in TNP migration. He will also develop new code as required to address portions of subshapebinder and Sketcher that vary from both the code base at the time of the original TNP branch and from the current Linkstage3 branch. When no bugs are present, he will refactor code in Part and PartDesign based on discoveries during the toponaming project. Bradley was awarded a grant of USD 5,000.

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

### Bradley Mclean (@bgbsww): Toponaming issue mitigation

*Funding approved 7 April 2024.*

Bradley will complete the toponaming project code transfer. He was awarded a grant of USD $5,000 for the work.

### Mario Passaglia (@marioalexis84): Bugfixing and electromagnetic system simulations using CalculiX

*Funding approved 11 February 2024.*

Mario will be working for 7 months to provide solutions for electromagnetic problems leveraging the CalculiX solver. He will also fix bugs in the FEM workbench. Mario was awarded a grant of USD 4,000.

### Bradley Mclean (@bgbsww): Toponaming issue mitigation

*Funding approved 22 January 2024.*

Bradley will be working for two months on integrating fixes for the toponaming issue from RealThunder's branch to upstream FreeCAD. He was awarded a grant of 4800 USD.

### Vincenzo Calligaro (@CalligaroV): Toponaming issue mitigation

*Funding approved 22 January 2024.*

Vincenzo will be working for two months on integrating fixes for the toponaming issue from RealThunder's branch to upstream FreeCAD. He was awarded a grant of 3400 EUR.

## 2023

### Ajinkya Dahale (@jnxd): Curve Geometry Improvements

*Funding approved 26 November 2023.*

Ajinkya will implement general tangency with B-splines and make it possible to preview B-splines when drawing them. He will also investigate the implementation of Bezier curves and improve support for joining curves. Ajinkya was awarded a grant of 5000 USD.

### Chris Jones (@ipatch): Improvements to Homebrew FreeCAD Setup

*Funding approved 12 September 2023.*

Chris will implement autoconnection of homebrew-freecad to self-hosted runners, create GitHub actions to perform autochecks for changed dependencies and then rebuild them, and add regular bundle builds. He will also look into making homebrew-freedesk compatible with linuxbrew. Chris was awarded a grant of 1000 USD.

### Benjamin Bræstrup Sayoc (@bensay): Fix Issue #5903

*Funding approved 3 August 2023.*

Bensay is implementing the autofilling of text fields in SVG page templates in TechDraw workbench. He was awarded a grant of 500 USD.

### AgCaliva (@AgCaliva): Per-document Unit Selector

*Funding approved 3 August 2023.*

AgCaliva implemented a simple per-document unit selector in FreeCAD. He was awarded a grant of 600 USD.

### Alexandre Prokoudine (@prokoudine): New grant program

*Funding approved 19 July 2023.*

Alexandre is revamping the grant program for FreeCAD Project association to make it more attractive to new contributors. He was awarded an overall grant of 3500 USD — 1500 for initial research and 2000 for designing the new program.

## 2022

### Lei Zheng (@realthunder): Topological Naming Problem Mitigation

*Funding approved 15 November 2022.*

In recognition of the efforts he has put into FreeCAD, especially the very large time investment he has made in working with the FreeCAD Maintainers to integrate his work on the topological naming problem, Zheng is awarded a grant of 1000 USD.

### Ajinkya Dahale (@jnxd): Spline Handling in Sketcher

*Funding approved 26 September 2022.*

Ajinkya proposed numerous improvements to the spline handling in the sketcher workbench. He raised funds from many members to do this work and has largely completed stage one. The FPA contributed to the second stage which focused on functionality to create more interesting curves not possible by knot position and slope alone. In recognition of his significant contribution to FreeCAD, Dahale is awarded a grant of 1000 USD.

## Canceled grants

### Dr. Rajeevlochana G. Chittawadigi, Dr. Ravi Kumar V., and Dr. Mohan Kumar S.: Content and Pedagogy Development for Teaching and Learning of Sketcher Workbench in FreeCAD Software

*Funding approved 9 November 2024.*

The team will develop a Sketcher addon for teaching how to use the workbench. Users will follow step-by-step instructions, and the wizard will highlight mistakes (if any) after each step. The project deliverables are spread across 9 months. The team was awarded a grant of USD 6,000 (to be paid to one representative in three steps).

### Anurag Singh (@drLite35): Improve the FreeCAD API documentation

*Funding approved 24 June 2024.*

Anurag will reorganize the existing documentation, enhance docstrings to ensure uniformity and thoroughness, enhance the documentation's visual appeal and usability, automate documentation's generation, and write a contributor guide with instructions for effective documentation. The project is expected to last approx. 5 months. Anurag was awarded USD 4,000 for the entire project.
