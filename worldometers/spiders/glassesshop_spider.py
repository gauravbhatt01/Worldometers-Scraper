# coding : utf-8
import scrapy

class GlassesHopSpider(scrapy.Spider):

	name = 'glasseshop'
	allowed_domains = ['https://www.glassesshop.com/']
	start_urls = ['https://www.glassesshop.com/bestsellers']