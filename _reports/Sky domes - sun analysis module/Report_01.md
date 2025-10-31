# Sky domes, sun radiations analysis module

FPA Grant to Francisco Rosa

## Report 1, 2025/10/31

This first report on the development of sun radiations analysis by sky domes in FreeCAD addresses three subjects: procedures acquired, results and next steps.

Continuing the work of the Solar Workench, which focuses on applying the resources available in the Python ladybug library, we have completed this first part dedicated to developing an application of colored sky domes as diagrams for recording and analyzing solar radiation from a specific geographic location over a given period of time.

## 1. Procedures acquired

The work procedures consisted of the following steps:

Understanding the ladybug code resources for producing solar analysis domes, such as the modules: *ladybug.wea, ladybug.analysisperiod, ladybug_radiance.skymatrix*, and *ladybug_radiance.visualize.skydome*, in addition to those previously used (*ladybug.location* and *ladybug.sunpath*).

To obtain irradiance values, an additional library, *ladybug-radiance*, was necessary, as well as the installation of the *Radiance* application, as instructed in the README.md.

The code for the sky domes was planned to consist of three documents with two modules and an .ui file for the future configuration window.

The first of these, containing the dome classes and the main set of functions, was finalized in this stage: the Skydomes.py module.

The second module will work in conjunction with the .ui file of the sky domes configuration dialog window, similar to the SunDialog.py and SunSetup.ui pair.

First, we experimented with using an expanded version of SunSetup.ui to control the celestial domes, but we noticed that there were more differences than similarities in their properties, so this hypothesis was abandoned.

We also evaluated the option of constructing the domes using meshes, as the ladybug library suggests. However, its handling and final results in FreeCAD proved to be more limited and complicated than using solid objects, which can be freely modified, saved, and exported.

## 2. Results

Sky domes are objects that can be configured and modified extensively and completely through the future dialog window in FreeCAD. Now, the main data they offer are:

Diagrams of solar radiation at a location over a given period, distributed as total, direct, and diffuse values ​​in kWh/m².

Diagrams of solar irradiance at a location over a given period, distributed as total, direct, and diffuse values ​​in W/m².

Furthermore, the domes can be presented in two models: Tregenza with 144 parts, and Reinhart with 576 parts.

We remind that the data from the sky domes will be fundamental for the development of future modules analyzing solar irradiance on objects in their contexts, even though they are not part of this grant.

The Workbench with these works can be downloaded at: https://github.com/Francisco-Rosa/Solar/tree/updates

## 3. Next steps

Our next steps will involve developing the code for the configuration module of the sky domes' properties and its dialog box, as well as making the necessary adjustments for proper and integrated operation on the workbench.

We will also conduct usability tests and make the necessary corrections.
