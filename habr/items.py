# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HabrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field() 
    url_article = scrapy.Field()
    date = scrapy.Field() 
    title = scrapy.Field() 
    images = scrapy.Field() 
    image_urls = scrapy.Field() 
    voting = scrapy.Field()
    count_comments = scrapy.Field()
