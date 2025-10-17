## Websites improvements initiative - Step 1

| Report Date | Report Author | Project Status |
| --- | --- | --- |
| 1st October 2025 | marcuspollio | WIP (Alpha Phase mostly complete) |

This first report is issued as part of the [Websites improvements initiative - Step 1](https://github.com/FreeCAD/FPA-grant-proposals/issues/40) FPA Grant.

### Summary

The grant proposal had two simultaneous objectives:

- Update some parts of the websites infrastructure with a unified structure, layout and code.
- Lay the foundations for improved guidelines, documentation, curation and maintenance effort of FreeCAD websites.

The first objective is the unification of the Homepage, News blog and Developers Handbook under one common roof. While not fully complete, the work accomplished so far reached a fairly decent state. Work will continue in order to have a coherent, refreshed and maintainable website. Currently, most of the [_Alpha Phase_](https://github.com/marcuspollio/FreeCAD-website/milestone/1) deliverables have been completed. Some [_Beta Phase_](https://github.com/marcuspollio/FreeCAD-website/milestone/2) deliverables are quite advanced too (refactors, cleanups, documentation, some content). The schedule is roughly on track. The end of the _Beta phase_ may probably take a little longer than expected, depending on the content contributions.

The second objective is the setup of improved guidelines, documentation, curation and maintenance of the websites. Little work on this part has been accomplished yet, except for those matters strictly related to the first objective. We also note the difficulty in expanding the contributors base: despite the enthusiasm, the attendance at meetings is low, feedback is quite rare, and code contributions are even scarcer. This is to be expected given the nature and past experience in the project (varying availability, volunteer based, lack of established collaborative framework).

### Websites unification

As a reminder, part of the new unified website (general structure and some technical choices) had already been developed since mid-2024, before the FPA grant application. However, the work carried out over the last few months has allowed to clarify and flesh out the remaining major points. They will see continued improvements during the _Beta phase_ and beyond.

As part of the FPA grant, the following tasks have been completed since end of May 2025 (FPA grant proposal submission):

- News blog articles migration and cleanup. Most recent articles will need to be migrated too.
- News taxonomy improvements and better multi-language fallbacks.
- Community page with Calendar, latest event-related news articles, links to FPA, FreeCAD Professional Network.
- Documentation landing page.
- Contribute landing page.
- Developer Handbook cleaned up and moved to its own section. Most recent changes will need to be migrated too.
- Telemetry page with basic metadata, currently two diagram options (donut and histogram).
- Thank you page after downloading.
- Footer with site map, social media and share on Fediverse form links.
- Addons list with basic metadata.
- Donate page with donation form, list of latest funded FPA grant projects, list of sponsors and small FAQ section.
- A few custom content shortcodes, useful when adding custom element to pages (e.g. box & column, bundled video, Mastodon toot).
- 3 GitHub action workflow to update data files used for building several parts of the website (Addons, Telemetry, FPA grants).
- Expose some page params and i18n theme strings to the CMS.
- Optimize site build and page loading times, specially by fine-tuning media sizes, largest contentful paint and resources loading (CSS, JS).
- Many small improvements all over the place (content, theme, style).
- Many refactors all over the place (content, theme, style, CMS).
- A little bit of documentation here and there.
- Dependencies updates, a few bugs or limitations reports to upstream (Hugo and Sveltia).

This represents more than 200 commits (a dozen by action bot to update data files, others by marcuspollio), some small (a few lines of code), some larger (thousands of lines and dozens of files).

The following tasks have seen little or no improvements yet:

- Homepage content
- Authors credit (articles and image)

The first one needs a discussion and proper design with other contributors and FPA.

### Foundations for improved guidelines, documentation, curation and maintenance

As summed up above, this objective has seen little work. However, some meetings were set up, some intermittent discussions and even constructive albeit rare feedback happened.

There may be three inherent main factors at play in this regard: firstly, the FPA grant program is currently primarily intended for individuals, as there is little or no structure to support active group work. Secondly, the classic organization into successive brief, design, prototyping, procurement, implementation, testing and use phases, where various stakeholders have a decisive influence on particular phases or throughout the entire process, is almost non-existent in the development of FreeCAD. The recent formation of interest groups is a positive step but its application is still quite limited. Thirdly, the very nature of the project, which relies on the goodwill of contributors. Significant improvements in several areas are underway and appreciated, while acknowledging their limited scope and reach.

Regarding this project, establishing a common platform bringing together everyone involved in the website is a good step. Setting up regular discussions or meetings can help with coordination and ensure that everyone is up to date. Then, framing group projects while leaving room for initiative can help move forward.

### Next steps

The [_Beta phase_](https://github.com/marcuspollio/FreeCAD-website/milestone/2) will seen continued improvements, specially content and theme polishing, refactoring, cleanups and documentation. Some minor features will be introduced as needs arise. More testing, specially on diverse systems and devices, is needed to make sure as many bugs and annoyances are tackled before deployment. A special focus on the simplification and modularity of the code base will allow easier flexibility, scalability, maintenance and contributions. The delivery of a pleasant and solid website base for 2026 is the next major goal.

This has been a pretty fun journey, much has been learned, and much more still remains to be.