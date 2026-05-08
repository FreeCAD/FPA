## Summary of Activities - OCCT Liaison - April 2026

### Community work

- Contact with OCCT on possible boolean operation performance problems
- Relay feedback on Gordon surfaces in relation to curves workbench

### Investigate crashes

This month I wanted to focus on crashes and incorporate `Part::SignalException`
in various places.  I got down a rabbit hole because it didn't work for the
first PR that I tried, namely
[#23975](https://github.com/FreeCAD/FreeCAD/issues/23975) (I still had crashes
after using `Part::SignalException`).

Luckily I became aware of Hyarion's
[#28854](https://github.com/FreeCAD/FreeCAD/pull/28854) that I reviewed in
depth.  With the signal handler from this PR,
[#23975](https://github.com/FreeCAD/FreeCAD/issues/23975) does provide good
results and crashes are prevented.

A next step was to investigate if we can make this work in the same way as on
Windows.  It turned out that Windows has a different mechanism to catch
segfaults that has a different underlying architecture.  Investigating whether
we can reconcile the two mechanisms is something I can do, but is probably very
challenging, so I defer it for later because we now have mechanisms that work
on all three platforms.

With Hyarion's PR merged, my plan is to add signal handlers (potentially with
help from the community) for each of FreeCAD's reported crashes with the goal
to make FreeCAD more stable.
