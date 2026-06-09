## Summary of Activities - Improve C++ API Documentation - October 2025

I picked up on this project after finishing the Improve UX VarSet project.
Last progress on this project was halted on a [discussion on how to approach
the
documentation](https://github.com/FreeCAD/FreeCAD/pull/21494#issuecomment-2909471139).
The discussion happened on Discord and after reviewing this discussion again, I
came to the compromise in [this
comment](https://github.com/FreeCAD/FreeCAD/pull/21494#issuecomment-3397022581)
that was accepted.  This means that the [alternative
PR](https://github.com/FreeCAD/FreeCAD/pull/21708) is not regarded as the way
to go.

This PR is awaiting conflict resolution and since we are waiting for a
reformatting of the code, I decided to not update this PR.

Other work that was done in this project:
- Upgrade Doxygen to a new version
- Document `App::Document`
- Create a topic for Document
- Document `App::Application`
- Create a topic for Application
- Document `App::Link`
- Create a topic for Link
- Document `App::Expression`
- Create a topic for Expression
- Document the classes for element mapping (toponaming) (unfinished)

Since we are waiting for a big PR that reformats the C++ code and this is not
for 1.1, I haven't created PRs for this work yet.

With this effort, the project is nearing its end.  The things to do are:
- Finish documenting the classes for element mapping
- Create a topic for element mapping.
- Improve the formatting of the website
- Present the work at the developers meeting
- Create the PRs for this work
- Update the developer's guide



