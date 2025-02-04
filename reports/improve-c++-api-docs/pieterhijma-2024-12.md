## Summary of Activities - Improve C++ API Documentation - December 2024

The work in December is still starting up the project.

I started a [forum topic](https://forum.freecad.org/viewtopic.php?t=92919) in
which many opinions were expressed.  I'm processing these comments and
investigating in the code to what extent I can support the various opinions.

This amounts to:
- Trying to provide more general documentation on subsystems.
- Preventing the situation that we don't have resources to maintain the documentation.
- Is it a better idea to refactor instead of document?
- Can we create a way to declutter the code with comments?

Based on this, I'm experimenting with an improved index page in order to find a
way to provide more general documentation on subsystems.

This topic was also discussed at the [Saturday 21 December 2024 Developer's Meeting](https://github.com/FreeCAD/FreeCAD-developer-meetings/blob/main/Minutes/minutes-2024-12-21.md#c-and-python-api-documentation-discussion).

In this meeting concerns were raised about resources to maintain the
documentation, more preference for overview documentation, API documentation is
very useful in the Python Console.  Another viewpoint not raised on the forum
was that comments may help unexperienced or non-professional programmers.  In
the end we want the code to be accessible to the whole community and
documentation can help with that.

Overall my conclusion is that it makes sense to add documentation to the App
package as I intended in the FPA grant proposal, while taking all these
concerns into account.  I'll do my best to include "overview documentation" as
well.
