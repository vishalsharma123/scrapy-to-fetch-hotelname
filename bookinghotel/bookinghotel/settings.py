# -*- coding: utf-8 -*-

# Scrapy settings for bookinghotel project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import getpass

import datetime
current_user = getpass.getuser()
BOT_NAME = 'bookinghotel'
TEM_PIPELINES= {

        'bookinghotel.pipelines.BookinghotelPipeline': 300,



    }

SPIDER_MODULES = ['bookinghotel.spiders']
NEWSPIDER_MODULE = 'bookinghotel.spiders'
start_url="https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaGyIAQGYAS7CAQN4MTHIAQzYAQPoAQGSAgF5qAID&sid=4b923040ec8f80543bf75935475ba9ea&sb=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaGyIAQGYAS7CAQN4MTHIAQzYAQPoAQGSAgF5qAID%3Bsid%3D4b923040ec8f80543bf75935475ba9ea%3Bsb_price_type%3Dtotal%26%3B&ss=Los+Angeles&ssne=Los+Angeles&ssne_untouched=Los+Angeles&dest_id=20014181&dest_type=city&checkin_monthday=11&checkin_month=6&checkin_year=2017&checkout_monthday=18&checkout_month=6&checkout_year=2017&room1=A%2CA&group_adults=2&group_children=0&no_rooms=1"
FILES_STORE = '/home/'+current_user+'/bookinghotel/downloads'+str(datetime.date.today())
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bookinghotel (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bookinghotel.middlewares.BookinghotelSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'bookinghotel.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'bookinghotel.pipelines.BookinghotelPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
