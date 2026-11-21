# Summary of Activities – Thread Feature – October 2026

## Second Stage – In Progress - Validation and Documentation

Development during October focused on fixing cosmetic behavior, extending conical-thread support, and aligning the thread feature with the hole conventions. 

Code quality is being improved now to make it easier to review soon.

Late in the month, work began on the third stage in another branch: refactoring the Hole class to extract the shared threading logic into a reusable component.

Sketch-defined profiles were completed for the common thread standards, including ISO Metric Fine, NPT, Whitworth, and others.
Cosmetic threads now use a resolved start position and depth. The internal modeled thread hole entrance is now fixed, and the generated geometry is limited to the supported face on external modeled threads. 

The Tapered and TaperedAngle properties were removed, and conicity is now derived from the selected supporting face. User-facing thread data was revised to show nominal labels for imperial sizes instead of millimeter conversions, and the full thread designation is now displayed more clearly and completely than before.

The automated suite was consolidated into 17 core Thread tests covering profile loading, profile-based end trimming, all four extent modes, internal and external modeled threads, cosmetic threads, conical supports, and metric and BSP geometry signatures.

The pull request is available here: [https://github.com/FreeCAD/FreeCAD/pull/29613](https://github.com/FreeCAD/FreeCAD/pull/29613)

The PR remains a **Draft**. Broader validation and review of all bundled standards, custom definitions, conical cases, interface performance, and documentation is still required before merging. Code quality is also being improved.

## Progress Checklist

| Expected Requirement                                                         | Status      |
| ---------------------------------------------------------------------------- | ----------- |
| Support for internal and external threads on cylinders and cones.            | ✓           |
| Support for standardized metric profiles and custom profiles.                | ✓           |
| Cosmetic thread overlay in Coin3D.                                           | ✓           |
| Dynamic 3D View updates when changing parameters or visibility.              | ✓           |
| Unit and integration test suite passing without regressions.                 | ✓           |
| Feature page created/updated for the official FreeCAD Wiki.                  | In Progress |

Some items in this checklist may not be fully complete in every edge case, but overall they accurately reflect the current state of development.