## Activity Report 2

### Week 3

This week had a fair amount of research and pre-work, as we had some development dependencies that prevented moving PRs along.  It was also closer to a 4 day than a 7 day week due to travel.  The time wasn't wasted, as you can see from the following week's much faster clip.

* [#12247](https://github.com/FreeCAD/FreeCAD/pull/12247) Stop tests from leaving files around after execution *merged*
* [#12237](https://github.com/FreeCAD/FreeCAD/pull/12237) Transfer in makeElementRefine   *merged*
* [#12305](https://github.com/FreeCAD/FreeCAD/pull/12305) Toponaming/Part FeaturePartFuse   *opened*
* [#12295](https://github.com/FreeCAD/FreeCAD/pull/12295) Toponaming: transfer in FeaturePartBoolean  *merged

Overall, after completing two of the top level features, I switched to one very complicated top level feature - PartFeatures, which has a lot of dependencies.  The goal is to find any issues sooner rather than later.  Next week will be about getting all those dependencies in place.

### Week 4

As planned, dependencies were the name of the game, and many PRs were issued.  Part Features was eventually completed.  Some team support and a documentation update to [log of issues and discoveries](https://github.com/FreeCAD/DevelopersHandbook/issues/92) occured.

* [#12498](https://github.com/FreeCAD/FreeCAD/pull/12498) Toponaming/Part: Remove makeElementShape and cleanup opcode code  *merged*
* [#12484](https://github.com/FreeCAD/FreeCAD/pull/12484) Toponaming/Part part features transfer  *merged*
* [#12483](https://github.com/FreeCAD/FreeCAD/pull/12483) Toponaming/Part make element thick solid *merged*
* [#12482](https://github.com/FreeCAD/FreeCAD/pull/12482) Toponaming/Part: get sub topo shape  *merged*
* [#12460](https://github.com/FreeCAD/FreeCAD/pull/12460) Toponaming/Part: make element pipe shell  *merged*
* [#12435](https://github.com/FreeCAD/FreeCAD/pull/12435) Toponaming/Part: make element loft  *merged*
* [#12431](https://github.com/FreeCAD/FreeCAD/pull/12431) Toponaming/Part: make element ruled surface  *merged*
* [#12417](https://github.com/FreeCAD/FreeCAD/pull/12417) Toponaming/Part: transfer in linearize  *merged*
* [#12414](https://github.com/FreeCAD/FreeCAD/pull/12414) Toponaming/Part: Add searchSubShape as findSubShapesWithSharedVertex *merged*
* [#12405](https://github.com/FreeCAD/FreeCAD/pull/12405) Toponaming/Part: Transfer in MakeElementDraft  *merged*
* [#12366](https://github.com/FreeCAD/FreeCAD/pull/12366) Toponaming/Part: Move getSubTopoShape   *merged*

Next up is a review of all the tests written for clarity and coverage, and then a discussion with the team on the most effective place to focus while leaving room for other team members to work comfortably.

Overall, the prognosis after completing half the allocated time is good.  The big unknown is what the python level work will look like.
