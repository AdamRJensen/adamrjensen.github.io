---
author: Adam R. Jensen
date : 2021-06-10
tags: pvlib, solar, open science, gsoc
---

# pvlib - a one stop source for solar resource data
![gsoc and pvlib logo](/images/gsoc_at_pvlib.png)

This title at least represents the aim of my [Google Summer of Code (GSoC)](https://summerofcode.withgoogle.com/about/) project that I will be completing during the next 10 weeks. In short, I’ll be extending [pvlib python’s](https://pvlib-python.readthedocs.io/en/stable/) current iotools functionalities to provide users with easy and standardized access to all major open-source solar resource databases.

And why would I do that, you ask? Well, first of all, I am a bit of a solar geek, but my primary motivation comes from a frustration over how unnecessarily difficult it is to obtain good solar resource data. 
The good thing is that there actually is a lot of very good data out there, free for anyone to use! The downside is that the time and technical expertise required to obtain the data is limiting its wider use.

Given that solar irradiance is the most important input to predicting solar energy yield, using suboptimal data is kinda a big deal. Solar resource data is not only essential to the design stage but is also crucial for benchmarking solar radiation models (decomposition models, forecasting techniques, etc.) and assessing system performance.

pvlib python has a module called `iotools` for retriving/reading solar data, but it currently only supports access to a few of the many available sources and covers a limited part of the world.

## Data sources
During the project I'll be adding functions to the iotools within pvlib python, that will allow users to retrieve data from the following datasets (in addition to the existing ones):
- [Baseline Surface Radiation Network (BSRN)](https://bsrn.awi.de/) 
- [ERA5 from ECMWF](https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era5)
- [MERRA2 from NASA](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/)
- [PVIGS hourly data](https://ec.europa.eu/jrc/en/PVGIS/tools/hourly-radiation)
- [CAMS McClear](http://www.soda-pro.com/web-services/radiation/cams-mcclear)
- [CAMS radiation](http://www.soda-pro.com/web-services/radiation/cams-radiation-service/info)
- [Climate One Building](http://climate.onebuilding.org/)

Each of the above datasets have their own strengths and differs by geographical coverage, time resolution, and accuracy. But I’ll cover this in more detail in a later blog post.

```{note}
You can already check out some of the existing pvlib functions for retrieving data. For example, satellite-derived solar irradiance and clear-sky data from [CAMS](https://pvlib-python.readthedocs.io/en/latest/generated/pvlib.iotools.get_cams.html) and ground measurements from the [Solar Radiation Monitoring Laboratory (SRML) monitoring stations](https://pvlib-python.readthedocs.io/en/stable/generated/pvlib.iotools.read_srml_month_from_solardat.html#pvlib.iotools.read_srml_month_from_solardat).
```

If you think that I’ve missed any important open-source datasets, please let me know!

## Google Summer of Code
Google Summer of Code (GSoC) is a global program that aims at getting students writing code and taking active part in the open-source community. During the 10 week program, the organization provides a mentor that guides the student through the process.

I’m very fortunate to have a phenomenal mentor, [Kevin Anderson](https://github.com/kanderso-nrel).

For now, you can read my official project abstract [here](https://summerofcode.withgoogle.com/projects/#6071460558274560).

## What’s next?
I just completed adding [CAMS support to pvlib python](https://github.com/pvlib/pvlib-python/pull/1175). CAMS provides satellite-derived solar radiation for Europe and Africa. But not only that, CAMS also lets you retrieve McClear clear-sky data for anywhere in the world. Hint: McClear is based on actual aerosol data and probably provides the best clear-sky data you will ever use.

Now that this has been completed, I have moved on to writing tests for the functions I’ve written for retrieving and reading hourly data from PVGIS.

So stay tuned for more news on how you can easily get your hands on solar radiation data, and leave a comment below if you have any questions in getting started with retrieving CAMS data!
