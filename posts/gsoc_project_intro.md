---
author: Adam R. Jensen
date : 2021-06-10
tags: pvlib, solar, open science, gsoc
---

# pvlib-python - a one stop source for solar resource data

This title at least, represents the aim of my [Google Summer of Code (GSoC)](https://summerofcode.withgoogle.com/about/) project that I will be copmleting over the next two months. In short, I'll be extending pvlib python’s current iotools functionalities to include harmonized functions for allowing seamless access to all major open-source solar resource databases.

And why would I do that you ask? Well first of all I am a bit of a solar geek, but more importantly, solar resource data is fundamental to the deployment of new solar projects, and sound research.


Information of the solar resource is perhaps the most important input when designing and assessing solar energy systems, which is at the core of the open-source library pvlib python. For this reason, pvlib currently has capabilities for reading a number of different file formats and supports access to sources for solar resource data, including PVGIS and NREL’s PSM3. However, the library currently only supports direct access to a few of the many available sources and only covers a limited area, primarily focusing on North America and Europe.

## Data sources


## Google Summer of Code
If you're wondering what exactly Google Summer of Code is, then I can promise I'll do a post on that in a weeks time, when I know more myself. For now you can read the official project abstract [here](https://summerofcode.withgoogle.com/projects/#6071460558274560).



Jupyterbook is a library that allows you to create your very own online textbook built up from either markdown files or Jupyter Notebooks. I had a lot of fun playing around with Jupyterbook over a weekend, and started to dream of the possibility to use the EBP tools to build a blog. 

```{note}
I was excited enough about the idea of building a blog with Jupyterbook that I raised [this issue here](https://github.com/executablebooks/jupyter-book/issues/900) (and it's still 1 of the project's top 👍 issue!)
```
You can explore the entire ecosystem of tools under the EBP on this [page](https://executablebooks.org/en/latest/tools.html).

## Sphinx
Sphinx is a Python-based documentation generation tool that efficiently indexes and keeps track of content files. Amongst Sphinx's many extensions is one called [Ablog](https://ablog.readthedocs.io/). Ablog uses Sphinx as an engine to convert my content files into html/css files that make up this site.

```{admonition} Alternative blogging tool - [Fastpages](https://github.com/fastai/fastpages)
:class: tip
You might also want to consider Fastpages as an alternative notebook-focused blogging library. It comes from the excellent fastai family of tools.

The only reason why I decided to not go with Fastpages was that I had a preference of using Sphinx(Python) over Jekyll(Ruby). I've read in the [fastai forums](https://forums.fast.ai/t/fastpages-github-pages-blog-using-nbdev/62828/273) that a new version powered by Hugo is planned, and would be very interested to try that once it's out!
```

## My reasons for using EBP + Sphinx

I am familiar with Jupyter and Sphinx because I use these tools at work
: My goal for blogging is to practise my writing, so it's important to me that the tooling doesn't get too in the way.

Jupyter notebooks are 1st class citizens
: Jupyter notebooks are notoriously finicky to convert into html/css. The tools from EBP essentially take away a lot of the usual friction you would encounter and make it easy to include other features such as 

I like the aesthetics of the [Pydata theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/index.html)
: If, like me, you spend a lot of time reading the [pandas documentation](https://pandas.pydata.org/docs/), you probably would find the look and feel of this blog comfortingly familiar. That's because the blog is using the exact same theme! I've grown to like the design choices of this theme, and applying it to my blog was a no-brainer.

I was inspired by [Chris Holdgraf's blogpost starter template](https://predictablynoisy.com/posts/2020/sphinx-blogging/)
: Chris is one the core members in EBP. In this blogpost, Chris explains how he rewrote his blog using EBP + Sphinx and the source code and helpful links. Thanks to this blogpost, things were simple enough for me to start working on my own. My blog and the template I will share in the next section is pretty much Chris's starter code + a few modifications from me.


## [Blog Starter Template](https://github.com/ddanieltan/blog_ebp_sphinx_starter)

```{admonition} Caveat
:class: warning
I am super happy to share my template + explain my approach to get my blog up and running.
But, I also want to state up-front that I have **very little experience with front-end programming**. So more than likely, this next section contains some convuluted/hacky/incorrect/inefficient code. 

(If you find any issue, [drop me an email](/about/) to explain what I'm doing wrong and I'll do my best to correct it.)
```

I have created a simple blog starter template at [https://github.com/ddanieltan/blog_ebp_sphinx_starter](https://github.com/ddanieltan/blog_ebp_sphinx_starter).
These are the files in the repo:

```
git clone https://github.com/ddanieltan/blog_ebp_sphinx_starter.git
```


When I'm crafting a new post, I typically do so using `jupyter lab`. If I'm crafting a new post using a jupyter notebook, I can actually run and execute any code block that appears in my post. And, I have full control over whether I want to display each code cell's inputs, outputs or both. You can see the full flexibility of options at [https://jupyterbook.org/file-types/notebooks.html](https://jupyterbook.org/file-types/notebooks.html).



When it comes to exploring the full list of configurable options we will hit 1 of the downsides of my approach to creating a blog. As we are are using separate libraries, we don't have a single centralized place that records all the configurable options in this project. So for any existing of new configuration you want to implement, you will need to spend some time exploring the following resoures:
- [Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html) 
- [Ablog documentation](https://ablog.readthedocs.io/)
- [Pydata Theme documentation](https://pydata-sphinx-theme.readthedocs.io/en/latest/index.html)
- [MyST parser documentation](https://myst-parser.readthedocs.io/en/latest/using/intro.html)
