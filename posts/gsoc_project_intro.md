---
author: Adam R. Jensen
date : 2021-06-10
tags: pvlib, solar, open science, gsoc
---

# pvlib-python - a one stop source for solar resource data

This title at least, represents the aim of my [Google Summer of Code (GSoC)](https://summerofcode.withgoogle.com/about/) project that I will be copmleting over the next two months. In short, I'll be extending pvlib python’s current iotools functionalities to allow seamless access to all major open-source solar resource databases.

And why would I do that you ask? Well first of all I am a bit of a solar geek, but more importantly, solar resource data is fundamental to the benchmarking solar energy systems, financial risk assessment, of large-scale solar projects, and sound research.


Information of the solar resource is perhaps the most important input when designing and assessing solar energy systems, which is at the core of the open-source library pvlib python. For this reason, pvlib currently has capabilities for reading a number of different file formats and supports access to sources for solar resource data, including PVGIS and NREL’s PSM3. However, the library currently only supports direct access to a few of the many available sources and only covers a limited area, primarily focusing on North America and Europe.

## Data sources
I'll be developing functions for accessing data from the following data sources:
- [Baseline Surface Radiation Network (BSRN)](https://bsrn.awi.de/) 
- [ERA5 from ECMWF](https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era5)
- [MERRA2 from NASA](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/)
- [PVIGS hourly data](https://ec.europa.eu/jrc/en/PVGIS/tools/hourly-radiation)
- [CAMS McClear](http://www.soda-pro.com/web-services/radiation/cams-mcclear)
- [CAMS radiation](http://www.soda-pro.com/web-services/radiation/cams-radiation-service/info)
- [Climate One Building](http://climate.onebuilding.org/)

Each of the above datasets have their own streths, and differs by geographical coverage, time resoultion, and accuracy.

```{note}
You can already check out some of the existing pvlib functions for retrieving data. For example, satellite derived solar data from [NRELS' National Solar Radiation Database (NSRDB)](https://pvlib-python.readthedocs.io/en/stable/generated/pvlib.iotools.get_psm3.html#pvlib.iotools.get_psm3) and ground measurement data from the [Solar Radiation Monitoring Laboratory (SRML) monitoring stations](http://solardat.uoregon.edu/SolarData.html).
```


## Google Summer of Code
If you're wondering what exactly Google Summer of Code is, then I can promise I'll do a post on that in a weeks time, when I know more myself. For now you can read the official project abstract [here](https://summerofcode.withgoogle.com/projects/#6071460558274560).






