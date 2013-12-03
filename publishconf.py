#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

#SITEURL = ''
#RELATIVE_URLS = False

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

#DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

AUTHOR = u'TehLug'
SITENAME = u'Python The Right Way'
SITEURL = 'http://k1-hedayati.github.io/python-the-right-way'

TIMEZONE = 'Asia/Tehran'

DEFAULT_LANG = u'fa'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_CATEGORY = u'uncategorised'
THEME = "themes/zurb"
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_DATE = 'fs'
PLUGIN_PATH = 'plugins'
PLUGINS = ['sort_by_slug']
SUMMARY_MAX_LENGTH = None
