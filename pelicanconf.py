# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'LUG Paran\xe1'
SITENAME = u'LUG Paran\xe1'
SITETITLE = u'LUG Paran\xe1'
SITEDESCRIPTION = 'Grupo de Usuarios de </br>Software Libre </br>de Paraná, Argentina'
SITELOGO = '/images/logo.png'
#FAVICON = SITEURL + '/images/favicon.ico'


#PATHS
PATH = 'content'            # General content path
PAGE_PATHS = ['pages']      # Pages path (Relative to PATH)
ARTICLE_PATHS = ['blog']    # Articles path (Relative to PATH)
STATIC_PATHS = ['images']   # Static path (Relatives to PATH) for static files
ARTICLE_URL = 'blog/{date:%Y}/'


SITEURL = '' 
TIMEZONE = 'America/Argentina/Buenos_Aires'
DEFAULT_LANG = u'es'
DEFAULT_PAGINATION = 5

DISPLAY_HOME_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

#THEME='theme'
THEME="lugparana-pelican-theme"
# Uncomment following line if you want document-relative URLs when developing        │blog/  pages/ 
#RELATIVE_URLS = True 

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/groups/lugparana/'),
          ('linkedin', 'https://www.linkedin.com/groups/8195477'),
          ('googleplus','https://plus.google.com/communities/102117268282574409059'),
          ('telegram','https://telegram.me/LUGParana'),
          ('twitter','https://twitter.com/lugparana'),
          ('youtube','http://www.youtube.com/channel/UCtzu8DvzTCHlEHse32Pl9hQ'),
          ('github','http://www.github.com/LugParana'),
          ('mail','mailto:lugparana@listas.usla.org.ar'),)
