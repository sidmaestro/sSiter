# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SiterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    link = scrapy.Field()
    allHtml = scrapy.Field()
    isTitlePresent = scrapy.Field()
    numChars = scrapy.Field()
    numCharsTitle = scrapy.Field()
    numCharsBody = scrapy.Field()
    numHtmlTags = scrapy.Field()
    numLinks = scrapy.Field()
    numSameDomainLinks = scrapy.Field()
    numOutDomainLinks = scrapy.Field()
    numImages = scrapy.Field()
    hasCopyright = scrapy.Field()
    hasRobotstxt = scrapy.Field()
    numButtons = scrapy.Field()
    numForms = scrapy.Field()
    numSpecialChars = scrapy.Field()
    numNumbers = scrapy.Field()
    numDiffFonts = scrapy.Field()
    numDiffFontSizes = scrapy.Field()
    numWords = scrapy.Field()
    numMailTo = scrapy.Field()
    hasXml = scrapy.Field()
    
