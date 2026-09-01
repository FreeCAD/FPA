# Summary of Activities – Thread Feature – August 2026

## Second Stage – In Progress

The second stage of development is currently in progress.

The feature now supports loading `.FCStd` thread profile files from both standard installation directories and the user’s AppData directory. Internal and external threads are functional, including start-object selection. Further validation and testing are currently underway.

Based on the current development status, the final delivery may require an **additional 15 days** to complete the remaining implementation, testing, and bug fixes.

Development is ongoing for custom thread profiles, conical threads, clearance standards, depth options such as **Up To Geometry** and **Through All**, as well as performance optimizations. Several bugs and edge cases have also been identified and are currently being addressed.

Approximately **149 of the planned 175 development hours** have been completed.

The current pull request is available here:
[https://github.com/FreeCAD/FreeCAD/pull/29613](https://github.com/FreeCAD/FreeCAD/pull/29613)
Additional implementation details, progress, and ongoing changes can be found in the pull request. The PR is **not yet ready for merging**, as development and validation are still in progress.

## Progress Checklist

| Expected Requirement                                                         | Status      |
| ---------------------------------------------------------------------------- | ----------- |
| Support for internal and external threads on cylinders and cones.            | In Progress |
| Support for standardized metric profiles and custom profiles.                | In Progress |
| Cosmetic thread overlay in Coin3D.                                           | In Progress |
| Dynamic 3D View updates when changing parameters or visibility.              | In Progress |
| Unit and integration test suite passing without regressions.                 | In Progress |
| Feature page created/updated for the official FreeCAD Wiki.                  | In Progress |