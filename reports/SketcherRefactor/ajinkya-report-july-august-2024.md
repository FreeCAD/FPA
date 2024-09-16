# Sketcher Refactor: August 2024 Update

Pull Request(s):
* https://github.com/FreeCAD/FreeCAD/pull/14696 (WIP)
* https://github.com/FreeCAD/FreeCAD/pull/15811 (ready to merge)

## What was done

1. In addition to `SketchObject.cpp`, some other files were also touched, including `GCS.cpp` (in planegcs) and `CommandConstraints.cpp` (in Gui).
2. That said, `SketchObject` remained the main target. This has far more offending methods than any other.
3. Cumulatively, the number of methods having high complexity in `SketchObject` has reduced from 43 to 35, with a majority of methods receiving at least some reduction. Note that both numbers have increased since the previous report because of addition toponaming-related code.
4. Some of the remaining complex methods are just above the threshold of 26. Additionally, some complexity is caused since `clang-tidy` first expands macros for the estimation. If and when macros are replaced by functions, this complexity will automatically drop.
5. Some additional tests were added to validate constraint changes after geometry deletion.
6. A "ready to merge" PR was created including changes that have been covered by tests.
2. Moved code that gets arc of a given curve to the `Part::Geometry` subclasses directly. These new methods can be used in methods like `trim`, `split` and possibly `expand`. For now, only `trim` has been changed.
7. The `trim` method was further changed to fix some failing tests, as well as to reinstate some constraint modifications that were temporarily removed (leading to loss of said constraints).

Changes within SketchObject:
|------------------------------------|-------------------|------------------|------|--------|
| Function                           | Complexity before | Complexity after | Test | Macros |
|------------------------------------|-------------------|------------------|------|--------|
| buildShape                         | 64                | 57               |      |        |
| buildInternals                     | 32                | 32               |      | x      |
| generateId                         | 112               | 112              |      | x      |
| getPoint                           | 38                |                  | x    |        |
| delGeometry                        | 31                |                  |      |        |
| delGeometriesExclusiveList         | 34                |                  |      |        |
| toggleExternalGeometryFlag         | 27                |                  |      |        |
| delConstraintOnPoint               | 102               | 52               |      |        |
| transferFilletConstraints          | 99                | 69               |      |        |
| fillet                             | 165               | 114              |      |        |
| trim                               | 233               | 75               | x    |        |
| (lambda within trim)               | 40                | 0                |      |        |
| split                              | 95                | 26               | x    |        |
| join                               | 28                |                  |      |        |
| isCarbonCopyAllowed                | 50                |                  |      |        |
| addSymmetric                       | 190               | 104              |      |        |
| getSymmetric                       | 68                | 66               |      |        |
| addCopy                            | 267               | 172              |      |        |
| (lambda within addCopy)            | 0                 | 123              |      |        |
| removeAxesAlignment                | 65                | 36               |      |        |
| exposeInternalGeometry             | 153               |                  |      |        |
| deleteUnusedInternalGeometry       | 160               |                  |      |        |
| modifyBSplineKnotMultiplicity      | 59                | 41               |      |        |
| insertBSplineKnot                  | 54                | 26               |      |        |
| carbonCopy                         | 70                | 66               |      |        |
| addExternal                        | 36                | 36               |      |        |
| delExternalPrivate                 | 73                | 27               |      |        |
| attachExternal                     | 39                | 39               |      | x      |
| validateExternalLinks              | 39                |                  |      |        |
| rebuildExternalGeometry            | 439               | 395              |      |        |
| fixExternalGeometry                | 63                | 63               |      | x      |
| getCoincidenceGroups               | 32                | 26               |      |        |
| getGeometryWithDependentParameters | 30                |                  |      |        |
| validateExpression                 | 45                | 35               |      |        |
| onChanged                          | 263               |                  |      | x      |
| onGeometryChanged                  | 0                 | 45               |      | x      |
| onExternalGeoChanged               | 0                 | 58               |      | x      |
| onExpressionEngineChanged          | 0                 | 40               |      | x      |
| updateGeometryRefs                 | 161               | 161              |      | x      |
| restoreFinished                    | 71                | 71               |      | x      |
| migrateSketch                      | 104               | 57               |      |        |
| port_reversedExternalArcs          | 42                | 42               |      |        |
| AutoLockTangencyAndPerpty          | 28                |                  |      |        |
| getSubObject                       | 75                | 70               |      |        |
| getHigherElements                  | 27                | 27               |      |        |
| setExpression                      | 39                | 39               |      | x      |
| getElementName                     | 36                | 36               |      |        |
| checkSubName                       | 35                | 35               |      | x      |
|------------------------------------|-------------------|------------------|------|--------|
(A complexity of 0 implies that the method was deleted/did not previously exist. Empty complexity entry impliex that the complexity was not reported by `clang-tidy` since it fell below the threshold of 25.)

## Next steps

1. Complete tests for remaining changed functions.
2. Abstract out more common code dependent on type of geometry, especially checks that can only be done within Sketcher (like getting the point based on `PointPos`). This is intended so that there are fewer places to change as new curve types are added.
3. Refactor further, creating helper functions for repeated code.
4. Eventually break down `SketchObject` (as well as other large classes) such that the single responsibility principle is respected.
