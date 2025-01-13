## Summary of Activities - Research Variant Parts - December 2024

The work in December focused on referring to parent properties in relation to
FreeCAD's recompute mechanism and dependencies between document objects.  I
also made a start into computing shapes for variants.

### Referring to parent properties

In [this post](https://forum.freecad.org/viewtopic.php?p=795527#p795527) and
following in the Developer's Corner I give a detailed account of how dependency
checking works in FreeCAD.

I tried to make the text accessible to non-developers as well because it can
help with designs.  I refer to that series of posts in [this
post](https://forum.freecad.org/viewtopic.php?p=795548#p795548) in the Open
Discussion section.

Instead of releasing a PR for this work, I refer to [my branch with debugging
code](https://github.com/pieterhijma/FreeCAD/tree/debug-dependencies) in the
Developer's Corner topic because the code is not meant to be merged.  I also
provide a test file so developers can verify my findings.

In the same forum topic, I discuss the problems with referring to parent
properties by means of hidden references.  In essence hidden references create
cycles but they have a separate dependency checking mechanism and since the two
dependency mechanism are unaware of each other, this form of cycles is allowed.
I refer to the code that contains the alternative separate dependency check
code.

I then argue that the fact that a reference to a parent object creates a cycle
is artificial because there is not much distinction in having it in for example
a VarSet.  The problems seem to come from the granularity of the dependency
graph.  [This post](https://forum.freecad.org/viewtopic.php?p=795717#p795717)
summarizes the findings.

I then propose a more find-grained dependency graph that allows properties to
be marked as "exposed" with which it is possible to refer to parent properties
without creating cycles.

Given this dependency graph formalism, I could create a proof-of-concept
implementation that follows these rules.  This is reported in [this Open
Discussion post](https://forum.freecad.org/viewtopic.php?p=796523#p796523) and
contains a video of the functionality.

The implementation is discussed [in this Developer's Corner
post](https://forum.freecad.org/viewtopic.php?p=796706#p796706) and lists two
implementation options with drawbacks and benefits listed for both of them.
[Draft PR #18412](https://github.com/FreeCAD/FreeCAD/pull/18412) contains the
proof-of-concept implementation.

One problem is that the community has to decide whether 1) we actually want
this functionality and 2) if so, which of the two implementations that we want.
This was discussed in the Developer's Meeting of [21 December
2024](https://github.com/FreeCAD/FreeCAD-developer-meetings/blob/main/Minutes/minutes-2024-12-21.md).
The current solution was discussed and how to decide on it.  For the latter
there was no clear solution, but the RFC process that was discussed in this
meeting as well seems like a good process.

### Computing Shapes for variants

I spent time on trying to compute a shape given geometry in a document object,
for example a Body or Part.  The idea is that for a variant, we compute a shape
allowing to set certain properties temporarily without making copies or using
hidden documents (something that copy-on-change subshapebinders currently do).

I am still investigating how to do this in the current code base without making
large, cross cutting changes.  I have not found a satisfying way and do not
have output for this as of yet.  My preliminary conclusion is that everything
in FreeCAD (properties, document objects) is heavily tied to the concept of a
document in a way that is actually described in the
[forum](https://forum.freecad.org/viewtopic.php?t=91584&hilit=worser).  The
fact that the copy-on-change link mechanism relies on hidden temporary
documents and copies is a logical consequence of this.


