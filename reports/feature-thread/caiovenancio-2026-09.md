# Summary of Activities – Thread Feature – September 2026

## Second Stage – In Progress – Geometry and Profile Integration

The second stage ended up extending through September. Work this month focused on cosmetic threading, thread depth controls, and the transition to sketch-defined thread profiles.

The up-to-geometry and up-to-first depth modes were added, modeled thread generation for ISO Metric and ISO Metric Fine was corrected, and thread-end handling and validation were introduced. This also fixed thread preview, cosmetic overlays, invalid lateral face referencing, and crashes when opening thread files.

Threads can now be defined in .FCStd files, where they are loaded, validated, and normalized for size and pitch, which are then used in modeling.

Automated regression coverage was expanded for metric modeled threads and profile validation. Adding new tests and resuming the current ones are expected for next month. 

The third stage has not started yet: broader validation of the second stage is still needed, and conical threads remain the main blocker before advancing, as they are not yet fully supported. 

The pull request is available here: [https://github.com/FreeCAD/FreeCAD/pull/29613](https://github.com/FreeCAD/FreeCAD/pull/29613)

The PR remained a **Draft**, as the new geometry and profile-loading paths still required further testing and review.

## Progress Checklist

| Expected Requirement                                                         | Status                                      |
| ---------------------------------------------------------------------------- | ------------------------------------------- |
| Support for internal and external threads on cylinders and cones.            | In Progress (cones in progress)             |
| Support for standardized metric profiles and custom profiles.                | ✓                                          |
| Cosmetic thread overlay in Coin3D.                                           | ✓                                          |
| Dynamic 3D View updates when changing parameters or visibility.              | ✓                                          |
| Unit and integration test suite passing without regressions.                 | In Progress                                 |
| Feature page created/updated for the official FreeCAD Wiki.                  | In Progress                                 |
