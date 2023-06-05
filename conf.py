# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os.path

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'NeuroPoly'
copyright = '2021, NeuroPoly'
author = 'NeuroPoly'


# -- General configuration ---------------------------------------------------

root_doc = 'README'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser', 'sphinx_design']
myst_enable_extensions = ["colon_fence"]

# enable #section links: https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-header-anchors
myst_heading_anchors = 4

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    '.venv',
    'Thumbs.db',
    '.DS_Store',
    'publications/publications-combined.md',  # included in publications/journal_articles.md
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["theme.css"]

html_sidebars = {
    "**": [
        "navbar-logo.html",
        "gtranslate.html",
        "search-field.html",
        "sbt-sidebar-nav.html",
    ]
}

html_favicon = "_static/logo.png"
panels_add_bootstrap_css = False

html_sourcelink_suffix = ".md" # our sources are in markdown; but this only has an effect if "use_download_button": True

html_theme_options = {
    "logo": {
        "image_light": "_static/logo.png",
        "image_dark": "_static/logo.png",
        "alt_text": "NeuroPoly Lab",
    },
    "toc_title": "Page Contents",
    "search_bar_text": "Search...",

    "use_fullscreen_button": False,
    "use_edit_page_button": True,
    "use_download_button": False,
}

html_context = {
    "default_mode": "light",
    "github_user": "neuropoly",
    "github_repo": "neuro.polymtl.ca",
    "github_version": "master",
    "doc_path": "",
}

# On Github's UI, README.{md,txt,rst} are treated as front pages
# On every other web site, index.{html,php,py,....} are.
# To make both renders work, glue these two together by symlinks _build/html/**/index.html -> README.html
#
# Doing this here, in conf.py, is hacky, but it's what we've got for now.
# TODO: an even better solution would be to find/write a sphinx extension
#       that internally renamed README -> index during the writing, but only internally.
#       but unless we special-cased something hat would break the edit_page_button.
# TODO: Another solution is to host on that lets us use .htaccess files to choose README.md as index pages
# TODO: Another solution is to decide not to care about auto-rendering index pages on github.
for dir, dirs, fnames in os.walk("."): #XXX "." is possibly buggy? This isn't necessarily running from the source dir.
    dirs[:] = [d for d in dirs if d not in exclude_patterns] # prune the search
    for fname in fnames:
        if os.path.splitext(fname)[0] == "README":
            z = os.path.join("_build", "html", dir, "index.html")
            #html_extra_path.append(z)
            os.makedirs(os.path.dirname(z), exist_ok=True)
            if os.path.lexists(z):
                os.unlink(z)
            if not os.path.exists(
                     os.path.join(os.path.dirname(z),
                                  "README.html")): # don't create dangling symlinks;
                                                   # it annoyes Github Pages.
                os.symlink("README.html", z)


# -- Custom scripts ----------------------------------------------------------

import os
from pathlib import Path
import random
import requests
from subprocess import run
from textwrap import dedent
from urllib.parse import urlparse
from ghapi.all import GhApi
import pandas as pd

import yaml

from sphinx.application import Sphinx
from sphinx.util import logging

LOGGER = logging.getLogger("conf")

def build_gallery(app: Sphinx):
    # Build the gallery file
    LOGGER.info("building gallery...")
    grid_items = []
    projects = yaml.safe_load((Path(app.srcdir) / "gallery_software.yml").read_text())
    for item in projects:
        if not item.get("image"):
            item["image"] = "https://jupyterbook.org/_images/logo-square.svg"

        star_text = ""
        twitter_text = ""

        if "repository" in item.keys():
            try:
                url = urlparse(item["repository"])
                if url.netloc == "github.com":
                    _, org, repo = url.path.rstrip("/").split("/")
                    star_text = f"[![GitHub Repo stars](https://img.shields.io/github/stars/{org}/{repo}?label=&style=social)]({item['repository']})"
            except Exception as error:
                pass

        if "twitterName" in item.keys():
            twitter_text = f"[![Twitter Follow](https://img.shields.io/twitter/follow/{item['twitterName']}?label=&style=social)](https://twitter.com/{item['twitterName']})"

        grid_items.append(
            f"""\
        `````{{grid-item-card}}
        :text-align: center
        <div style="background-image: url('{item["image"]}'); background-size: contain; background-position: center; background-repeat: no-repeat; height: 100%; min-height: 150px;"></div>
        +++
        {" ".join(item["name"].split())}
        ````{{grid}} 2 2 2 2
        :margin: 0 0 0 0
        :padding: 0 0 0 0
        :gutter: 1
        ```{{grid-item}}
        :child-direction: row
        :child-align: start
        :class: sd-fs-5
        {{bdg-link-secondary}}`website <{item["website"]}>`
        ```
        ```{{grid-item}}
        :child-direction: row
        :child-align: end
        {twitter_text}
        {star_text}
        ```
        ````
        `````
        """
        )
    grid_items = "\n".join(grid_items)

# :column: text-center col-6 col-lg-4
# :card: +my-2
# :img-top-cls: w-75 m-auto p-2
# :body: d-none

    panels = f"""
``````{{grid}} 1 2 3 3
:gutter: 1 1 2 2
:class-container: full-width
{dedent(grid_items)}
``````
    """
    (Path(app.srcdir) / "gallery_software.txt").write_text(panels)

def build_publications(app: Sphinx, pagename, templatename, context, doctree):
    if pagename == "publications/articles":
        app.add_js_file("js/custom.js")
        app.add_css_file("css/custom.css")

def setup(app: Sphinx):
    app.connect("builder-inited", build_gallery)
    app.connect("html-page-context", build_publications)
