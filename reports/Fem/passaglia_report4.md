# Bugfixing and electromagnetic system simulations using CalculiX

FPADF Grant to Mario Passaglia (@marioalexis84)

## Report 4, 2024/12/25

This period was dedicated to bug fixing and code cleanup due 1.0 feature freeze.
Box and elliptical sections were added to beam section objects.
FemMeshShape objects were reworked by adding new base class and the corresponding Python Feature.
Using transactions, cancellation from task panels controls removal of objects added from commands.

Below is the list of merged pull requests:

* [Fem: Disconnect slot when destroying Constraint object](https://github.com/FreeCAD/FreeCAD/pull/15980)
* [Fem: Undo Python object creation by pressing cancel button](https://github.com/FreeCAD/FreeCAD/pull/15960)
* [Fem: Add box and elliptical beam section types - fixes #12614](https://github.com/FreeCAD/FreeCAD/pull/15843)
* [Fem: Remove callback on right click during point marker selection - fixes #13694](https://github.com/FreeCAD/FreeCAD/pull/15767)
* [Fem: Fix link scope for Python objects](https://github.com/FreeCAD/FreeCAD/pull/15669)
* [Fem: Improve FemMeshShape objects](https://github.com/FreeCAD/FreeCAD/pull/15624)
* [Fem: Remove unused gmsh option - fixes #6354](https://github.com/FreeCAD/FreeCAD/pull/15566)
* [Fem: Import/export 1D elements from mesh to vtk - fixes #15541](https://github.com/FreeCAD/FreeCAD/pull/15544)
* [Fem: Remove redundant \*Fix properties in constraint displacement - fixes #14556](https://github.com/FreeCAD/FreeCAD/pull/15531)
* [Fem: Fix mystran preference path - fixes #15348](https://github.com/FreeCAD/FreeCAD/pull/15502)
* [Fem: Handle single value field - fixes #14022](https://github.com/FreeCAD/FreeCAD/pull/15482)
