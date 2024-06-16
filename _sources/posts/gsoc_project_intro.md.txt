# Enhancing solar energy modelling: implementing new spectral corrections in pvlib python
# A first blog post
```{post} 2024-05-27
:author: Rajiv Daxini
:tags: pvlib, solar, open science, gsoc, introduction
```

This first blog post introduces the motivation and plan for my [Google Summer of Code (GSoC)](https://summerofcode.withgoogle.com/about/) project. The overall aim of the project is to implement new spectral correction models in pvlib, as well as examples of their application and use. The official project abstract [can be found here](https://summerofcode.withgoogle.com/programs/2024/projects/TT5QrYqTv) and is reinstated below.

## Project abstract

Accounting for spectral effects in photovoltaic (PV) performance models is critical for accurate and reliable performance forecasts. Variation in the solar spectral distribution changes the useful fraction of irradiance incident on a PV device, and thus can increase or decrease its performance. The relationship between the performance of a PV module and the solar spectrum is captured by a “spectral correction function” (SCF), a plethora of which have been published in the literature over the last quarter of a century. However, only a fraction of these published models are available in pvlib. The aim of this project is to implement new SCFs in pvlib and develop examples to guide users in applying these models. The implementation of these new models will strengthen pvlib through enhancing its flexibility, accuracy, and reliability for different modelling scenarios. Furthermore, the additions to the example gallery will increase the accessibility and usability of these models and pvlib as a whole, in particular for new users.

## What motivates me?
As for my personal motivation, I am driven by a desire to contribute to pvlib and help improve the open-source resources available to scientists, engineers, and whoever else wants to know how a particular PV system is going to perform under any particular set of conditions. So, for one there is the goal to contribute, but on top of that is the fact that I need to and want to learn _how_ to contribute. As a proponent of open science and open source, it's a natural and necessary step for me to learn how to code collaboratively and the best way to learn is to do... so, here we are! As a newbie to open-source software development, I am also keen to share my learning experience with you, hence the existence of these blog posts. I hope not only to share technical updates on the project itself, but also reflect on the overall learning experience of open-source software development. I hope that in doing so I will be able to help and inspire others to engage and contribute to open-source projects, especially those with little or no prior experience of doing so.

Besides my internal motivation, I have to say that I am also motivated by my mentors for this project -- [Adam Jensen](https://github.com/AdamRJensen) and [Kevin Anderson](https://github.com/kandersolar). These guys' are integral members of the pvlib community and their commitment to the ongoing growth and development of pvlib is inspiring. After introducing me to the GSoC program, they both supported my application and I am fortunate to have them as my guides for this work.

![gsoc and pvlib logo](/images/gsoc_at_pvlib.png)

# Why care about spectral irradiance?
# Not all light is created equal
Aside from what motivates me to work on this project, what motivates the project itself? Sunny days => more solar power, right? What does the colour of light (spectral irradiance) have to do with anything? Well, not exactly. Not all light is created equal --- sometimes you have more infrared, sometimes more ultraviolet. Much like your skin when you go out on a sunny day, sometimes you get warm and sometimes you get sun burnt, solar panels also respond differently to different types of light (different spectra) because they have what is known as a "spectral response". Accounting for this effect when modelling PV performance is critical and failing to do so can lead to [errors of up to 15%](https://doi.org/10.1016/j.solener.2019.12.042) for annualised performance predictions.
# pvlib: current capabilities
Pvlib currently contains three spectral correction functions (SCFs) to model PV performance variations due to changes in the spectrum. However, the scope of models is limited in terms of the diversity of dependent variables and the documentation lacks examples to guide users on the implementation of these functions in the overall modelling pipeline. In terms of the diversity of dependent variables, there are two primary limitations. First, none of the existing models explicitly consider the effects of cloud cover. Second, all models are based on proxy variables. Proxy variables are indirect characterisation indices of the solar spectrum, suchas air mass, precipitable water content, and so on. These are atmospheric factors that influence the spectrum and whose influence is considered sufficiently dominant such that their value may be used as an indicator for the prevailing spectral irradiance conditions. As a simple analogy, when it is hot outside, one would expect ice cream sales to increase. Therefore, temperature could be used as a proxy for ice cream sales. The advantage of these varaibles is of course that they can easily be calcualted using easily acquirable parameters such as time of day, location, ambient air temperature, humidity, and so on. The limitation is that they limit the amount of information on the spectrum contained with the correction function. More information on different models and characterisation indices can be found [in this review paper](https://doi.org/10.1016/j.energy.2023.129461).
# pvlib: what's next?
Three new models will be implemented in pvlib. The first two models will be based on the air mass and clearness index parameters. These would be the first spectral corrections in pvlib to include the clearness index variable, which accounts for the effects of cloud cover on the solar spectrum. A stretch goal will be to include a third model that is not based on proxy variables, but rather variables derived directly from spectral irradiance data. [An issue](https://github.com/pvlib/pvlib-python/issues/1950) has been raised on GitHub, the response to which has provided guidance on which models from the literature are a priority for some users. The table below summarises the models existing in pvlib and those to be implemented through this project. The first three rows summarise the former while the last three rows summarise the altter.

| Model                                                | Reference                                                                      |
| ---------------------------------------------------- | ------------------------------------------------------------------------------ |
| Air mass                                             | [King et al. 2002](https://doi.org/10.1109/PVSC.1997.654283)                   |
| Air mass, aerosol optical depth, precipitable water  | [Caballero et al. 2018](https://doi.org/10.1109/JPHOTOV.2017.2787019)          |
| Air mass, precipitable water                         | [Lee and Panchula 2016](https://doi.org/10.1109/PVSC.2016.7749836)             |
| -------------Proposed models below------------------ | --------------------------Proposed models below------------------------------- |
| Air mass, clearness index                            | [Pelland et al. 2020 ](https://doi.org/10.1109/PVSC45281.2020.9300932)         |
| Air mass, clearness index                            | [Huld et al. 2009](http://dx.doi.org/10.4229/24thEUPVSEC2009-4AV.3.27)         |
| Average photon energy + spectral band depth          | [Daxini et al. 2023](https://doi.org/10.1016/j.energy.2023.129046)             |

The implementation of these models in pvlib will be supported by a new example demonstrating their application and use in the overall PV performance modelling pipeline. This will be the first example in pvlib python for a spectral correction function.

## Closing remark
Stay tuned into this blog for more updates. You can also follow [this github issue](https://github.com/pvlib/pvlib-python/issues/2065) and [my LinkedIn page](https://www.linkedin.com/in/rajiv-daxini-ba354a237/) for updates on the project. Please feel free to share your comments and thoughts on the open issues and public posts so that we may develop this project together. All and any feedback is always more than welcome!

-Dax 

27 May 2024
