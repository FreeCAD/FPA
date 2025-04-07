## Summary of Activities - OCCT Liaison - March 2025

First of all, thank you very much to all of the community for offering me this
position.  In this and subsequent files, I will report the progress in my role
as OCCT Liaison.  This month was primarily focused on setting myself up.

### Contact with Dmitrii: Data Exchange

Yorik introduced me to Dmitrii Pasukhin from OCCT based on [the forum topic on
Data Exchange (DE)](https://forum.freecad.org/viewtopic.php?t=95294).  I tried
to get an understanding of Dmitrii's offer and studied a [DE wrapper
sample](https://github.com/dpasukhi/DE_Wrapper-Sample) from Dmitrii to
understand the technology and how it could integrate.

My understanding is currently:

FreeCAD remains as open as it is.  There can be a commercial (though possibly
still open source) addon that may load proprietary libraries for data exchange.
The addon will "stream" the resulting files to FreeCAD which means that the
interface with FreeCAD is minimal and most likely already exists.

The addon is only for users who want to pay for importing and exporting
advanced file formats, while FreeCAD remains as it is.

This will need follow up in the next month.

### Sorting through issues

A large task was to find a way to organize all the OCCT-related issues.  Max
and luzpaz have already prepared this to a high degree with the OCCT label.  I
created a [GitHub project](https://github.com/orgs/FreeCAD/projects/32/views/1)
where I and others can track the OCCT-related issues.  Max and I have now an
understanding of how to notify me of new OCCT issues.

A next task is to study a DRAW harness created by Brad McClean.

### Building FreeCAD

An important step is to set up FreeCAD such that I can easily switch between
various versions of OCCT and can debug OCCT.

### Setting up a channel on Discord

I created a channel on Discord to discuss OCCT-related topics and for people to
find me there.  The first discussion is the next section.

### Discussion on OCCT bug reporting and versions

I noticed that various OCCT issues reported use different OCCT versions.  In
some cases, the issue does not appear in newer OCCT versions.  This makes it
hard to decide what to do with these issues.

On top of that, FreeCAD maintains its own version with Blobfish patches on it.
All this has been discussed with Oursland and Blobfish himself weighed in as
well, stating that we should not use his patches for FreeCAD.

We agreed that we try to officially support only one version of OCCT and bug
reports on OCCT should use this version.  Currently, there is a dependency
problem preventing us to switch to 7.9.0 as of yet.

This will need follow up in the next month.

### Present myself in the DEV meeting

On Saturday 15 March I presented myself as the OCCT Liaison.  Since the minutes
are a bit sparse, I will write a summary here:

#### About myself

- I'm honored to have gotten this position.  I try to be very approachable by
  the community and I hope to be able to be a bridge between OCCT and FreeCAD.
- I hope that the interaction between OCCT and FreeCAD both help FreeCAD and OCCT.
- I'm highly motivated to improve FreeCAD and since various issues rely on
  OCCT, I'm motivated to improve OCCT as well.  I want to improve FreeCAD
  because I believe that technology to design things should be widely
  available.

#### OCCT Versions

We discussed the OCCT version for FreeCAD and the API stability that OCCT 8
will present.  We touched on the Blobfish patches.  An valid issue is that if
FreeCAD officially supports 7.9.0, then the Ubuntu version is likely outdated.
We don't have a very good solution for that, FreeCAD will may simply have more
issues than the official version.

#### STEP AP242 ed1/2/3/4 support

This is an issue from Max and he discussed it mostly.  Having these file
formats most likely means that we need support in the Assembly workbench and
improved GD&T support in FreeCAD.  The biggest problem is that we need
developers that want to work on this.

##### GitHub Project

I presented my project and the fillet/chamfer problems are of course well-known
and perhaps most pressing.  Chris mentioned that having this fixed by the OCCT
team by hiring them is incredibly expensive, too expensive for the FPA
currently.

#### Plan

My plans are roughly for the coming year:

- Improve the project
- Study the forum for understanding earlier attempts to organize OCCT-related
  issues
- Study existing DRAW tests
- Become an OCCT developer
- Discuss how to test bugs
- Talk to other OCCT users
- Talk to OCCT

### Set myself up for a high number of GitHub notifications

I noticed that I can't keep up with all the GitHub notifications that I
receive, so I worked on improving processing the GitHub notifications.  I
believe I have a process that more or less works now.

### Suggest a process for a 10 year roadmap

In the FPA meeting there was a discussion on corporate sponsors.  Brad made the
point that if we want to acquire sponsoring it has to be worth something for
the corporate sponsors.  I believe it would be beneficial to be able to offer a
realistic outlook, for example for a period of 10 years, to ensure that the
corporate sponsors know what they are sponsoring.  This can also make
priorities clear for the FPA and where funding should be directed to.

As a concrete example, I consider OCCT a close partner, so they may become a
sponsor of FreeCAD.  This could not only be money, but they could also decide
to invest in fixing fillets or for example supporting STEP AP242 ed1/2/3/4.
Dmitrii has already shown interest in the latter topic, but I noticed that
FreeCAD needs support for this as well.  This means that if we find the route
towards STEP AP242 important, then FreeCAD should also invest in support for
this.  Otherwise, the efforts of OCCT towards this direction cannot "land" in
FreeCAD.  Having a roadmap as an outlook to the future can show commitment from
the FreeCAD community and can help with convincing partners such as OCCT to
invest in this.

I have discussed this with Brad and one of the plans is to hold a developers
meeting with this as topic.  My next step is to reach out to some people in the
community to discuss the plan.

### Check forum on OCCT issues

I read through all the forum posts on OCCT.  The forum makes it very hard to
get an overview, at least for me, but some community members were keeping very
well track of the issues.  I opted for a GitHub project that gives all kinds of
ways to present the issues.

As a follow up, I want to participate on the forum.

### Register as OCCT developer

I registered myself as an OCCT developer by signing their CLA.
