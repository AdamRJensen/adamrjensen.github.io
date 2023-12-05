#!/usr/bin/env python


# Adam R. Jensen build configuration file, created by
# `ablog start` on Tue Jun  8 16:24:54 2021.

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# import ablog


# -- Project information -----------------------------------------------------

project = "Predictably Sunny"
copyright = "2021, Adam R. Jensen"
author = "Adam R. Jensen"


# -- General ABlog Options ----------------------------------------------------

# A path relative to the configuration directory for blog archive pages.
blog_path = 'blog'

# The "title" for the blog, used in active pages.  Default is ``'Blog'``.
blog_title = "Predictably Sunny"

# Base URL for the website, required for generating feeds.
blog_baseurl = "http://predictablysunny.com/"

# -- Blog Post Related --------------------------------------------------------

# Format date for a post.
# post_date_format = '%%d %%b, %%Y'

# Number of paragraphs (default is ``1``) that will be displayed as an excerpt
# from the post. Setting this ``0`` will result in displaying no post excerpt
# in archive pages.  This option can be set on a per post basis using
# post_auto_excerpt = 1

# Index of the image that will be displayed in the excerpt of the post.
# Default is ``0``, meaning no image.  Setting this to ``1`` will include
# the first image, when available, to the excerpt.  This option can be set
# on a per post basis using :rst:dir:`post` directive option ``image``.
# post_auto_image = 0

# Number of seconds (default is ``5``) that a redirect page waits before
# refreshing the page to redirect to the post.
# post_redirect_refresh = 1

# -- ABlog Sidebars -------------------------------------------------------

# There are seven sidebars you can include in your HTML output.
# postcard.html provides information regarding the current post.
# recentposts.html lists most recent five posts. Others provide
# a link to a archive pages generated for each tag, category, and year.
# In addition, there are authors.html, languages.html, and locations.html
# sidebars that link to author and location archive pages.
html_sidebars = {
    '**': [ #'about.html',
            #'postcard.html', 'navigation.html',
            'recentposts.html', #'tagcloud.html',
            #'categories.html',  'archives.html',
            #'searchbox.html',
            ],
    }

# -- Blog Feed Options --------------------------------------------------------

# Turn feeds by setting :confval:`blog_baseurl` configuration variable.
# Choose to create feeds per author, location, tag, category, and year,
# default is ``False``.
# blog_feed_archives = False

# Choose to display full text in blog feeds, default is ``False``.
# blog_feed_fulltext = False

# Blog feed subtitle, default is ``None``.
# blog_feed_subtitle = None

# Choose to feed only post titles, default is ``False``.
# blog_feed_titles = False

# Specify custom Jinja2 templates for feed entry elements:
#     `title`, `summary`, or `content`
# For example, to add an additional feed for posting to social media:
# blog_feed_templates = {
#     # Use defaults, no templates
#     "atom": {},
#     # Create content text suitable posting to social media
#     "social": {
#         # Format tags as hashtags and append to the content
#         "content": "{ title }{% for tag in post.tags %}"
#         " #{ tag.name|trim()|replace(' ', '') }"
#         "{% endfor %}",
#     },
# }
# Default: Create one `atom.xml` feed without any templates
# blog_feed_templates = {"atom": {} }

# Specify number of recent posts to include in feeds, default is ``None``
# for all posts.
# blog_feed_length = None

fontawesome_included = True

# Alternatively, you can provide the path to `Font Awesome`_ :file:`.css`
# with the configuration option: fontawesome_css_file
# Path to `Font Awesome`_ :file:`.css` (default is ``None``) that will
# be linked to in HTML output by ABlog.
# fontawesome_css_file = None

# -- Sphinx Options -----------------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_nb',
    'ablog',
    'sphinxext.opengraph',
    'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/pandoc_ipynb/inputs/*', 'ipynb_checkpoints/*']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pydata_sphinx_theme'
html_title = 'Predictably Sunny'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
  "github_url": "https://github.com/adamrjensen/",
  "analytics": {"google_analytics_id": "G-B5PLZ8N24G"},
  "navbar_end": ["navbar-icon-links.html", "search-field.html"],
  "search_bar_text": "Search this site...",  # defaults to "Search the docs..."
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_sidebars = {
    "index": ["hello.html"],
    "about": ["hello.html"],
    "publications": ["hello.html"],
    "projects": ["hello.html"],
    "posts/**": ['ablog/postcard.html', 'ablog/recentposts.html'],
    "blog": ['ablog/archives.html'],  # 'ablog/tagcloud.html'
    "blog/**": ['ablog/postcard.html', 'ablog/recentposts.html', 'ablog/archives.html']
}

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%%b %%d, %%Y'

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = False

blog_post_pattern = "posts/*"

# OpenGraph config
ogp_site_url = "https://predictablysunny.com"
ogp_image = "https://predictablysunny.com/_static/profile.png"

# Adds custom css templates, necessary for the custom "hello.html" template
def setup(app):
    app.add_css_file("custom.css")

#jupyter_execute_notebooks = "off"
#nb_execution_allow_errors = True

nb_execution_excludepatterns = ['irradiance_maps.ipynb', 'inset_map_cartopy.ipynb', 'twoaxistracking_animation.ipynb', 'blue_marble_map.ipynb', 'earth_as_rubiks_cube.ipynb', 'danish_district_heating_areas.ipynb', 'draft/*']
