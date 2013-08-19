#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kearney Liu'
SITENAME = u"Kearney Liu's Home"
SITEURL = 'htpp://www.kearneyliu.com'
GITHUB_URL = 'https://github.com/kearneyliu'
DISQUS_SITENAME = u"kearneyliu"
GOOGLE_ANALYTICS = 'UA-43258597-1'

ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

RELATIVE_URLS = True
DEFAULT_PAGINATION = 5

TIMEZONE = 'Asia/Shanghai'

THEME = 'tuxlite_tbs'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS =  (('Google', 'https://www.google.com/ncr'),
          ('Python.org', 'http://python.org/'),
          
          )

# Social widget
SOCIAL = (('Github', 'https://github.com/kearneyliu'),
          ('Weibo', 'http://weibo.com/liukaiyukearney'),
          ('Facebook', 'https://www.facebook.com/profile.php?id=100004019769371'),
          ('RenRen','http://www.renren.com/250927132/profile'),
          )

PLUGIN_PATH = u"pelican-plugins"
PLUGINS = ["sitemap"]
SITEMAP = {
            "format": "xml",
             "priorities":
            {
                "articles": 0.7,
                "indexes": 0.5,
                "pages": 0.3,
            },
            "changefreqs": 
            {
                "articles": "monthly",
                "indexes": "daily",
                "pages": "monthly",
            }
          }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
