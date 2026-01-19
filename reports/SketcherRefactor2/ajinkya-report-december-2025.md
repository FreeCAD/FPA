# Sketcher Refactor 2: December 2025/January 2026 Update


## What was done

* Work log includes changes from May 2025.
* Still more delays from a lot of travel, plus day job.
* Merging halted in preparation for 1.1. Stage 5 (#22951) is now merged.
* Lot of time putting out fires: corner cases and/or seg-fault issues in `trim` and `addSymmetric`.
* Merged bugfix PRs include:
 * #26886
 * #25914
 * #25536
 * #25054
 * #22577
* Reviews on a few other PRs
* (An updated table of current cognitive complexity can be added once #14696 is again rebased)

## Next steps

* Continue merging work as older stages are completed
* Remove all/most of the code that changes data in Sketcher _without breaking the sketch_. Current progress in https://github.com/AjinkyaDahale/FreeCAD/tree/sk-move-out-sketchobject-changes.
* Some things that still need to stay: delete/add geometry/constraints/externalgeometry.
* Create a "function object" so that the editing procedure is straightforward.
* No new refactoring grant planned, ideally should be done by everyone.

