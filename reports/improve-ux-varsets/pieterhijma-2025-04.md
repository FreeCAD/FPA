## Summary of Activities - VarSet User Experience - April 2025

### Update the project page

I've updated the [project page](https://github.com/orgs/FreeCAD/projects/30/views/1).

### Visibility icon for VarSet

Last month I couldn't find a satisfactory solution.  This month I have:
- [#20649 (merged)](https://github.com/FreeCAD/FreeCAD/pull/20649)
- [#20573 (closed)](https://github.com/FreeCAD/FreeCAD/pull/20573)

### Units in the VarSet dialog

Last month, I worked on units in the VarSet dialog, but I couldn't make them
work properly.  This month I have:
- [#20570 (merged)](https://github.com/FreeCAD/FreeCAD/pull/20570).

### Frame around the value field in the VarSet dialog

The value field lacked a frame.  This has been fixed in:
- [#20582 (merged)](https://github.com/FreeCAD/FreeCAD/pull/20582)

### Immediate access to value field VarSet dialog

In the VarSet dialog, it was necessary to first define a name and type, and
only then the value field would appear, leading to a strange user experience.
This has been fixed in:

- [#20824 (merged)](https://github.com/FreeCAD/FreeCAD/pull/20824)

### Add multiple properties VarSet dialog

In [issue #20637](https://github.com/FreeCAD/FreeCAD/issues/20637) there are
different opinions on how the user flow should be when adding multiple
properties in the VarSet dialog.  I started a discussion with the Design
Working Group, but there does not seem to be much consensus either.

### Refactoring properties

A larger task in the project is allowing users to refactor properties in
VarSets or other document objects.  I've started thinking about how this should
happen and the concrete action I'm now working on is renaming as I announced in
[issue #16222](https://github.com/FreeCAD/FreeCAD/issues/16222).
