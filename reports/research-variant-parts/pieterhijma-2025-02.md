## Summary of Activities - Research Variant Parts - February 2025

- Computing Shapes for Variants
- Improving the view provider
- Reporting

### Computing Shapes

This was the core of the project and has been completed in a satisfying way by
means of intercepting property access.  This makes sure that computing a shape
of a document object does not affect the document object itself by means of
setting up a stack of "contexts" as an alternative memory for computing shapes.

### Improving the view provider

This was mainly to have GUI support to be able to show the functionality in a
satisfying way.

### Reporting

The project has been reported in various ways:
- A forum topic in [Open Discussion](https://forum.freecad.org/viewtopic.php?t=91325)
- A forum topic in the [Developers corner](https://forum.freecad.org/viewtopic.php?t=91537)
- A [discord channel](https://discord.com/channels/870877411049357352/1298197289357021204)

Many videos have been created with explanation in general and in this month I
created [a video of a
propotype](https://forum.freecad.org/viewtopic.php?p=812021#p812021) and [one
with more advanced
configurations](https://forum.freecad.org/viewtopic.php?p=813545#p813545).

Finally, I created a presentation for the Sunday 2 March Developer meeting that
I report on in [this
post](https://forum.freecad.org/viewtopic.php?p=814501#p814501).

The prototype code has been submitted in three (stacked) PRs:

- [#18412 Core: Allow exposing properties](https://github.com/FreeCAD/FreeCAD/pull/18412)
- [#19733 Core: Compute shapes for variants](https://github.com/FreeCAD/FreeCAD/pull/19733)
- [#19735 Gui: Add Part variant logic](https://github.com/FreeCAD/FreeCAD/pull/19735)

Please note that although the proposal stated that I would submit multiple
alternatives for each phase, the alternatives were vastly less viable than
expected.  Hence, only one option was implemented for each phase, essentially
the only viable one.  The PRs are all draft and are only meant to show the
prototype.  If we ever want to build on these ideas, I would propose to build
on them and implement all corner cases as well.  In that case, the structure of
the PR will probably change, most likely splitting up the PRs into smaller
incremental steps.

### Concluding remarks

I consider this project now finished and all the reporting on this project has
been indexed in [this
post](https://forum.freecad.org/viewtopic.php?p=814501#p814501).  A next step
is to investigate to define a FreeCAD Enhancement Proposal for this work.
