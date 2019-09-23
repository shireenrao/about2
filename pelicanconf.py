#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Srini"
SITENAME = "Boston Python"
SITEURL = ""
SITESUBTITLE = "The Boston-area Python user group"

PATH = "content"
OUTPUT_PATH = 'docs/'

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

PLUGINS = ['assets']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "theme/simple"

STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DEFAULT_PAGINATION = False

FAVICON = "images/favicon.ico"

from datetime import datetime

YEAR = datetime.now().strftime("%Y")

