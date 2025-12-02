## Summary of Activities - VarSet User Experience - September 2025

This project is almost finished.  The only implementation work necessary is
copying properties to other objects.

### Moving properties

The following PR for moving properties was used as a base to discuss various
issues, most notably with `theo-vt`.  This PR has been closed in favor of a new
PR that has a satisfying solution, although I have some reservations because it
pushes the transaction system to the limit.  I brought this PR to the attention
of the CQWG.

- [#22960 (closed)](https://github.com/FreeCAD/FreeCAD/pull/22960)
- [#23841 (submitted)](https://github.com/FreeCAD/FreeCAD/pull/23841)


### Presenting the project at the developer's meeting on 20 September

[This project](https://github.com/orgs/FreeCAD/projects/30) is almost complete,
with most issues done and merged and all but one a submitted PR.  The last one,
copying properties, depends on a discussion with the CQWG that is planning on
reviewing my solution on moving properties.  In the meeting, I tried to explain
the different considerations for the implementation.  Although the
implementation finds the limits of the transaction system, there was not strong
resistence against the current path and merging it in the dev release after the
1.1 release.

Based on this, I conclude that it is worth to work on the last PR, copying
properties, while understanding that a review of the "move property" PR may
render the copying properties PR unnecessary.

### Reconcile Add Property dialogs

Remove the old Add Property dialog in favor of the one that is used for
VarSets.

- [#23426 (merged)](https://github.com/FreeCAD/FreeCAD/pull/23426)


### Allow editing of a property tooltip in the Property View

This PR has been merged.

- [#23510 (merged)](https://github.com/FreeCAD/FreeCAD/pull/23510)

### Expanding and collapsing properties in the Property View

This PR has been merged after DWG discussion and approval.

- [#23535 (merged)](https://github.com/FreeCAD/FreeCAD/pull/23535)

### Add a binding for property removal

This PR adds a binding to remove properties and takes into account Mac users as well.

- [#23552 (merged)](https://github.com/FreeCAD/FreeCAD/pull/23552)

### Various fixes for properties and the expression dialog

These PRs solve several small issues with the Property View and the expression dialog.

- [#23631 (merged)](https://github.com/FreeCAD/FreeCAD/pull/23631)
- [#23648 (merged)](https://github.com/FreeCAD/FreeCAD/pull/23648)
- [#23650 (merged)](https://github.com/FreeCAD/FreeCAD/pull/23650)
- [#23991 (merged)](https://github.com/FreeCAD/FreeCAD/pull/23991)


### Reporting where properties are being used

This PR allows users to obtain a report where properties are used (referred to)
in their designs.

- [#23989 (submitted)](https://github.com/FreeCAD/FreeCAD/pull/23989)
