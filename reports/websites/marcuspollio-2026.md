## Websites improvements initiative - Step 1

| Report Date | Report Author | Project Status |
| --- | --- | --- |
| June 2026 | marcuspollio | Completed |

This report is issued as part of the [Websites improvements initiative - Step 1](https://github.com/FreeCAD/FPA-grant-proposals/issues/40) FPA Grant.

**Website repository:** [FreeCAD/Website](https://github.com/FreeCAD/Website)

**Temporary deployment:** [freecad.github.io/Website](https://freecad.github.io/Website/)

### Summary

The grant proposal had two simultaneous objectives:

- Update some parts of the websites infrastructure with a unified structure, layout and code.
- Lay the foundations for improved guidelines, documentation, curation and maintenance effort of FreeCAD websites.

The first objective is the unification of the Homepage, News blog and Developers Handbook under one common roof. The general structure, setup, configuration, template code, default assets, and documentation of the website project are fully completed. Continued work from the community will now focus on the content, refinements, onboarding news contributors and the next steps.

The second objective is the setup of improved guidelines, documentation, curation and maintenance of the websites. The setup of a dedicated team structure and how curation and maintenance will be organized is still on-going and will continue during the next steps.

### Work done

As a reminder, part of the new unified website (general structure and some technical choices) had already been developed since mid-2024, before the FPA grant application. However, the work carried out over the last few months has allowed to clarify, flesh out, and fully implement the remaining major points.

As part of the FPA grant, the following tasks have been completed since end of May 2025 (FPA grant proposal submission):

- News blog articles migration and cleanup.
- News taxonomy improvements and better multi-language fallbacks.
- Community page with Calendar, latest event-related news articles, links to FPA and FreeCAD Professional Network.
- Documentation landing page with Developer Handbook cleaned up and section about website and Hugo theme.
- Telemetry page with basic metadata, currently two diagram options (donut and histogram).
- Thank you page after downloading.
- Footer with site map, social media and share on Fediverse form links.
- Addons list with basic metadata taken from Addons catalog.
- Donate page with donation form, list of sponsors and small FAQ section.
- Custom content shortcodes, useful when adding custom element to pages (e.g. block & group, tabs, git links, carousel, canvas & compare image, bundled video, Mastodon toot, PDF, etc.).
- GitHub action workflows to update data files used for building several parts of the website (Addons, Telemetry).
- Expose content and i18n theme strings to the CMS.
- Optimize site build and page loading times, specially by fine-tuning media sizes, largest contentful paint and resources loading (CSS, JS).
- Many small improvements all over the place (content, theme, style).
- Many refactors and cleanup all over the place (content, theme, style, CMS).
- Website project documentation.
- Dependencies updates, a few bugs or limitations reports to upstream (Hugo and Sveltia).

This represents more than 400 commits (mostly by marcuspollio, a dozen by action bot to update data files, a few by news article writers), some small (a few lines of code), some larger (thousands of lines and dozens of files).

### Next steps

Next are the involvement of the community for content, assets and translations, and testing of the website on diverse systems and devices to make sure as many bugs and annoyances are tackled before deployment. The delivery of the new unified website is planned for the next release (26.3).

This has been a pretty fun journey, much has been learned. There are still lots of neat ideas to explore, which is really appealing. Thanks to its open nature, the project will also evolve over time, which is exciting to witness.