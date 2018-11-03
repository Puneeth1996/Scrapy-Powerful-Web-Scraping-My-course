# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request, FormRequest


class TaxSpider(Spider):
    name = 'tax'
    allowed_domains = ['office.incometaxindia.gov.in']
    start_urls = ['http://office.incometaxindia.gov.in/']

    def parse(self, response):
        self.logger.info('All good')
        page = FormRequest(url='http://office.incometaxindia.gov.in/administration/Pages/tax-defaulters.aspx',formdata={'ctl00$SPWebPartManager1$g_1033a07f_ed99_4d49_bf9b_a310532378d8$btnSubmit': 'Search',
        	'ctl00$SPWebPartManager1$g_1033a07f_ed99_4d49_bf9b_a310532378d8$ctl00$txtPageNumber': '1'})
        tag = response.xpath('//*[@class="faqsno-heading taxdefaulter"]')
        name = tag.xpath('//span[1]/text()').extract()
        PAN = tag.xpath('//span[2]/text()').extract()
        ParentsName = tag.xpath('//span[3]/p/text()').extract()
        Tax = tag.xpath('//span[4]/text()').extract()
        URL = response.url
        yield {'name':name,
			   'PAN':PAN,
			   'ParentsName':ParentsName,
			   'Tax':Tax,
			   'URL':URL}

		
		
		
		
		
		
		
