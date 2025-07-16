## Summary of Activities - VarSet User Experience - June 2025

### Renaming properties

This month focused on renaming properties.  I've created a PR for transactions
and a PR for GUI support:

- [#21975 (merged)](https://github.com/FreeCAD/FreeCAD/pull/21975)
- [#21976 (draft)](https://github.com/FreeCAD/FreeCAD/pull/21976)

The latter one can now be taken out of draft.  There is a small issue remaining
where the GUI is not updated soon enough.  I think Kacper may know what the
problem is.

### Equations in the VarSet dialog

I've been looking into
[#19716](https://github.com/FreeCAD/FreeCAD/issues/19716) that addresses the
fact that equations are not possible in the VarSet dialog.  I'm looking into
this, but it is challenging because to create an equation, there needs to be a
valid Property with a name and type.  This means I can't postpone creating a
property until the very end, something that makes the dialog much more simple.
