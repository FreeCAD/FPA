# Bugfixing and electromagnetic system simulations using CalculiX

FPADF Grant to Mario Passaglia (@marioalexis84)

## Month 2 Report, 2024/05/27

This second period was mostly dedicated to working on the view providers of the objects, both the constraints and the meshes. Along with the resolution of the symbol scaling problem, a new framework was introduced for the creation and manipulation of symbols for constraint objects, both in C++ and Python. This is expected to simplify the process of adding new view providers. See [#13274] (https://github.com/FreeCAD/FreeCAD/pull/13274).
In addition, support for the functionalities offered by CalculiX for heat transfer analysis was increased.
The work on rigid body constraint started by @AjinkyaDahale with contributions from @FEA-eng  was completed, which represents an improvement in relation to torsion analysis.

Below is the list of merged pull requests:

* [Fem: Update ReferenceNode property from task dialog - fixes #14172](https://github.com/FreeCAD/FreeCAD/pull/14183)
* [Fem: Increase size of reference node symbol in rigid body constraint - fixes #14133](https://github.com/FreeCAD/FreeCAD/pull/14158)
* [Fem: Don't hide input filter with DataAtPoint and DataAlongLine - fixes #14135](https://github.com/FreeCAD/FreeCAD/pull/14157)
* [Fem: Highlight active Analysis according to user defined color](https://github.com/FreeCAD/FreeCAD/pull/14047)
* [Fem: Improve constraint section print](https://github.com/FreeCAD/FreeCAD/pull/14046)
* [Fem: Load heat flux from CalculiX results - fixes #12117](https://github.com/FreeCAD/FreeCAD/pull/14019)
* [Fem: Add constraint rigid body](https://github.com/FreeCAD/FreeCAD/pull/13900)
* [Fem: Reset field color bar - fixes #13695](https://github.com/FreeCAD/FreeCAD/pull/13820)
* [Fem: Rescaling and transparency fix for heat constraint symbols](https://github.com/FreeCAD/FreeCAD/pull/13723)
* [Fem: Make pipeline filters invisible if a new filter is added](https://github.com/FreeCAD/FreeCAD/pull/13701)
* [Fem: Save and restore custom colors of elements in mesh - fixes #6131](https://github.com/FreeCAD/FreeCAD/pull/13698)
* [Fem: Constraint symbol scaling based on shape size - fixes #7030](https://github.com/FreeCAD/FreeCAD/pull/13586)
* [Fem: Remove unused view properties](https://github.com/FreeCAD/FreeCAD/pull/13569)
* [Fem: Add radiation heat transfer](https://github.com/FreeCAD/FreeCAD/pull/13466)
* [Fem: Add element types to ABAQUS writer](https://github.com/FreeCAD/FreeCAD/pull/13464)
* [Fem: Fix display modes order - fixes #13326](https://github.com/FreeCAD/FreeCAD/pull/13358)
* [Fem: Constraint symbol scaling](https://github.com/FreeCAD/FreeCAD/pull/13274)


To be merged:

* [Fem: Cleanup ViewProviderFemConstraint and update constraint transform](https://github.com/FreeCAD/FreeCAD/pull/14353)


The goal for the next period is focused on fixing bug due to feature freeze start.
