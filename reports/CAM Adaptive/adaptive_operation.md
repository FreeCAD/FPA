I have completed all sub-projects of the grant "CAM improvements for the Adaptive operation"

### List major changes and respective pull requests

#### Sub-project 1: Improvements to enable successful generation at small stepovers

- Deliverable: code change to enable generation at small stepovers FreeCAD/FreeCAD#24044
- Deliverable: example model that didn't work before, but does work with the change (attached to PR)

#### Sub-project 2: Improved automatic diameter selection for helix entry

- Deliverable: code change to enable successful entrances where a smaller entrance helix is required FreeCAD/FreeCAD#23980
- Deliverable: example model that didn't work before, but does work with the change (attached to PR)

#### Sub-project 3: Add "rest machining" support for adaptive toolpaths

- Deliverable: a "Use Rest Machining" chekcbox in the adaptive UI panel
- Deliverable: a code change to avoid re-cutting regions that are already cut
- Deliverable: a code change to allow adaptive paths to plunge in cleared space to begin cutting in a region, instead of entering with  a helix or from the edge of the stock

 All 3 deliverables are provided by FreeCAD/FreeCAD#27908


 ### Tell us what the challenges were (if any).

 Sub-projects 1 and 2 were delayed in review while the CAM team was busy exclusively examining PRs for the 1.1 release, and not reviewing work for 1.2. I postponed working on the last sub-project to avoid having too many open Adaptive PRs at once.

 I ended up rewriting the Adaptive operation significantly more than I expected to in this grant. I was aware while writing the proposal that I had some uncertainty about the magnitude of the change required to support rest machining, and I expected it to go notably beyond simply initializing the ClearedArea data structure with the appropriate region. But I thought the ultimate solution would involve careful reading of the code and a collection of subtle changes to add support for a non-empty initial ClearedArea; I did not anticipate doing a full rewrite of the algorithms for region pre-processing and selecting (re-)engagement points, and also modifying the code for lead-in and lead-out paths and adding a new system for ensuring reliable climb cutting. Between sub-projects 1 and 3, I ended up rewriting nearly every major component of the core Adaptive algorithm.


 ### Tell us if you think the rest of the project should be reorganized based on what you’ve learned, and why.
 ### Tell us if you are ready to continue working on the project as agreed.

 The project is complete now. I have also submitted a [PR](https://github.com/FreeCAD/FreeCAD/pull/29033) to close the corresponding epic in the CAM Roadmap.
