# Summary of Google Summer of Code with pvlib
```{post} 2021-08-22
:author: Adam R. Jensen
:tags: pvlib, solar, open science, gsoc
```

The coding period of this year's Google Summer of Code (GSoC) is officially over, and it's time to take a step back and evaluate the experience. For those of you who might not know, I've been working on extending pvlib's iotools for the past 10 weeks, which I described in this [blog post](/posts/gsoc_project_intro).

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

After +200 hours behind the screen and keyboard, I have made 232 commits on GitHub, contributing 2992 lines of new code - you can see a full list of my contributions to pvlib during GSoC [here](https://github.com/pvlib/pvlib-python/commits?author=adamrjensen&since=2021-06-01&until=2021-08-22). My contributions focused on adding new file reading and data retrieval functions for all of the above data sources, with the exception of Climate One Building. The reason for not including Climate One Building was that I concluded that other data sources would be preferable for almost all solar energy applications. Developing functions for Climate One Building would probably increase its use, which most likely would be undesirable.

Perhaps the work that I am most proud of is the functions for accessing and reading BSRN data. The [BSRN](https://bsrn.awi.de/) is a global network of high-quality radiation measurement stations, which store their data in a notoriously archaic file format. Accessing BSRN data is now super easy and can be done in just a few lines of code:

```python
import pvlib
import pandas as pd

df, meta = pvlib.iotools.get_bsrn(
    station='cab', start=pd.Timestamp(2018,6,1), end=pd.Timestamp(2018,8,31),
    username='username', password='password')
```

So if the success of the project is judged in terms of whether I achieved the objective of developing functions that "would allow novice and expert users alike to access a wealth of data" then I certainly believe that it has been a great success. I suppose there will first be sufficient user feedback in 6 months to really tell, though already now, I've been getting positive feedback from colleagues in the field of solar resource assessment who say that they have found the functions useful in their work!

The project sponsor, Google, states that the [goals of GSoC](https://google.github.io/gsocguides/student/#goals-of-the-program) are:
* Inspire young developers to begin participating in open source development.
* Help open source projects identify and bring in new developers.
* Get more open source code written and released for the benefit of all.
* Provide students the opportunity to do work related to their academic pursuits during the summer: "flip bits, not burgers."
* Give students more exposure to real-world software development.

I can confidently say that all of these goals have been fulfilled to a great extent in this project. It's certainly been a very inspiring process, where I've written a lot of code and learned more than I ever could have imagined - and I have no plans of stopping contributing to pvlib and other open-source communities.

## Pull requests
All the work I've done during the project has resulted in pull requests, most of which are already merged into pvlib's master branch. Each pull request contains a description of the added functionality, as well as the entire development history, i.e., discussion along the way, code reviews, and an overview of the new code and tests.

First, I'd recommend that you check out the documentation of the functions, and if you still are interested in further details of the function development, then check out the pull requests:

* CAMS Radiation and McClear from SoDa-Pro: [documentation](https://pvlib-python.readthedocs.io/en/stable/reference/generated/pvlib.iotools.get_cams.html), [pull](https://github.com/pvlib/pvlib-python/pull/1175)
* PVGIS Hourly radiation: [documentation](https://pvlib-python.readthedocs.io/en/stable/reference/generated/pvlib.iotools.get_pvgis_hourly.html), [pull](https://github.com/pvlib/pvlib-python/pull/1186)
* BSRN data: [documentation](https://pvlib-python.readthedocs.io/en/stable/reference/generated/pvlib.iotools.get_bsrn.html), [pull](https://github.com/pvlib/pvlib-python/pull/1254)
* ERA5: [pull](https://github.com/pvlib/pvlib-python/pull/1264)
* MERRA-2: [pull](https://github.com/pvlib/pvlib-python/pull/1274)
* Fix of iotools inconsistencies: [pull](https://github.com/pvlib/pvlib-python/pull/1268)

I'm already planning on contributing to pvlib iotools in the future, possibly adding functionality for downloading files locally, as discussed in [PR #1282](https://github.com/pvlib/pvlib-python/pull/1282).

## Lessons learned
In the last two weeks of the program, I've found myself stumbling into tasks that were similar to what I did at the beginning of the program. The difference is that now I can effortlessly solve these problems, and I know how and why it works. It's truly a great feeling to realize that I’ve learned a ton, and it's already proven useful.

Now I'm first and foremost a scientist, and programming and software development are secondary interests. But I've been blown away by how much there is for scientists to learn from software development. The ability of open-source libraries to support a community of scientists, reducing each individual’s workload and providing access to tested and validated tools, is of incredible value. Why don't we do more of this!?! As I come to the end of my Ph.D. and begin to plan my post-doc in the Spring, I hope to inspire others in my research community to use open-source tools and contribute to them, as I truly believe this can result in better and more efficient and reproducible science.

## Recommendations to future GSoC students
If you are a student and in doubt whether to participate due to time or other commitments, then do it anyway! There is absolutely no better way to learn software development than, well, just doing it. And when else do you really have the chance to get a personal mentor? Almost never, so this is your chance to make something useful out of your summer, both for yourself and software users around the world.

Even better, get involved with an open-source community first, which could likely lead you to the opportunity to participate in GSoC. Start with just a small pull request fixing a typo to familiarize yourself with the workflow and how things are done. Then progress by taking up an issue labeled `good first issue` and asking for help. GSoC formalizes this process, but there's no way you shouldn't get started today!

## Acknowledgments
The true hero of this project is my mentor [Kevin Anderson](https://github.com/kandersolar), who first encouraged me to apply for the program and devoted countless hours to this project. Kevin's passion was an inspiration throughout the entire project, and I am incredibly thankful for all the time he spent teaching me basic software concepts, helping me debug when I got stuck, and fun off-topic discussions (like the eating habits of antlions).

The pvlib maintainers, Will Holmgren, Mark Mikofski, and Cliff Hansen, have also offered invaluable help throughout the project - reviewing my ever-improving code and discussing the future direction of pvlib. I'd also like to thank Google founders Sergey Brin and Larry Page, for coming up with the concepts for Google Summer of Code and funding future generations of open-source software developers.
