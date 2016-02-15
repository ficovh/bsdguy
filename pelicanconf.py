#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Francisco Valladolid'
SITENAME = u'BSDguy.org'
SITEURL = 'http://blog.bsdguy.org'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

BANNER = 'images/banner.jpg'

PROFILE_IMG_URL = u'http://www.gravatar.com/avatar/ab1e128805502b007dd29966ca93273c.png'
STATIC_PATHS = ['images', 'pages']
DISPLAY_PAGES_ON_MENU = 'True'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('NetBSD', 'http://www.netbsd.org/'),
          ('Perl','http://www.perl.org'),)

SOCIAL = (
            ('twitter', 'http://twitter.com/ficovh'),
            ('github', 'http://github.com/ficovh'),
            ('google+','https://plus.google.com/100483028055704960452')
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#THEME='pelican-bootstrap3'
BOOTSTRAP_THEME='flatly'

GITHUB_URL='http://github.com/ficovh'
DISQUS_SITENAME = "blogdefranciscovalladolid"
