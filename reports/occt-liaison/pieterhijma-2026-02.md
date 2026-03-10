## Summary of Activities - OCCT Liaison - February 2026

### Update the project

The [OCCT Liaison
project](https://github.com/orgs/FreeCAD/projects/32/views/1?layout=table) has
received updates on various issues.

### Investigate [Issue #25720](https://github.com/FreeCAD/FreeCAD/issues/25720)

This is a blocker that was suspected to have to do with OCCT.  After trying
with multiple versions I could conclude that it was not OCCT.

### Submit bug reports for issues

- [Issue #25158](https://github.com/FreeCAD/FreeCAD/issues/25158)
- [Issue #24115](https://github.com/FreeCAD/FreeCAD/issues/24115)

There is a group of issues originating from doing CAM with breps.  I've
submitted bug reports to OCCT for two of them.

### Check out Evaluation Representations

I was pinged by OCCT about adding evaluation representations to have more
precise and performance evaluation for often used functions on BReps.  I've
investigated this and need to start a discussion on this within FreeCAD.

### Port FreeCAD to OCCT 8

The OCCT 8 API is significantly changing and because of that, lots of changes
are required in FreeCAD and Salome.  [Draft PR
#25502](https://github.com/FreeCAD/FreeCAD/pull/25502) brings FreeCAD up-to-date with the new OCCT 8 API.

