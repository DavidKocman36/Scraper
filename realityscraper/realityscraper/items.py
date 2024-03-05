# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class RealityscraperItem(scrapy.Item):
    name = scrapy.Field()
    photos = scrapy.Field()
