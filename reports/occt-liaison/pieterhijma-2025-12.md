## Summary of Activities - OCCT Liaison - December 2025

### Update the project

The [OCCT Liaison
project](https://github.com/orgs/FreeCAD/projects/32/views/1?layout=table) has
received updates on issues.

### Investigate [Issue #24115](https://github.com/FreeCAD/FreeCAD/issues/24115)

This is an issue from freckletonj trying to compute toolpaths with section.
Last month I offered help to freckletonj to compile OCCT and FreeCAD to
investigate further.  Unfortunately there has been no progress on this further.
I will ping once more.

### Investigate [Issue #25821](https://github.com/FreeCAD/FreeCAD/issues/25821)

This was a peculiar issue.  There was already a minimal version and I found out
that it was a seam issue.  A DRAW script showed that OCCT was likely not the
issue but FreeCAD itself.  Later I could confirm that it was definetely not
OCCT.

### Checking out KiCad issues

Seth Hilbrand listed some of the issues they have, mostly with STEP files and
face/solid/group colors.  It turns out that KiCad has already an effective way
to report their issues to KiCad and I could confirm for Seth that one of their
issues had already been solved.

It would be interesting to see if we have similar problems as KiCad has, but it
looks like FreeCAD has workarounds in place.

### Investigate [Issue #11654](https://github.com/FreeCAD/FreeCAD/issues/11654)

This issue led to 5 submitted OCC issues, two of them crashes, three others
with faulty shapes.  The crashes have been fixed, but when checking them, they
also resulted in faulty shapes.  I now understand that OCCT considers crashes
and quality as separate issues, so I submitted follow up issues that reveal the
quality problems.

### Investigate other issues

- [#23975](https://github.com/FreeCAD/FreeCAD/issues/23975): true OCCT issue and needs more attention
- [#25134](https://github.com/FreeCAD/FreeCAD/issues/25134): needs more analysis in OCCT
- [#25955](https://github.com/FreeCAD/FreeCAD/issues/25955): is likely an assembly solver issue


### Discusson on OCCT priorities

I wanted to bring up a question on priorities, whether we should focus on
submitting as much as possible to OCCT or if I should also pay attention to
provide work arounds to prevent crashes.

The general consensus was that I should try to estimate how prevalent a crash
is and if that is high, we should try to add a workaround.  In the mean time
submitting bugs is also important.

So, I will try to go over the list of issues with crashes and assign some value
on how common such an issue is.

