---
date : 2021-05-21
title : "How to create this blog"
---

# How to create this blog
In this How-to, I explain the tools I used to create this blog and how you can create one of your own! The 2 core tools are [The Executable Books Project (EBP)](https://executablebooks.org/en/latest/) and [Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html).


## The Executable Books Project (EBP)
The EBP is a collection of tools under the Jupyter ecosystem focused on allowing Data Scientists (or anyone really) to create computational narratives or "executable books". My 1st exposure to the EBP was when I came across one of their most popular tools - [Jupyterbook](https://jupyterbook.org/). 

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
.
├── LICENSE
├── Makefile
├── README.md
├── _build
├── _static
│   ├── custom.css
│   ├── magnifying.ico
│   └── profile.png
├── _templates
│   ├── archives.html
│   ├── footer.html
│   ├── hello.html
│   ├── recentposts.html
│   └── tags.html
├── about.md
├── conf.py
├── index.md
├── posts
│   ├── jupyter_post.ipynb
│   └── markdown_post.md
└── requirements.txt
```
### Setting up
Clone the repository

```
git clone https://github.com/ddanieltan/blog_ebp_sphinx_starter.git
```

Install the dependencies

```
conda create --name blog_env -c conda-forge --file requirements.txt
```

You can build your site with

```
make html
```
This command will populate the `_build` directory with the required html/css files that will make up your blog website.

Alternatively, you can also run
```
make live
```
This command will not only populate the `_build` directory, but also watch this directory for any changes. Once it detects a change, it will autobuild the site again. By default, your site can be viewed locally on `localhost:8000`. This is particularly more convenient when you are crafting a new blog post and want to see how it appears in a browser.

And there you go, you now have everything set up to start blogging! 🥳 🥳 🎉 🎉

## How to write posts

When I'm crafting a new post, I typically do so using `jupyter lab`. If I'm crafting a new post using a jupyter notebook, I can actually run and execute any code block that appears in my post. And, I have full control over whether I want to display each code cell's inputs, outputs or both. You can see the full flexibility of options at [https://jupyterbook.org/file-types/notebooks.html](https://jupyterbook.org/file-types/notebooks.html).

In my opinion, this is what makes this approach for writing blogs shine! Unlike many other blogging solutions, every post lives as an executable piece of code, while still giving the author control over the look and narrative of this post when it goes unto the web.

## Miscellaneous details

When I was building this blog, I ran into areas I did not find entirely straightforward. Here are some notes I wrote that might help you if you run into any roadblocks.

### conf.py

`conf.py` is the main configuration file for the entire project and it contains a lot of settings. My advice is to really experiment and play around with all these settings to understand the extent of how to make this blog your own.

When it comes to exploring the full list of configurable options we will hit 1 of the downsides of my approach to creating a blog. As we are are using separate libraries, we don't have a single centralized place that records all the configurable options in this project. So for any existing of new configuration you want to implement, you will need to spend some time exploring the following resoures:
- [Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html) 
- [Ablog documentation](https://ablog.readthedocs.io/)
- [Pydata Theme documentation](https://pydata-sphinx-theme.readthedocs.io/en/latest/index.html)
- [MyST parser documentation](https://myst-parser.readthedocs.io/en/latest/using/intro.html)

### index.md
Every html output page has an equivalent markdown/Jupyter notebook page. Most pages are rather self explanatory, for example you can compare the output of The order of the pages in the topbar of the site inherits from the `toctree`.

### Customizing html and css
There were some customizations I wanted to make to my site that did not have a `conf.py` API. 

For example, by default, "Build with Sphinx \<version>" is written in every `footer.html`. While I definitely wanted to attribute my blog to Sphinx, but equally, I wanted to attribute the tools from EBP. As I could not find a way to configure my footer message in `conf.py`, my eventual solution was simply to overwrite the `footer.html` in `_templates/` with the message you currently see.

`footer.html` is written in the [Jinja templating language](https://jinja.palletsprojects.com/en/2.11.x/), which means you can probably elegantly use the `{extends}` pattern to append added code. However, as I'm honestly quite new to front end coding, I just overwrote the entire file using code taken from its [source](https://github.com/pandas-dev/pydata-sphinx-theme/blob/master/pydata_sphinx_theme/footer.html).

Similarly, any custom css, for example the [waving hand animation](https://jarv.is/notes/css-waving-hand-emoji/) in my About me page, is added to `_static/custom.css`. 

All custom themes and css are written last during each build, ensuring those settings overwrite the defaults.

## Conclusion
I think I speak for many when I say that I know that blogging is an incredibly useful thing to do, but there's  always so much inertia to start and maintain a blog. These set of tools really helped inspire me to get past my inertia to start my blog, and I hope that this post will help you to start yours too! 👍