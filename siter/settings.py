# -*- coding: utf-8 -*-

# Scrapy settings for siter project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'siter'

SPIDER_MODULES = ['siter.spiders']
NEWSPIDER_MODULE = 'siter.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'siter (+http://www.yourdomain.com)'
LOG_LEVEL = "DEBUG"
LOG_FILE = "scrapy_log_last.log"

ROBOTSTXT_OBEY = True
DOWNLOADER_MIDDLEWARES = {
        #'scrapy.contrib.downloadermiddleware.robotstxt' : True
    }
