# Bugfixing and electromagnetic system simulations using CalculiX

FPADF Grant to Mario Passaglia (@marioalexis84)

## Report 5, 2024/12/25

Period dedicated to bug fixing and developing a new implementation for meshing using the Netgen mesher.
For several years now, the Netgen plugin of the internal Salome SMESH version is broken, so meshing with Netgen was only possible on Windows and AppImage using an unmaintained external plugin.
This new implementation is based on the Netgen Python bindings and exposes most of the parameters available in the mesher.
Also, now both the Gmsh and Netgen processes do not block the program and it is possible to cancel the process at any time.
The view provider for FemMesh and Postprocessing objects was improved by fixing flickering between faces and the wireframe.

Below is the list of merged pull requests:

* [Fem: Fix flickering between faces and wireframe in FemPostObject view provider](https://github.com/FreeCAD/FreeCAD/pull/16867)
* [Fem: Fix flickering between faces and wireframe in FemMesh view provider](https://github.com/FreeCAD/FreeCAD/pull/16714)
* [Fem: Use shape global placement in Mesh Netgen new implementation](https://github.com/FreeCAD/FreeCAD/pull/16705)
* [Fem: Use reference subshape transformation on the underlying geometry when finding points for constraint symbols](https://github.com/FreeCAD/FreeCAD/pull/16673)
* [Fem: Minor change to MeshGmsh task panel and renaming mesh properties group](https://github.com/FreeCAD/FreeCAD/pull/16602)
* [Fem: Enable cancel meshing for Gmsh - fixes #5914](https://github.com/FreeCAD/FreeCAD/pull/16515)
* [Fem: New implementation of FemMesh Netgen object](https://github.com/FreeCAD/FreeCAD/pull/16433)
* [Fem: Set Elmer result output format to Ascii](https://github.com/FreeCAD/FreeCAD/pull/16394)
* [Fem: Allow only one shape type per mesh group - Partially revert #16076](https://github.com/FreeCAD/FreeCAD/pull/16351)
* [Fem: Use regex to search gmsh groups items and fix physical group item id](https://github.com/FreeCAD/FreeCAD/pull/16076)
