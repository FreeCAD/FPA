## Summary of Activities - Research Variant Parts - January 2025

The work in January focused on computing shapes for variants.  In December I
made a beginning but not in a satisfying way, meaning that I didn't see a way
forward without making cross-cutting changes throughout FreeCAD.  After the
holidays I picked up this project again after giving it some rest to think
things through.

I experimented again with making VarSets an integral abstraction and while
doing that, I realized a different route that had more potential and is
actually very close to how I explain variants to others, namely by means of the
analogy of calling functions in programming languages.

Calling a function allows one to inject values as parameters and these
parameters are read to compute a result.  To accomplish this, you need to set
up a data structure as a form of temporary memory and typically in programming
languages this is a stack to support recursion.

In FreeCAD document objects, the state of a document object is captured in
properties, so if I can set up a data structure as a form of temporary memory
for properties to execute document objects, I can potentially accomplish the
same.  Interestingly, I would have to do this with a stack as well because
variants can contain variants.

Most of the development effort went into setting up the above logic.  It was
working well for a simple cube and I showed this to Yorik at the first day of
the FreeCAD hackathon.  During the rest of the hackathon I tried to make it
work for more complex geometry as well, a body with a simple sketch.  My goal
was to make this example work and present it at the FreeCAD day.
Unfortunately, making this work was quite challenging because finding the
correct property setters and getters was challenging.  At the FreeCAD day I was
a bit disillusioned because my code was becoming more and more complex up to
the point that it is almost as complex as copy-on-change links.

At the FreeCAD day, my goal was to present the simple Cube version to the
audience, but unfortunately there was not enough time.  However, more
importantly, with the limited time I had, I ran a simple poll on the audience
asking who of the about 30 people both developers and users ever used
copy-on-change links.  My questions were:
- Who has ever used copy-on-change links?
- Who has ever used tracking copy-on-change links?
- Who has ever used copy-on-change links in combination with subshape binders?

In this audience that could definitely be called FreeCAD enthusiasts, only one
person responded to these three questions, all with the answer, I tried but
failed to make it work.  I'm actually amazed that not more people lack this
functionality and to me it means that we should really find a good alternative.

By the way, this was also highlighted in a session I had with Pierre (paddle):
we spent half an hour trying to make copy-on-change links work for Pierre's
designs and although we ended up making it work, it seemed far too complicated
to be used in practice.

Unfortunately, I couldn't conclude the experiments on computing shapes, but I'm
very close to report on it now.



