# Summary of Google Summer of Code with pvlib
```{post} 2021-08-22
:author: Adam R. Jensen
:tags: pvlib, solar, open science, gsoc
```

The coding period of this year's Google Summer of Code (GSoC) is officially over, and it's time to take a step back and evaluate the experience. For those of you who might not know, I've been working on extending pvlib's iotools for the past 10 weeks, which I described in this [blog post](gsoc_project_intro/).

## Success or not?
There are many ways to determine if a project has been a success; one way is to look if the project goals have been met. So let's refer back to the project outline:

```{admonition} Original project outline
During the project, I'll be adding functions to the iotools module within pvlib-python, that will allow users to retrieve data from the following datasets (in addition to the existing ones):
* [Baseline Surface Radiation Network (BSRN)](https://bsrn.awi.de/)
* [ERA5 from ECMWF](https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era5)
* [MERRA2 from NASA](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/)
* [PVGIS hourly data](https://ec.europa.eu/jrc/en/PVGIS/tools/hourly-radiation)
* [CAMS McClear](http://www.soda-pro.com/web-services/radiation/cams-mcclear)
* [CAMS Radiation](http://www.soda-pro.com/web-services/radiation/cams-radiation-service/info)
* [Climate One Building](http://climate.onebuilding.org/)
```

After +200 hours behind the screen and keyboard, I have made 232 commits on GitHub, contributing 2992 lines of new code - you can see a full list of my contributions to pvlib [here](https://github.com/pvlib/pvlib-python/commits?author=adamrjensen). My contributions focused on adding new file reading and data retrieval functions for all of the above data sources, with the exception of Climate One Building. The reason for not including Climate One Building was that I concluded that other data sources would be preferable for almost all solar energy applications. Developing functions for Climate One Building would probably increase its use, which most likely would be undesirable.

Perhaps the work that I am most proud of are the functions for accessing and reading BSRN data. The [BSRN](https://bsrn.awi.de/) is a global network of high-quality radiation measurement stations, which store their data in a notoriously archaic file format. Accessing BSRN data is now super easy and can be done in just a few lines of code:

```python
import pvlib
import pandas as pd

df, meta = pvlib.iotools.get_bsrn(
    station='cab', start=pd.Timestamp(2018,6,1), end=pd.Timestamp(2018,8,31),
    username='username', password='password')
```

So if the success of the project is judged in terms of whether I achieved the objective of developing functions that "would allow novice and expert users alike to access a wealth of data" then I certainly believe that it has been a great success. I suppose there will first be sufficient user feedback in 6 months to really tell. Though already now, I've been getting feedback from colleagues in the field of solar resource assessment that they have found the functions useful in their work.

The project sponsor, Google, states that the [goals of GSoC](https://google.github.io/gsocguides/student/#goals-of-the-program) are:
* Inspire young developers to begin participating in open source development.
* Help open source projects identify and bring in new developers.
* Get more open source code written and released for the benefit of all.
* Provide students the opportunity to do work related to their academic pursuits during the summer: "flip bits, not burgers."
* Give students more exposure to real-world software development.

I can confidently say that all of these goals have been fulfilled to a great extent in this project. It's certainly been a very inspiring process, where I've written a lot of code and learned more than I ever could have imagined - and I have no plans of stopping contributing to pvlib and other open-source communities.

## Pull requests
All the work I've done during the project has resulted in pull requests, most of which are already merged into pvlib's master branch. Each pull request contains a description of the added functionality, as well as the entire development history, i.e., discussion along the way, code reviews, and an overview of the new code and tests.

First, I'd recommend that you check out the documentation of the functions, and if you still are interested in the details of the function development, then check out the pull requests:

* CAMS Radiation and McClear from SoDa-Pro: [documentation](https://pvlib-python.readthedocs.io/en/latest/generated/pvlib.iotools.get_cams.html), [pull](https://github.com/pvlib/pvlib-python/pull/1175)
* PVGIS Hourly radiation: [documentation](https://pvlib-python.readthedocs.io/en/latest/generated/pvlib.iotools.get_pvgis_hourly.html), [pull](https://github.com/pvlib/pvlib-python/pull/1186)
* BSRN data: [documentation](https://pvlib-python.readthedocs.io/en/latest/generated/pvlib.iotools.get_bsrn.html), [pull](https://github.com/pvlib/pvlib-python/pull/1254)
* ERA5: [pull](https://github.com/pvlib/pvlib-python/pull/1264)
* MERRA-2: [pull](https://github.com/pvlib/pvlib-python/pull/1274)
* Fix of iotools inconsistencies: [pull](https://github.com/pvlib/pvlib-python/pull/1268)

I'm already planning on contributing to pvlib iotools in the future, possibly adding functionality for downloading files locally, as discussed in this PR [#1282](https://github.com/pvlib/pvlib-python/pull/1282).

## Recommendations to future GSoC students
If you are a student and in doubt whether to participate due to time or other commitments, then do it anyway! There is absolutely no better way to learn software development than, well, just doing it. And when do you really have the chance to get a personal mentor? Almost never, so this is your chance to make something useful out of your summer, both for yourself and software users around the world.

## Acknowledgements
The true hero of this project is my mentor [Kevin Anderson](https://github.com/kanderso-nrel), who first encouraged me to apply for the program and devoted countless hours to this project. Kevin's passion was an inspiration throughout the entire project, and am incredible thankful for all the time he spent teaching me basic software concents, helping me debug when I got stuck, and fun discussions on non-related tangent topics (like the eating habbits of antlions).

The pvlib maintainers, Will Holmgreen, Mark Mikofski, and Cliff Hansen, have also been of invaluable help throughout the project - reviewing my ever-improving code and discussing the future direction of pvlib. I'd also like to thank Google founders Sergey Brin and Larry Page, for coming up with the concepts for Google Summer of Code and funding future generations of open-source software developers.
