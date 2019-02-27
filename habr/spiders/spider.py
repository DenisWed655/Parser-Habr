import scrapy

from time import sleep

from scrapy.spiders import CrawlSpider
from random import choice
from habr.items import HabrItem 
from scrapy.loader import ItemLoader

class HabrSpider(scrapy.Spider):
	name = 'habr'
	allowed_domains = ['habr.com']
	start_urls = ['https://habr.com/ru/top/']

	def parse(self, response):
		
		for post_link in response.xpath("//h2[@class='post__title']"
										"/a[@class='post__title_link']/@href").extract():
			sleep(choice(range(3)))
			yield scrapy.Request(post_link, callback=self.parse_page)

		next_page = response.xpath("//a[@class='arrows-pagination__item-link arrows-pagination__item-link_next']/@href").extract_first()
		url_next_page = response.urljoin(next_page)
		yield scrapy.Request(url_next_page, callback=self.parse)



	def parse_page(self, response):
		page = ItemLoader(HabrItem())

		page.add_value('url_article', response.url)		
		try:
			author = response.xpath("//span[@class='user-info__nickname user-info__nickname_small']/text()").extract_first().strip()
			page.add_value('author', author)
		except:
			page.add_value('author', author)

		try:
			date = response.xpath("//span[@class='post__time']/text()").extract_first().strip()
			page.add_value('date', date)
		except:
			page.add_value('date', date)

		try:
			title = response.xpath("//span[@class='post__title-text']/text()").extract_first().strip()
			page.add_value('title', title)
		except:
			page.add_value('title', title)

		try:
			image_urls = response.xpath("//div[@class='post__body post__body_full']//img/@src").extract_first().strip()
			image_urls = image_urls.replace('habrastorage', 'hsto')
			page.add_value('image_urls', image_urls)
			page.add_value('images', image_urls)
		except:
			page.add_value('image_urls', '')
			page.add_value('images', '')


		try:
			voting = response.xpath("//span[@class='voting-wjt__counter voting-wjt__counter_positive  js-score']/@title").extract_first().strip()
			page.add_value('voting', voting)
		except:
			page.add_value('voting', voting)

		try:
			count_comments = response.xpath("//span[@id='comments_count']/text()").extract_first().strip()
			page.add_value('count_comments',  count_comments)
		except:
			page.add_value('count_comments', count_comments)
		
		yield page.load_item()