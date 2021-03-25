#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Francisco Valladolid'
SITENAME = u'BSDguy.org'
SITEURL = 'https://blog.bsdguy.org'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

#BANNER = 'images/banner.jpg'


COVER_IMG_URL = u'images/banner.jpg'
PROFILE_IMG_URL = u'http://www.gravatar.com/avatar/ab1e128805502b007dd29966ca93273c.png'

PATH = 'content'
STATIC_PATHS = ['images']
PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = 'True'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['gravatar']

THEME_STATIC_PATHS = ['static']
THEME_STATIC_DIR = 'theme'
THEME='./theme/pure'


# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python', 'http://python.org/'),
          ('NetBSD', 'http://www.netbsd.org/'),
          ('Perl','http://www.perl.org'),)

SOCIAL = (
            ('twitter', 'http://twitter.com/ficovh'),
            ('github', 'http://github.com/ficovh'),
            ('gitlab','https://gitlab.com/ficovh')
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

GITHUB_URL='http://github.com/ficovh'
DISQUS_SITENAME = "blogdefranciscovalladolid"
