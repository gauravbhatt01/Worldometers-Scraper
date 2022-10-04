# coding : utf-8
import scrapy

class SpecialOffersSpider(scrapy.Spider):
	name = 'special_offers'
	allowed_domains = ['www.tinydeal.com.hk']
	start_urls = ['https://www.tinydeal.com.hk/specials.html']

	def parse(self, response):
		for product in response.xpath("//ull[@class='productlisting-ul']/div/li"):
			yield {
				'title': product.xpath().get(),
				'url': response.urljoin().get(),
				'discounted_price': product.xpath().get(),
				'original_price' : product.xpath().get()
			}

		next_page = response.xpath("//a[@class='nextPage'/@href").get()

		if next_page:
			yield scrapy.Request(url=next_page, callback=self.parse)