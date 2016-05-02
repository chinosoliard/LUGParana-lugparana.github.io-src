# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'LUG Paran\xe1'
SITENAME = u'LUG Paran\xe1'
SUBTITLE = u'Linux User Group Paraná'
SITEURL = ''

TIMEZONE = 'America/Argentina/Buenos_Aires'


PATH = 'content'
PAGE_PATH = 'pages'
ARTICLE_PATH = 'blog'
STATIC_PATHS = ['images/article','images/static','images/widgets','files']
ARTICLE_URL = 'blog/{category}/{date:%Y}/{date:%b}/{slug}.html' 
ARTICLE_SAVE_AS = 'blog/{category}/{date:%Y}/{date:%b}/{slug}.html' 

THEME = './theme' 


DEFAULT_LANG = u'es'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('envelope', 'mailto:lugparana@listas.usla.org.ar'),
          ('github', 'https://github.com/LUGParana'),
          ('facebook', 'https://www.facebook.com/groups/lugparana/'),
          ('google-plus', 'https://plus.google.com/u/0/communities/102117268282574409059'),
          ('youtube', 'http://www.youtube.com/channel/UCtzu8DvzTCHlEHse32Pl9hQ'),
          ('linkedin', 'https://www.linkedin.com/groups/8195477'))

DEFAULT_PAGINATION = True

TEMPLATE_PAGES = {'blog.html': 'blog.html'}
PAGINATED_DIRECT_TEMPLATES = ('blog',)
DIRECT_TEMPLATES = ('index', 'categories')
POST_LIMIT = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# THEME CONFIG
SLIDE1 = 'http://www.rugbychampagneweb.com/wp-content/uploads/2009/02/hj-mayorazgo-fachada-noche_1.jpg'
SLIDE2 = 'https://lh4.googleusercontent.com/-AgnPO5GPOio/VMpA6favO8I/AAAAAAAAASY/ysmBpQdzpVEkfyvhdZxy2SHgBZCTOBHJwCL0B/w757-h568-no/DSCN7039.JPG'
SLIDE3 = 'http://www.isletasnoticias.com.ar/wp-content/uploads/2013/06/PARANAAA.jpg'
SLIDE4 = 'http://www.rugbychampagneweb.com/wp-content/uploads/2011/03/13.jpg'
SLIDE5 = 'http://static.panoramio.com/photos/original/639011.jpg'
LOGO = '/images/static/logo.png'
HEADER_IMAGE = '/images/static/logo.png'
FAVICON = '/images/static/favicon.ico'
#ICON = ''
#SHORTCUT_ICON = ''
COPYRIGHT = '2016 &copy;'


#Items to descripe a work, "type", "cover-image link", "title", "descption", "link"
WORK_LIST = (('link', 'https://dl.dropboxusercontent.com/u/299446/BT3-Flat.png', 'BT3-Flat', 'A BT3 flat theme for pelican', 'https://github.com/KenMercusLai/plumage'),)
