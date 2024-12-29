# Sketcher Refactor: June 2024 Update

Pull Request(s): https://github.com/FreeCAD/FreeCAD/pull/14696

## What was done

1. Learning about what changes may be needed. Mainly from "Clean Code" by Bob Martin.
2. SketchObject was targeted, since it has a lot of changes possible, and, not having GUI components, it's easier to add tests.
3. The number of methods having high complexity reduced from 32 to ~22. Some of them are just above the threshold of 26.
4. Tests for getPoint, split, and trim.
5. Some changes done in manipulating if-then statements and for loops. This was done to identify the potential before going forward. Tests will be added before the PR is ready to merge.

|------------------------------------|-------------------|------------------|
| Function                           | Complexity before | Complexity after |
|------------------------------------|-------------------|------------------|
| getPoint                           | 38                |                  |
| delGeometry                        | 28                |                  |
| delGeometriesExclusiveList         | 34                |                  |
| delConstraintOnPoint               | 102               | 91               |
| transferFilletConstraints          | 99                | 99               |
| fillet                             | 165               | 165              |
| trim                               | 233               | 74               |
| (lambda within trim)               | 40                | (removed)        |
| split                              | 95                | 26               |
| join                               | 28                |                  |
| isCarbonCopyAllowed                | 50                |                  |
| addSymmetric                       | 190               | 190              |
| getSymmetric                       | 68                | 68               |
| addCopy                            | 267               | 267              |
| removeAxesAlignment                | 65                | 56               |
| exposeInternalGeometry             | 153               | 146              |
| deleteUnusedInternalGeometry       | 160               | 147              |
| modifyBSplineKnotMultiplicity      | 59                | 59               |
| insertBSplineKnot                  | 54                | 26               |
| carbonCopy                         | 51                | 51               |
| delExternal                        | 36                |                  |
| validateExternalLinks              | 39                |                  |
| rebuildExternalGeometry            | 179               | 179              |
| getCoincidenceGroups               | 32                | 26               |
| getGeometryWithDependentParameters | 30                |                  |
| onChanged                          | 59                | 59               |
| migrateSketch                      | 104               | 104              |
| port_reversedExternalArcs          | 42                | 42               |
| AutoLockTangencyAndPerpty          | 28                |                  |
| getSubObject                       | 67                | 67               |
| setExpression                      | 39                | 39               |
| getElementName                     | 32                | 32               |
|------------------------------------|-------------------|------------------|

## Next steps

1. Complete tests for remaining changed functions.
2. Abstract out common code dependent on type of geometry. Some of these tasks may be movable to the `Part::Geometry` subclasses directly (like getting a segment of the curve), but others have to be explicitly checked within Sketcher (like getting the point based on `PointPos`).
3. Refactor further, creating helper functions for repeated code.
4. Move on to other files.

## Lessons

1. CogComp doesn't necessarily give the complete picture. For example, it doesn't increase within functions.
