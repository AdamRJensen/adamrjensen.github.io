# Project summary of Google Summer of Code with pvlib
```{post} 2021-08-22
:author: Adam R. Jensen
:tags: pvlib, solar, open science, gsoc
```

The coding period of this year's Google Summer of Code (GSoC) is officially over and it's time to take a step back and evaluate the experience. For those of you who haven't been following, I've been working on extending pvlib's iotools for the past 10 weeks, which I described in this [blog post](gsoc_project_intro/).

## Successfull or not?
Spoiler: it's been a huge success and I've learned much more than I imagined - and produced a lot of useful code.

First let's go back and look at the project outline:

> During the project I'll be adding functions to the iotools module within pvlib python, that will allow users to retrieve data from the following datasets (in addition to the existing ones):
> - [Baseline Surface Radiation Network (BSRN)](https://bsrn.awi.de/)
> - [ERA5 from ECMWF](https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era5)
> - [MERRA2 from NASA](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/)
> - [PVGIS hourly data](https://ec.europa.eu/jrc/en/PVGIS/tools/hourly-radiation)
> - [CAMS McClear](http://www.soda-pro.com/web-services/radiation/cams-mcclear)
> - [CAMS Radiation](http://www.soda-pro.com/web-services/radiation/cams-radiation-service/info)
> - [~~Climate One Building~~](http://climate.onebuilding.org/)

After +200 hours behind the screen and keyboard, I had managed to write xx lines of code with yy commits on GitHub, resulting in file reading and data retrieval functions for all of the above data sources, with the expcetion of Climate One Data. After further researching Climate One Data, I concluded that for al almost all solar energy applications, better datasets exists, hence it would be unfavorable making access to the dataset easier as this could increase it's usage (which most likely would be undesirable).

Perhaps the work that I am most proud of is the 

```{python}
import pvlib
import pandas as pd

df, meta = pvlib.iotools.get_bsrn(
    station='cab', start=pd.Timestamp(2018,6,1), end=pd.Timestamp(2018,8,31),
    username='username', password='password')
```


To answer this question I would like to simply demonstrate two exampes of how easy it now is to obtain solar resource data with pvlib:



## Pull requests
All the work I've done during the project, have resulted in completed pull request, adding new code to the stable version of pvlib-python.

The pull requests contains a description of the added functionality, as well as the entire development history, i.e., discussion along the way, code reviews, and of course an overview of the new code and tests.

* [CAMS Radiation and McClear from SoDa-Pro](https://github.com/pvlib/pvlib-python/pull/1175)
* [PVGIS Hourly radiation](https://github.com/pvlib/pvlib-python/pull/1186) - 52 commits 
* [BSRN data](https://github.com/pvlib/pvlib-python/pull/1254)
* [ERA5](https://github.com/pvlib/pvlib-python/pull/1264)
* [MERRA-2](https://github.com/pvlib/pvlib-python/pull/1274)
* [Fix of inconsistencies](https://github.com/pvlib/pvlib-python/pull/1268)

I'm certainly planning on contributing to the pvlib iotools in the future, possibly adding functionality for downloading files locally as discussed in this PR [#1282](https://github.com/pvlib/pvlib-python/pull/1282).

Most of the pull-requests have corresponding GitHub issues, which are referenced in the pull-request description.


## Blog posts



## Lessons learned
In the last two weeks of the program I've found myself stumbling into a few tasks that were similar to stuff I did in the beginning - the difference now being is that it's been super easy and having to re-apply it really sets in the learning. It's a great feeling being able to look back and think: this was really freaking hard last time I did it and it's effortless and you get why it works like it does.

## Recommendations to future GSoC students
* If you are in doubt whether to participate due to time or other commitment, then do it anyways! There is absolutely no better way to learn software development than actually doing it. And when do you really have the chance to get a personal mentor? Probably never.

## Acknowledgements
Kevin. The pvlib maintainers.
