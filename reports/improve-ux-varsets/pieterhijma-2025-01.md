## Summary of Activities - Improve User Experience VarSets - January 2025

I've started the Improve User Experience VarSets project this month.  So far,
I've not done any development yet, but I started two discussions on the forum:
- [Open discussion, Renaming properties](https://forum.freecad.org/viewtopic.php?t=93705), and
- [Open discussion, Add Property Dialog: Group Prefix](https://forum.freecad.org/viewtopic.php?t=93844).

The renaming properties discussion has been fruitful so far.  The community is
leaning towards my recommendation in [this
post](https://forum.freecad.org/viewtopic.php?p=802600#p802600).  When I start
implementing this feature, I will take [Kadet's comment on
aliasing](https://forum.freecad.org/viewtopic.php?p=803142#p803142) in
consideration, which means that I will investigate how difficult it is and if
it's easy, then I will implement it.  I commented on [this
PR](https://github.com/FreeCAD/FreeCAD/pull/16990) to keep it on hold after I
have researched the alias possibility.

Regarding the group prefix, the community is leaning towards removing the group
prefix from the dialog or hide it behind a setting.  I found an especially
confusing example in [this
post](https://forum.freecad.org/viewtopic.php?p=803899#p803899).  There are
some suggestions for group postfix, but that would be breaking changes, which
should follow a different route.

Not related to the development path of this project, but related to the user
experience of VarSets is the [forum topic "Multiple data managers,
really!"](https://forum.freecad.org/viewtopic.php?t=93616) that was first
called "VarSets, really!".  I completely understand the frustration with the
VarSet user experience, but I felt a need to defend and explain how we ended up
in this situation.

I believe in this topic we were able to find a mutual understanding of how this
came to be.  I summarized it in [this
post](https://forum.freecad.org/viewtopic.php?p=803139#p803139) and there seems
to be no strong objections against the conclusion.
