# pindaPanda is noobest gamer on planet earth.

import scrapy

class AmazonSpider(scrapy.Spider):

    name = 'amazonia'
    allowed_domains = ['']
    start_urls = ['']

    def parse(self, response):
        pass