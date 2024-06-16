# Overview of solar radiation monitoring stations
```{post} 2021-09-23
:author: Adam R. Jensen
:tags: solar, open science
```

Ground-measured solar irradiance data is extremely valuable and critical for benchmarking solar radiation products and understanding the long-term trend in the radiation budget. However, there are only a few hundred high-quality stations globally due to high costs and maintenance requirements. Currently, it is difficult to identify where the nearest solar radiation station is located, as there is no overview of stations worldwide. In this blog, I suggest solving this issue by creating a simple catalog/database of available high-quality radiation stations.

```{note}
This blog post describe the original ideas that led to the [SolarStations.org](https://solarstations.org) website.
```

## Scope
First, it is important to determine the scope, specifically which types of stations and parameters to include. As the focus is on high-quality stations, only stations that measure all three irradiance components are considered. High-quality stations can be classified into two different categories: Tier 1 and Tier 2 stations.

### Tier 1 stations
Tier 1 stations are defined as those that meet all of the following requirements:
* measurement of direct normal irradiance (DNI) with a Class A thermopile pyrheliometer mounted on a solar tracker
* measurement of diffuse horizontal irradiance (DHI) with a Spectrally Flat Class A thermopile pyranometer shaded by a shading ball
* measurement of global horizontal irradiance (GHI) with a Spectrally Flat Class A thermopile pyranometer

Separate measurement of GHI is required for Tier 1 stations as most quality control procedures rely on comparing the measured and calculated GHI (closure equation). The stations in the [BSRN](https://bsrn.awi.de/) network are examples of Tier 1 stations.

### Tier 2 stations
Tier 2 stations are defined as those that do not meet the Tier 1 requirements but meet one of the following specifications:
* Meets two of the three requirements of Tier 1 stations
* Measures GHI and DHI using a rotating shading band pyranometer

### Non-qualifying stations
Stations that measure DHI using a shadow band are not considered, as such measurements are notoriously unreliable due to the shadow bands having to be manually adjusted every few days.

## Station metadata
The central part of the catalog is the list of stations and their metadata, including:
* Latitude, longitude, and elevation (according to ISO format)
* Years of operation
* City and Country
* Station name
* Station abbreviation
* Station network (e.g., BSRN, SURFRAD)
* Link to the station or network website (multiple links?)

The format for the time period should accommodate non-continuous periods and denote whether a station is currently active. The time period for a station from 2013 that is still active but does not have data for 2014 and 2019 could be denoted as (2013, 2015-2018, 2020-).

As not all stations have data available publicly, it would be convenient for users if a contact email was provided. However, issues relating to spam emailing probably outweigh the pros; hence, for now, this will be left out.

### Additional metadata
The above list of metadata is the minimum requirement for each station. It should be considered what additional metadata might also be added, such as:
* annual average GHI/DNI
* climate zone
* if spectral, albedo, or aerosol measurements are available
* which components are measured, e.g., upward fluxes
* additional meteorological parameters, e.g., temperature
* instrument types
* surface type, topography, rural/urban (categories used by the BSRN)
* Link to publications describing the station

Also, it should be considered how we can pass on information concerning good and bad stations or station years, e.g., some Tier 1 BSRN stations are very poor. It could be a possibility to have a subpage for each station with images and general information, e.g., comments on the overall quality.

## Implementation
The catalog will be hosted in a GitHub repository, allowing it to be continuously updated as stations close down or new stations become available. This means it will be open-source, and it is the aim that it will be supported by the solar research community.

The central part of this project will be a CSV file with a header line followed by lines of metadata for each station. While an Excel file would perhaps be more convenient for editing, version control is not well supported for Excel files. However, an Excel file will be automatically generated from the CSV file every time this is updated; hence users will have the option of downloading either a .csv or .xlsx file.

### Map overview
Also, an interactive map of all the stations will be made. This will allow users to conveniently find the station nearest to their point of interest and obtain the station name by clicking on the corresponding icon on the map.

## To do
* Discuss whether stations should be organized by name or country or a third criteria
* Write acknowledgments of data providers
* Should ventilation of pyranometers also be required for Tier 1 stations?
* Allow class B instruments in Tier 2?
* Define Tier 3 for complete characterization of all radiation stations (e.g., stations with just GHI)?
* Require 1-minute resolution for both Tier 1 and 2?
* Give an example of how to download data? (pvlib)
* Denote if they also measure temperature

### Have done
* Changed the name to SolarStations instead of RadiationStations
* Get a custom domain name
