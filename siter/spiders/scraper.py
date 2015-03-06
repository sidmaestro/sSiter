# -*- coding: utf-8 -*-
import scrapy
from scrapy import log
import os
from scrapy.selector import Selector
from siter.items import SiterItem

class ScraperSpider(scrapy.Spider):
    name = "scraper"
#    allowed_domains = ["www.dmoz.org"]
    start_urls = (
        'http://www.dmoz.org/',
    )

    def __init__(self, fileName=None):
        print os.getcwd()
        print "sidharth ran a scraper"
        if fileName:
            old_startUrls = self.start_urls
            with open(fileName, 'r') as f:
                self.start_urls = [url.strip() for url in f.readlines()]
            if (len(self.start_urls) == 0):
                self.start_urls = old_startUrls

    def parse(self, response):
        self.log('CheckDisOut : A response from %s just arrived!' % response.url)
        filewrite = response.url.split("/")[-1]
        filewrite = filewrite.split(".")[-2]
        filewrite = "urls" + "/" + filewrite
        print filewrite
        if not os.path.exists(filewrite):
            os.makedirs(filewrite)
        htmlwrite = filewrite + "/" + 'html.txt'
        stuffwrite = filewrite + "/" + 'stuff.txt'
        with open(htmlwrite, 'wb') as f:
            f.write(response.xpath('/html').extract()[0].encode('ascii', 'ignore'))
##        hxs = Selector(response)
##        titles = hxs.xpath("//span[@class='pl']")
##        items = []
##        for titles in titles:
##            item = SiterItem()
##            item ["title"] = titles.xpath("a/text()").extract()
##            item ["link"] = titles.xpath("a/@href").extract()
##            items.append(item)
##            print item["title"]
##        return items
        siterItem = SiterItem()
        siterItem['link'] = response.url
        siterItem['allHtml'] = response.xpath('/html').extract()[0]
        tmpEx = response.xpath('/html/head/title').extract()[0]
        if len(tmpEx) > 0:
            siterItem['isTitlePresent'] = 'yes'
            siterItem['numCharsTitle'] = len(tmpEx)
        else:
            siterItem['isTitlePresent'] = 'no'
            siterItem['numCharsTitle'] = 0
        siterItem['numChars'] = len(siterItem['allHtml'])
        siterItem['numCharsBody'] = len(response.body)
        tmpEx = response.xpath('/html//a[@href]/@href').extract()
        siterItem['numLinks'] = len(tmpEx)
        if siterItem['allHtml'].find('categories') > -1 or siterItem['allHtml'].find('Categories') > -1:
            siterItem['hasCopyright'] = 'yes'
        else:
            siterItem['hasCopyright'] = 'no'
        tmpIm = response.xpath('//img').extract()
        siterItem['numImages'] = len(tmpIm)
        siterItem['numButtons'] = siterItem['allHtml'].count('button')
        siterItem['numForms'] = siterItem['allHtml'].count('form')
        siterItem['numMailTo'] = siterItem['allHtml'].count('@')
        with open(stuffwrite, 'wb') as f:
            f.write('link=' + str(siterItem['link']) + '\n')
            f.write('isTitlePresent=' + str(siterItem['isTitlePresent']) + '\n')
            f.write('numCharsTitle=' + str(siterItem['numCharsTitle']) + '\n')
            f.write('numCharsBody=' + str(siterItem['numCharsBody']) + '\n')
            f.write('numLinks=' + str(siterItem['numLinks']) + '\n')
            f.write('hasCopyright=' + str(siterItem['hasCopyright']) + '\n')
            f.write('numImages=' + str(siterItem['numImages']) + '\n')
            f.write('numButtons=' + str(siterItem['numButtons']) + '\n')
            f.write('numForms=' + str(siterItem['numForms']) + '\n')
            f.write('numMailTo=' + str(siterItem['numMailTo']) + '\n')
        
