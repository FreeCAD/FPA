# Summary of Activities – Thread Feature – July 2026

## First Stage Completed

The GUI is largely complete, and face selection is working properly.
Additional parameters, such as thread runout and custom thread definitions, may be added next month.
Several major files have been added, including:
- FeatureThread.cpp
- TaskThreadParameters.cpp
- TaskThreadParameters.ui
- ThreadUtils.cpp
- ViewProviderThread.cpp

A basic face selection implementation is in place. It accepts cylindrical and conical lateral faces while rejecting unsupported face types. The task panel has all of its initial fields implemented.
Code quality is being improved continuously, and automated tests are being written to prevent regressions and support future refactoring between the Thread feature and the Hole feature.
Thread geometry modelling is currently in progress.
Approximately **75 of the planned 175 development hours** have been completed.

The pull request is available here: https://github.com/FreeCAD/FreeCAD/pull/29613
It is not intended to be merged yet, as the thread symbol and thread geometry modeling are still under development.

## Progress Checklist

| Expected Requirement                             | Status |
| ------------------------------------------------ | ------ |
| New `Thread` feature infrastructure exists       | ✓      |
| Can select cylindrical faces                     | ✓      |
| Can select conical faces                         | ✓      |
| Unsupported faces are rejected                   | ✓      |
| OCCT geometry parameters are extracted correctly | ✓      |
| Feature stores the selected face properly        | ✓      |
| Initial automated tests exist                    | ✓      |
| Code architecture is suitable for Stage 2        | ✓      |

Some items in this checklist may not be fully complete in every edge case, but overall they accurately reflect the current state of development.
