I have completed all sub-projects of the grant "Upgrade the CAM geometry kernel from Clipper 1 to Clipper 2"

### List major changes and respective pull requests

#### Sub-project 1: evaluate/select a replacement for clipper 1 

- Deliverable: evaluation of replacement libraries for Clipper 1
- Deliverable: the CAM team's buy-in for my selection of Clipper 2

Both of these were complete at the time of grant proposal submission, and included in the submission.

#### Sub-project 2: correct/non-heuristic arc fitting

- Deliverable: improved algorithm for arc fitting, replacing the current error-prone heuristic algorithm

The deliverable was fulfilled by FreeCAD/FreeCAD#30169, and a series of follow-up bug fixes.

#### Sub-project 3: replace our uses of Clipper 1 with Clipper 2 in the Adaptive operation

- Deliverable: the Adaptive code base makes library calls into Clipper 2, and not Clipper 1
- Optional/extension deliverable: rewrite adaptive's linking move generation algorithm to leverage new Clipper 2 features to improve linking move generation speed (which is a signficant contributor to run time on some models)

The deliverable was fulfilled by FreeCAD/FreeCAD#33739. The optional/extension deliverable is not complete; I will discuss this below in "project modifications".

#### Sub-project 4: replace all other uses of Clipper 1 in CAM with Clipper 2

- Deliverable: all CAM code outside of Adaptive makes library calls into Clipper 2, and not Clipper 1

The deliverable was fulfilled by FreeCAD/FreeCAD#29535.

#### Cumulative deliverables

- Delete Clipper 1 from our code base -- completed between sub-projects 3 and 4, with final removal in FreeCAD/FreeCAD#29535.
- Delete libarea (and inner kurve library) from our code base -- completed to the extent it made sense in sub-project 4 (FreeCAD/FreeCAD#29535); details below in "project modifications"


### Project modifications

1. Adaptive optional deliverable: when I submitted the grant proposal, I outlined an optional deliverable for migrating to clipper 2 in Adaptive to make a specific algorithmic improvement for faster linking move generation leveraging Clipper 2's triangulation features. I specified this as an optional but intended extension because I expected it to work but I was not certain it would. Since then, it has become apparent that Clipper 2's new triangulation features are buggy, and the maintainer said he regretted releasing them too soon. I think we will still make this algorithmic improvement eventually when these features stabilize, but they are not ready for use in FreeCAD yet. I am a little disappointed with this outcome, but fundamentally my uncertainty about clipper's new triangulation features were most of what made me designate this as an optional extension, so I am not entirely surprised by it.

2. Delete libarea and inner kurve library: when I wrote this deliverable I didn't have a fully complete understanding of all the ways each libarea feature was used in FreeCAD, and I should have written a little more slack into the description to reflect that. I did delete the kurve library, as well as many libarea functions, replacing them all with native use of Clipper 2. However, I have not actually deleted libarea. In part, this is a question of labeling: most of the code in FreeCAD's libarea directory is new code, written for FreeCAD, completely unrelated to the defunct upstream libarea library. Of the remainder, it did not seem productive to delete libarea's type definitions and replace them with new ones of our own. It also did not seem productive to delete a few helper methods that are (likely) original to libarea. I believe I have completed this deliverable in spirit, as it should have been written, removing our dependence on unmaintained libarea code for important and nuanced geometry functionality. But technically, the libarea directory and compilation unit still exist in our code base, as well as some original libarea code.


### Tell us what the challenges were (if any)

I significantly underestimated the difficulty and amount of work required in replacing our heuristic arc fitting process with a correct, non-heuristic algorithm (sub-project 2). I knew from the start that this was the most intricate and intellectually challenging part of my proposal, but I thought I had a full understanding of the challenges I would face, and that I had designed adequate solutions for them, prior to submitting my proposal. However, I encountered a number of difficulties I didn't expect:

- I ended up doing a rewrite of my initial implementation for edge tracking during offsets. The new implementation was fundamentally in-line with my original plan, but still a major change effectively amounting to a complete rewrite of a mostly-working implementation
- I encountered issues that I would describe as clipper bugs (I reported it upstream), in which clipper silently drops length-1 edges (in clipper units, so 1e-7 mm) in a way that broke my edge tracking system. It took a long time to track this down, and to figure out to what extent I could work around it and mitigate it with different and more robust processes for maintaining a connection between clipper's representation of arc edges and our external/native representation of those edges.
- I encountered and had to resolve many problems outside of clipper while making this change. I think I should have anticipated this while writing the grant application, but I did not:
  - We had code paths that explicitly discretized non-circular curves into line segments, and depended on heuristic arc fitting to get arcs back. I had to replace this with a new process leveraging our biarcs interpolation functions (which approximate curves with circular arcs), and then do several iterations of diagnosing and fixing bugs in that process, entirely separate from the new clipper code.
  - I did not have a full understanding of all of the places we our pre-existing code outside of clipper checked point-equality with a tolerance threshold, and these pre-existing checks led to bugs handling small arcs. Since the old, heuristic arc fitting algorithm didn't (ever? tend to?) produce such arcs, I had to diagnose and fix these issues as part of the new system for handling arcs in clipper.
  - I discovered pre-existing non-deterministic behavior in WireJoiner (pre-processing before clipper) and in BoundBox computation with/without the GUI, and had to diagnose and fix these issues to make it tractable to reliably reproduce clipper-related errors later in the process. Over all, the boundary between bugs related to the clipper upgrade and bugs elsewhere in the system was quite fuzzy, and led to appreciable scope creep while investigating bugs that surfaced after merging non-heuristic arc fitting.
 
 ### Tell us if you are ready to continue working on the project as agreed/Discuss future work

 The project is now complete, but I want to expand this section of the report to include related future work. When I discovered that the performance improvements to Adaptive I had hoped to implement as a part of this project weren't going to pan out, I did some preliminary investigation into other options for speeding up Adaptive. I am currently sitting on drafts for a number of modifications to Adaptive and to computation of cleared areas for rest machining that substantially decrease computation time in some/many models. While some of these improvements do leverage clipper 2 capabilities, I decided that they were too far divorced from the intent and description of this grant to prioritize them, and I set them aside temporarily. However, with the completion of this grant, I hope to follow up on them (possibly as part of a grant in the next quarter), and I think the clipper upgrade will help enable these and other performance improvements. I have less concrete plans for this, but I also intend to play with ideas for reimplementing our profile/deburr open offset functions with clipper 2 to help them produce reliably correct results.
