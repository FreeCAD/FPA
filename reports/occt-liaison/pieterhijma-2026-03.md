## Summary of Activities - OCCT Liaison - March 2026

### Contract renewal

The contract has been renewed with more tasks.  Thank you to all FPA members
for their vote of confidence.

### Update the project

The [OCCT Liaison
project](https://github.com/orgs/FreeCAD/projects/32/views/1?layout=table) has
received updates on various issues.

### Various issues were updated

Much attention has gone to check things for the release.  This month was about
catching up on various issues.

- [#25475](https://github.com/FreeCAD/FreeCAD/issues/25475)
- [#27211](https://github.com/FreeCAD/FreeCAD/issues/27211)
- [#16114](https://github.com/FreeCAD/FreeCAD/issues/16114)
- [#28092 (closed)](https://github.com/FreeCAD/FreeCAD/issues/28092)
  - provide user feedback on how to deal with offset with different radii
- [#24111 (should be closed)](https://github.com/FreeCAD/FreeCAD/issues/24111)
  - provide user feedback on infinite bounding box
- [#25193 (solved in OCCT)](https://github.com/FreeCAD/FreeCAD/issues/25193)
  - determined that the issue is solved in new OCCT
- [#24398 (solved by CAM team)](https://github.com/FreeCAD/FreeCAD/issues/23498)
  - an issue related to CAM, has been fixed apparently
- [#26161](https://github.com/FreeCAD/FreeCAD/issues/27302)
- [#16898](https://github.com/FreeCAD/FreeCAD/issues/16898)
- [#22031](https://github.com/FreeCAD/FreeCAD/issues/22031)
- [#28851](https://github.com/FreeCAD/FreeCAD/issues/28851)
  - reported a regression, file shows different results on different OSs

### Submit bug reports for issues

- [#25169](https://github.com/FreeCAD/FreeCAD/issues/25169)
- [#5561](https://github.com/FreeCAD/FreeCAD/issues/5561)
  - Very long standing issue in which a fillet or chamfer cannot meet opposite
    edges, [reported on forum](https://forum.freecad.org/viewtopic.php?p=881024#p881024) as well.

### Discuss correct preview with failing final version

In issues such as [#18656](https://github.com/FreeCAD/FreeCAD/issues/18656) and
[#27302](https://github.com/FreeCAD/FreeCAD/issues/27302), the preview shows a
correct result while the final shape is misformed.  Before investigating
further, I wanted to discuss with kadet.  According to kadet, in these cases,
the shape that is computed for the preview is simply correct, but then when the
final boolean is done, the boolean fails.

### Response from forum thread

I'm getting response from the [Community Help Requested](https://forum.freecad.org/viewtopic.php?p=839428#p839428).  Thanks
to the users that are helping me investigate fillet related issues!

### Started discussion on Evaluation Representations

I started a discussion on Discord on Evaluation Representations after being
pinged by OCCT on this.

### Port FreeCAD to OCCT 8

The OCCT 8 API is significantly changing and because of that, lots of changes
are required in FreeCAD and Salome.  [Draft PR
#25502](https://github.com/FreeCAD/FreeCAD/pull/25502) brings FreeCAD up-to-date with the new OCCT 8 API and has had minor changes.









