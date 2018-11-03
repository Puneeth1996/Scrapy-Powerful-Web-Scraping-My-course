# -*- coding: utf-8 -*-
import scrapy
import unicodedata

from XpathBot import settings
from XpathBot.items import ScraperItem

class generalscrapercss(scrapy.Spider):
    name = "XpathBot"
##    allowed_domains = settings.SETTINGS['allowed_domains']
    start_urls = [settings.SETTINGS['start_url']]


    download_delay = 2.0

    def parse(self, response):
        item = ScraperItem()
        if settings.SETTINGS['parseType'] == 'xpath':
            for sel in response.xpath(settings.CSS['main']):
                for name in sel.xpath(settings.CSS['name']).extract():
                        if name:
                                
                            item['name'] = unicode(name)
                            yield item
                        else:
                            print "Empty Item"
        else:
            if settings.SETTINGS['parseType'] == 'css':
                for sel in response.css(settings.CSS['main']):
                    for name in sel.css(settings.CSS['name']).extract():
                        if name:
                                
                            item['name'] = unicode(name)
                            yield item
                        else:
                            print "Empty Item"

    
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)
