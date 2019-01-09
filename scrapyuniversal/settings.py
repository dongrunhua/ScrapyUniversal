# -*- coding: utf-8 -*-

# Scrapy settings for scrapyuniversal project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'scrapyuniversal'

SPIDER_MODULES = ['scrapyuniversal.spiders']
NEWSPIDER_MODULE = 'scrapyuniversal.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapyuniversal (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# DEFAULT_REQUEST_HEADERS = {
#     "Cookie": 'device_id=ac21bafb8b6eba5842d1e7cf365e3e7a; _ga=GA1.2.1169553268.1534919150; s=dq1ach3l4k; __utma=1.1169553268.1534919150.1534929467.1534929467.1; __utmz=1.1534929467.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); webp=1; aliyungf_tc=AQAAAP3nB1MTqQsA3TBBcNTPstOwvMQH; xq_a_token=584d0cf8d5a5a9809761f2244d8d272bac729ed4; xq_a_token.sig=x0gT9jm6qnwd-ddLu66T3A8KiVA; xq_r_token=98f278457fc4e1e5eb0846e36a7296e642b8138a; xq_r_token.sig=2Uxv_DgYTcCjz7qx4j570JpNHIs; _gid=GA1.2.1960517093.1536132720; u=191536132719893; Hm_lvt_1db88642e346389874251b5a1eded6e3=1534919150,1534992703,1536132720,1536134388; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1536135021',
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
#
# }
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
#
# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

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
#    'scrapyuniversal.middlewares.ScrapyuniversalSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'scrapyuniversal.middlewares.ProxyMiddleware': 554,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
ITEM_PIPELINES = {

   #'scrapyuniversal.pipelines.TimePipeline': 298,
    #'scrapyuniversal.pipelines.HandleDate': 299,
   'scrapyuniversal.pipelines.MongoPipeline': 300,
}
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

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

#PROXY_URL = 'http://localhost:5555/random'

