# <img src="../images/freecad.svg" style="width:24px;" /> FreeCAD documentation migration

**Purpose**: Migrate the FreeCAD documentation from MediaWiki to a Git-managed markdown-based structure

**Contact**: [Yorik](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=68)

### Short term contract for Python / web programming and documentation management

The [FreeCAD Project Association](https://fpa.freecad.org) is seeking a developer to switch the [FreeCAD documentation](https://wiki.freecad.org), currently managed by a MediaWiki instance hosted on the FreeCAD website to a file-based, versioned system, preferably based on Git and markdown. 

Candidates should: 

1. have a good knowledge of the markdown format, including how to work with yaml data

2. be able to write scripts, preferably in Python, to automate some aspects of the migration or maintaining

3. be able and ready to explore and work with the API of online platforms such as MediaWiki, GitHub or Crowdin

Candidates are also expected to conform to the following open-source development standards:

1. Work with the community. Do not do a lot of work without publishing, ask for community feedback
2. Document everything you do. Allow others to develop on top of your work
3. Build on preexisting work whenever possible
4. Communicate often. Discuss your ideas before implementing them

For final acceptance, the following quality metrics must be met:

1. All the contents of the current wiki must have been migrated and cleaned
2. The new documentation should display satisfyingly in both a web browser and inside FreeCAD
3. A way to download the documentation for offline use must be provided
4. A translation solution must be in place or at least agreed upon
5. All the items mentioned in the workflow below should be studied and, in principle, addressed. Documentation is in place to allow others to work further on the migration, if not all points of the proposed workflow have been completed

The candidate will work closely together with the FPA members and the maintainers of FreeCAD's documentation. They will guide the on-boarding and mentoring process, and will work with the candidate to ensure their work meets all of the above criteria.  

### Duration and Schedule

The project is scoped to fit a 6-week full time schedule. Milestones for each week are available, and the progress will be evaluated by the developer and the mentor(s) in (at least) weekly discussion sessions. The schedule may be shifted in order to accommodate part-time candidates.  

Work on the project will start when agreed between the developer and the FPA and a commitment of at least 20 hours / week is expected. 

### Compensation

The total compensation for this project is USD 5000, paid in two payments of USD 2500:

- The first payment after all the contents of the current documentation, including translations, has been migrated and cleaned
- The second payment after the conclusion of the quality metrics explained above

### Why?

* The mediawiki software is a dinosaur to maintain, and complicated to maintain up-to-date
* The mediawiki data is hard to back up. We are constantly at risk of loosing data
* The mediawiki search feature is notoriously weak
* The mediawiki is complicated to theme and make look good
* Our doc has become as important as FreeCAD itself. It would benefit from having the same level of decentralisation
* The current translation system is always at risk of becoming obsoleted, like many mediawiki plugins. It is not used anymore by the MediaWiki project
* A simpler, file-based system would allow much more automation, scripting and integrations. Python/C++ API documentation can be built on-the-fly and integrated
* A Git-based system would allow branching/tagging/versions of the documentation corresponding to FreeCAD versions and maintaining a more up-to-date documentation
* A markdown-based system would allow to produce many kinds of outputs such as online/HTML like the current wiki, but also better integrate into the FreeCAD Help system, or produce e-book formats or even printed books
* A markdown + Git based system would be easy to integrate into online translation platforms, and therefore free us from one more part of maintainance and unify with other translation systems of FreeCAD

### What's there to test already

An automatic translation of the mediawiki content to markdown is already available on https://github.com/FreeCAD/FreeCAD-documentation . It is done automatically by the help of a python script at https://github.com/FreeCAD/FreeCAD-documentation/blob/main/migrate.py . The translated documentation can be read online, by browsing through the markdown pages, or from within FreeCAD's Help system. Both the [Help addon](https://github.com/FreeCAD/FreeCAD-Help) and the [markdown documentation](https://github.com/FreeCAD/FreeCAD-documentation) form the core of what we want to develop.

The goal of this project is to migrate for good to the markdown version, retire the migrate script, and shut down the wiki.

### Proposed workflow

* Write article explaining the migration to the community: why, what are the advantages, what are the issues
* Write a migration plan or adapt this one
* Define a directory / category structure that reflects the current documentation categories
* Define a tags / yaml system to allow further and finer classification of documentation pages
* Define a language switching system that allows user to use the documentation in their language
* Define a search system
* Define a sequence system so some pages can be assembled like a book
* Design an online HTML-based output
* Design a FreeCAD online output
* Design a FreeCAD offline output
* Design a multi-formats e-book output
* Design a printed book output
* Research and help choose a translation platform, investigate available plans (see below)
* Define what contributors should do while the wiki is in read-only mode
* Set the wiki in read-only mode
* Transfer all the contents from wiki to markdown files
* Verify that all the contents have been transferred
* Manually check each and fix each and every page for style errors
* Verify all the links
* Create a structure for translations and relocate all pages
* Setup the translation platform
* Tie the translation platform into the git repo
* Document the steps needed to setup the translation platform
* Document the process to adopt for translators
* Document the process to adopt for maintainers
* Define how dynamic contents such as FreeCAD API documentation can be extracted and added automatically to the documentation
* Write an article announcing the change
* Design a system to handle and redirect wiki.freecad.org links
* Remove the mediawiki installation

### Possible translation platforms, to be checked again

* Research which translation platform to use (transifex, crowdin?) based on:
  * are they free for FOSS projects, or what are the costs
  * how good they handle markdown files
  * how already translated pages can be fed back into the translation platform
  * automatic integration with github
* **Crowdin** - https://crowdin.com
  * Free for FOSS projects
  * **Incomplete** markdown support (looses images) (12/2020)
  * Allows to upload a translated file as translation
  * Integration with github
  * Advantage: FreeCAD users know it
* **Transifex** - https://transifex.com
  * Free for FOSS projects
  * **Incomplete** markdown support (looses images) (12/2020)
  * Allows to upload a translated page (git push)
  * Integration with github
* **Weblate** - https://weblate.org
  * Free for FOSS projects
  * No markdown support (12/2020)
