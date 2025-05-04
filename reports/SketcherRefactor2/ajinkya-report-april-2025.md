# Sketcher Refactor 2: April 2025 Update


## What was done

* Work log includes changes from December 2024.
* Plenty of delays from a lot of travel, plus day job.
* Things are now getting merged.
* Lot of time putting out fires: corner cases and memory leak issues in `trim`.
* Added a `SketchObject::replaceGeometries` method, that handles the riskier operations. If an error related to memory leak exists, it has to be here.

Current status, with remaining "complex" functions shown (the "before", as I added in the previous reports, doesn't make much sense now that a lot of work is merged):

| Line     | Function                     | Complexity | Test | Macros |
|----------|------------------------------|------------|------|--------|
| 330:20   | `buildShape`                 | 43         |      |        |
| 467:31   | `buildInternals`             | 32         |      | x      |
| 774:20   | `generateId`                 | 59         |      | x      |
| 2386:19  | `delConstraintOnPoint`       | 35         |      |        |
| 2510:20  | `transferFilletConstraints`  | 69         |      |        |
| 3547:20  | `deriveConstraintsForPieces` | 29         |      |        |
| 4145:19  | `addSymmetric`               | 78         |      |        |
| 4373:44  | `getSymmetric`               | 56         |      |        |
| 4764:19  | `addCopy`                    | 172        |      |        |
| 4809:32  | (lambda within `addCopy`)    | 123        |      |        |
| 5317:19  | `removeAxesAlignment`        | 36         |      |        |
| 6884:19  | `carbonCopy`                 | 66         |      |        |
| 7092:19  | `addExternal`                | 47         |      |        |
| 7255:20  | `delExternalPrivate`         | 27         |      |        |
| 7430:19  | `attachExternal`             | 39         |      | x      |
| 8032:6   | `processEdge`                | 144        |      |        |
| 8581:20  | `rebuildExternalGeometry`    | 345        |      |        |
| 9044:20  | `fixExternalGeometry`        | 63         |      | x      |
| 9618:27  | `validateExpression`         | 35         |      |        |
| 9889:20  | `onGeometryChanged`          | 45         |      | x      |
| 10023:20 | `onExternalGeoChanged`       | 58         |      | x      |
| 10146:20 | `onExpressionEngineChanged`  | 40         |      | x      |
| 10198:20 | `updateGeometryRefs`         | 121        |      | x      |
| 10432:20 | `restoreFinished`            | 71         |      |        |
| 10489:20 | `migrateSketch`              | 57         |      |        |
| 10752:19 | `port_reversedExternalArcs`  | 42         |      |        |
| 10943:36 | `getSubObject`               | 70         |      |        |
| 11083:15 | `getHigherElements`          | 27         |      |        |
| 11140:20 | `setExpression`              | 39         |      | x      |
| 11177:36 | `getElementName`             | 36         |      |        |
| 11271:33 | `checkSubName`               | 70         |      | x      |

## Next steps

* Remove all/most of the code that changes data in Sketcher _without breaking the sketch_.
* Some things that still need to stay: delete/add geometry/constraints/externalgeometry.
* Create a "function object" so that the editing procedure is straightforward.
* No new refactoring grant planned, ideally should be done by everyone.

