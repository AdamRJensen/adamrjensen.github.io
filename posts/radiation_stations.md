# Overview of solar radiation monitoring stations
```{post} 2021-09-23
:author: Adam R. Jensen
:tags: solar, open science
```

Ground measured solar irradiance is extremely valuable and critical to benchmarking solar radiation products and understanding long-term trends in the radiation budget. However, due to high costs and maintenance requirements, there are only a few hundred high-quality stations globally. Currently, it is difficult to identify the nearest solar radiation station as there is no good overview of the stations worldwide. This blog post addresses this issue by proposing a simple catalog/database of high-quality radiation stations.


## Scope
First, it is important to determine the scope, most importantly, which type of stations and parameters to include. As the focus is on high-quality stations, only stations that measure all three irradiance components are considered. Stations can be classified into two different categories, Tier 1 and Tier 2 stations.

### Tier 1 stations
Tier 1 stations are defined as meet all of the following requirements:
* measurement of direct normal irradiance (DNI) with a Class A thermopile pyrheliometer mounted on a solar tracker
* measurement of diffuse horizontal irradiance (DHI) with a thermopile pyranometer shaded by a shading ball
* measurement of global horizontal irradiance (GHI) with a Class A thermopile pyranometer

Seperate measurement of GHI is required for Tier 1 stations as this allows for thoroughly quality control. The stations in the [BSRN](https://bsrn.awi.de/) network are examples of Tier 1 stations.

### Tier 2 stations
Tier 2 stations are defined as those that do not meet the Tier 1 requirement but meet one of the following specifications:
* Meets two of the three requirements of the Tier 1 stations
* Measures GHI and DHI using a rotating shading band pyranometer

### Non-qualifying stations
Stations that measure DHI using a shadow band are not considered, as shadow bands have to be manually adjusted every few days and are notoriously unreliable.

## Basic station metadata
The main part of the catalog is the list of stations and their metadata, including:
* Latitude, longitude, and elevation (according to ISO format)
* Years of operation
* City and Country
* Station name
* Station abbreviation
* Station network (e.g., BSRN, SURFRAD)
* Link to website (multiple links?)
* Link to publications?

The format for the time period should accommodate non-continuous periods and denote whether a station is currently active. The time period for a station from 2013 that is still active but does not have data for 2014 and 2019 could be denoted as (2013, 2015-2018, 2020-).

As not all stations have data available publicly, it would be convenient for users if a contact email was available. However, issues relating to spam emailing probably outweigh the pros, hence, for now, this field will be left out.

### Additional metadata
The above list of metadata are the miminum requirements for each station. It should be considered what additional metadata might also be added, such as:
* annual average GHI/DNI
* climate zone
* if spectral, albedo, or aerosol measurements are available
* station owner with links? (e.g., NOAA, Norwegian Meteorological Institute)
* which components are measured
* intrument types

Also, it should be considered how we can pass on information concerning good and bad stations or station years, e.g., some Tier 1 BSRN stations are very poor. It could be a possebility having a subpage for each station with images and general information, e.g., comments on the overall quality.


## Implementation
The catalog will be placed in a GitHub repository, allowing it to be continuously updated as stations close down or new stations become available. This means it'll be open-source and it's the aim that it will be supported by the solar research community.

The central part of this project will be a comma-separated text file (CSV) with a header line followed by lines of metadata for each station. While an Excel file would perhaps be more convenient, version control is not well supported for Excel files. However, an Excel file will be automatically generated from the CSV file every time this is updated; hence users will have the option of downloading either a .csv or .xlsx file.

### Map overview
Also, an interactive map of all the stations will be made. This will allow users to conveniently find the station nearest to their point of interest and obtain the station name by clicking on the corresponding icon on the map.

## To do
* Add license
* Write acknowledgments of data providers
* Should stations be organized by station name or country or a third criteria?
* Should ventilation of pyranometers also be required for Tier 1 stations?
