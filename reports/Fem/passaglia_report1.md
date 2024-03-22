# Bugfixing and electromagnetic system simulations using CalculiX

FPADF Grant to Mario Passaglia (@marioalexis84)

## Month 1 Report, 2024/03/21

The first month was mainly dedicated to fixing the bugs listed in the FEM roadmap and implementing some feature requests, closing a total of 16 reported items (two of them still to be merged).
Solving items like the issue of post-processing transparency or incorrect representation of mixed mesh elements types, involves studying the SMESH, VTK, and Coin source code for several days to understand how some of its functions work in relation to these topics.

Below is the list of merged pull requests:

* [Fem: Format force constraint in CalculiX writer - fixes #12805](https://github.com/FreeCAD/FreeCAD/pull/12932) 
* [Fem: Partial transparency fix in FemPostObject display modes - close #6996](https://github.com/FreeCAD/FreeCAD/pull/12918)
* [Fem: Use mixed cell types in pipeline unstructured grid - fixes #12581](https://github.com/FreeCAD/FreeCAD/pull/12740)
* [Fem: Add partial support for hexahedral elements - fixes #12526](https://github.com/FreeCAD/FreeCAD/pull/12698)
* [Fem: Create mesh for check type analysis in CalculiX - fixes #12503](https://github.com/FreeCAD/FreeCAD/pull/12612)
* [Fem: Update constraint symbols when moving reference shape - fixes #6093](https://github.com/FreeCAD/FreeCAD/pull/12527)
* [Fem: Prevent stop CalculiX immediately - fixes #12448](https://github.com/FreeCAD/FreeCAD/pull/12499)
* [Fem: Enable checkbox for references mesh groups - fixes #10071, fixes #1214, fixes #5699](https://github.com/FreeCAD/FreeCAD/pull/12437)
* [Fem: Run option in examples open and run analysis - fixes #11056](https://github.com/FreeCAD/FreeCAD/pull/12434)
* [Fem: Move constraint properties to base class and expose symbol node to Python](https://github.com/FreeCAD/FreeCAD/pull/12393)
* [Fem: Use override](https://github.com/FreeCAD/FreeCAD/pull/12290)
* [Fem: Fix restoring old Tie constraint and add support for cyclic symmetry - fixes #12155](https://github.com/FreeCAD/FreeCAD/pull/12289)
* [Fem: Enable "Stop CalculiX" button - fixes #11448](https://github.com/FreeCAD/FreeCAD/pull/12273)
* [Fem: Use expression binding with the constraint tie Tolerance property](https://github.com/FreeCAD/FreeCAD/pull/12228)
* [Fem: Prevent selection of partially attached object - fixes #12163](https://github.com/FreeCAD/FreeCAD/pull/12220)

To be merged:

* [Fem: Improve post-processing object style - fixes #13017](https://github.com/FreeCAD/FreeCAD/pull/13066)
* [Fem: Export post-processing data to VTK - fixes #5816](https://github.com/FreeCAD/FreeCAD/pull/12987)


As the issue list grows in size due to new reported items, there are still about 80 items on the Roadmap, 9 of them marked as bugs, two of which need to pay special attention:
· [#8939](https://github.com/FreeCAD/FreeCAD/issues/8939) - Which causes a crash on some systems, probably due to a race condition based on attempts made to understand the issue.
· [#11306](https://github.com/FreeCAD/FreeCAD/issues/11306) (Scale Constraint Symbols) – The resolution for this is mostly implemented, but the Coin representation of the constraint symbols still needs to be rewritten.


The goal for the next period is focused on implementing feature requests and resolving remaining non-critical bugs.


Special thanks to user @FEA-eng for pull request testing, reporting new issues, and user point of view concepts.
