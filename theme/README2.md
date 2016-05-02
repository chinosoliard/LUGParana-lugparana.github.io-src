* ARCHIVE_LIST `Changes the right hand article listing from a tree representation
to a list representation.`
* ARTICLES_HOME_PAGE `Switches the \ (index) page from the 'about me' page to
the list of articles.`

the following part is my config file:
==========

# Do not publish articles set in the future
WITH_FUTURE_DATES = False
TEMPLATE_PAGES = {'blog.html': 'blog.html'}
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# Feed generation is usually not desired when developing
FEED_RSS = 'feed/index.html'
FEED_ATOM = 'feed/atom/index.html'
FEED_ALL_RSS = False
FEED_ALL_ATOM = False
TRANSLATION_FEED_RSS = False
TRANSLATION_FEED_ATOM = False

# Blogroll
LINKS = (('Ken M. Lai\'s Note', 'http://kenmlai.blogspot.com'),
         ('Martian Z', 'http://blog.martianz.cn/'))

# Social widget
SOCIAL = (('google-plus', 'https://plus.google.com/+KenLaimercus'),
          ('linkedin', 'http://www.linkedin.com/in/kenmercuslai'),
          ('githuB', 'https://github.com/KenMercusLai'),
          ('envelope', 'mailto:ken.mercus.lai@gmail.com')
          )


DEFAULT_PAGINATION = True
PAGINATED_DIRECT_TEMPLATES = ('blog-index',)
DIRECT_TEMPLATES = ('categories', 'index', 'blog-index', 'blog')

POST_LIMIT = 3

# PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Formatting for dates

DEFAULT_DATE_FORMAT = ('%d/%b/%Y %a')

# Formatting for urls

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

# Plugins

PLUGIN_PATH = 'plugins'
PLUGINS = ['sitemap', 'neighbors', 'related_posts']


# Specify theme

# THEME = "theme/BT3-Flat"
THEME = "/Users/KenMercusLai/Documents/Projects/BT3-Flat"
# GOOGLE_SEARCH = '013542728820335073314:dcpel18vrey'
SWIFTYPE = ''
SITE_THUMBNAIL = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
SITE_THUMBNAIL_TEXT = 'Network Tsukkomi'
SITESUBTITLE = 'Not only about network'

DISQUS_SITENAME = 'networktsukkomime'
GOOGLE_ANALYTICS = ''
GOOGLE_ANALYTICS_DOMAIN = 'networktsukkomi.me'

### Plugin-specific settings

RELATED_POSTS_MAX = 20

# TODO: align default SITEMAP config to http://wordpress.org/extend/plugins/google-sitemap-generator/stats/
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


#===theme settings===========================

FAVICON = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
ICON = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
SHORTCUT_ICON = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
HEADER_IMAGE = 'https://dl.dropboxusercontent.com/u/299446/logo-invert.png'
BACKGROUND_IMAGE = 'http://images.nationalgeographic.com/wpf/media-live/photos/000/763/cache/egret-fog-reflection_76312_990x742.jpg'
# COPYRIGHT = '2015 &copy; All Rights Reserved.'
# Google fonts can be downloaded with
# https://neverpanic.de/downloads/code/2014-03-19-downloading-google-web-fonts-for-local-hosting-fetch.sh'
# Maybe you need to add missing mime types to your webserver configuration
# USER_FONT = '/theme/fonts/font.css'
# USER_BOOTSTRAP = '//maxcdn.bootstrapcdn.com/bootstrap/3.3.4'
# USER_FONTAWESOME = '//maxcdn.bootstrapcdn.com/font-awesome/4.3.0'
# USER_JQUERY = '//code.jquery.com/jquery-1.11.2.min.js'

