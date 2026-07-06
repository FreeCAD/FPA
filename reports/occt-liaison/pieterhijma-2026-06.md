## Summary of Activities - OCCT Liaison - June 2026

### Adapt FreeCAD to -Werror and OCCT 8

This month, part of the effort went into making the OCCT 8 release play well
with `-Werror`, something that pixi now requires for the release builds, see
[#30940 (open)](https://github.com/FreeCAD/FreeCAD/pull/30940).  This work has been
done in communication with the Code Quality Working Group and several different
approaches have been tried.

### Find a solution for an OCCT 8 regression

Issue [#31067](https://github.com/FreeCAD/FreeCAD/pull/31067) reported a
regression on OCCT 8.  I've investigated in direct collaboration with OCCT and
I created a PR with a workaround suggested by OCCT: [#31067
(open)](https://github.com/FreeCAD/FreeCAD/pull/31067).  It is still under
discussion.
