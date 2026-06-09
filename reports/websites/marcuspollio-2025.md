## Websites improvements initiative - Step 1

| Report Date | Report Author | Project Status |
| --- | --- | --- |
| December 2025 | marcuspollio | WIP |

This report is issued as part of the [Websites improvements initiative - Step 1](https://github.com/FreeCAD/FPA-grant-proposals/issues/40) FPA Grant.

### Summary

The grant proposal had two simultaneous objectives:

- Update some parts of the websites infrastructure with a unified structure, layout and code.
- Lay the foundations for improved guidelines, documentation, curation and maintenance effort of FreeCAD websites.

The first objective is the unification of the Homepage, News blog and Developers Handbook under one common roof. While not fully complete, the work accomplished so far reached a fairly decent state. Work will continue in order to have a coherent, refreshed and maintainable website. Currently, most of the [_Alpha Phase_](https://github.com/marcuspollio/FreeCAD-website/milestone/1) and [_Beta Phase_](https://github.com/marcuspollio/FreeCAD-website/milestone/2) deliverables have been completed. After the _Beta phase_ end, focus will be on content, onboarding contributors and the next steps.

The second objective is the setup of improved guidelines, documentation, curation and maintenance of the websites. Little work on this part has been accomplished yet. At the end of _Beta phase_, the new unified website will be properly documented, content and contributions guidelines established. The setup of a dedicated team structure and how curation and maintenance will be organized is probably deferred to the next steps of the project.

### Work done

As a reminder, part of the new unified website (general structure and some technical choices) had already been developed since mid-2024, before the FPA grant application. However, the work carried out over the last few months has allowed to clarify and flesh out the remaining major points. They will see continued improvements after this very grant period.

As part of the FPA grant, the following tasks have been completed since end of May 2025 (FPA grant proposal submission):

- News blog articles migration and cleanup.
- News taxonomy improvements and better multi-language fallbacks.
- Community page with Calendar, latest event-related news articles, links to FPA and FreeCAD Professional Network.
- Documentation landing page with Developer Handbook cleaned up and section about website and Hugo theme.
- Telemetry page with basic metadata, currently two diagram options (donut and histogram).
- Thank you page after downloading.
- Footer with site map, social media and share on Fediverse form links.
- Addons list with basic metadata taken from Addons catalog.
- Donate page with donation form, list of latest funded FPA grant projects, list of sponsors and small FAQ section.
- A few custom content shortcodes, useful when adding custom element to pages (e.g. box & column, tabs, git merge, carousel & compare image, bundled video, Mastodon toot, PDF, etc.).
- GitHub action workflows to update data files used for building several parts of the website (Addons, Telemetry, FPA grants).
- Expose some page params and i18n theme strings to the CMS.
- Optimize site build and page loading times, specially by fine-tuning media sizes, largest contentful paint and resources loading (CSS, JS).
- Many small improvements all over the place (content, theme, style).
- Many refactors and cleanup all over the place (content, theme, style, CMS).
- A little bit of documentation here and there.
- Dependencies updates, a few bugs or limitations reports to upstream (Hugo and Sveltia).

This represents more than 300 commits (a dozen by action bot to update data files, others by marcuspollio), some small (a few lines of code), some larger (thousands of lines and dozens of files).

### Next steps

After the end of the [_Beta phase_](https://github.com/marcuspollio/FreeCAD-website/milestone/2) focus will be on testing the website on diverse systems and devices to make sure as many bugs and annoyances are tackled before deployment. The involvement of other contributors for content, assets and translations will be put in place. The delivery of a pleasant and solid website base for 2026 is the next major goal.

This has been a pretty fun journey, much has been learned. There are still lots of neat ideas to explore, which is really appealing. Thanks to its open nature, the project will also evolve over time, which is exciting to witness.