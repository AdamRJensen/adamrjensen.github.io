---
author: Adam R. Jensen
date : 2021-06-10
tags: pvlib, solar, open science, gsoc
---

# pvlib - a one stop source for solar resource data
![gsoc and pvlib logo](/images/gsoc_at_pvlib.png)

This title at least, represents the aim of my [Google Summer of Code (GSoC)](https://summerofcode.withgoogle.com/about/) project that I will be completing during the next two months. In short, I'll be extending [pvlib python’s](https://pvlib-python.readthedocs.io/en/stable/) current iotools functionalities to allow seamless access to all major open-source solar resource databases.

And why would I do that you ask? Well first of all I am a bit of a solar geek, but more importantly, solar resource data is essential to every step, from the preliminary design stage (where accurate data is crucial to determine the profitability of a project) to post-project completion during plant operation (where solar resource assessment is used to forecast and verify system performance).

While pvlib currently has capabilities for reading a number of different file formats and supports access to sources for solar resource data, the library currently only supports direct access to a few of the many available sources and only covers a limited part of the world, primarily focusing on North America.


## Data sources
The aim of this project is to extend the current capabilities of the iotools within pvlib python, by developing harmonized access functions for all major open-source solar resource databases and filetypes, including:
- [Baseline Surface Radiation Network (BSRN)](https://bsrn.awi.de/) 
- [ERA5 from ECMWF](https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era5)
- [MERRA2 from NASA](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/)
- [PVIGS hourly data](https://ec.europa.eu/jrc/en/PVGIS/tools/hourly-radiation)
- [CAMS McClear](http://www.soda-pro.com/web-services/radiation/cams-mcclear)
- [CAMS radiation](http://www.soda-pro.com/web-services/radiation/cams-radiation-service/info)
- [Climate One Building](http://climate.onebuilding.org/)

Each of the above datasets have their own streths, and differs by geographical coverage, time resoultion, and accuracy.

```{note}
You can already check out some of the existing pvlib functions for retrieving data. For example, satellite derived solar irradiance data from [NREL's National Solar Radiation Database (NSRDB)](https://pvlib-python.readthedocs.io/en/stable/generated/pvlib.iotools.get_psm3.html#pvlib.iotools.get_psm3) and ground measurements from the [Solar Radiation Monitoring Laboratory (SRML) monitoring stations](https://pvlib-python.readthedocs.io/en/stable/generated/pvlib.iotools.read_srml_month_from_solardat.html#pvlib.iotools.read_srml_month_from_solardat).
```

Also, if you know of a data source that I have not include, but probably should have, please do let me know!

## Google Summer of Code
So what is Google Summer of Code? It is essentially a then I can promise I'll do a post on that in a few weeks time, when I know more myself. For now you can read the official project abstract [here](https://summerofcode.withgoogle.com/projects/#6071460558274560).


## What's next?




