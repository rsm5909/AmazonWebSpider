# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmznItem(scrapy.Item):
    # define the fields for your item here like:
    result_number = scrapy.Field()
    product_asin = scrapy.Field()
    product_title = scrapy.Field()
    product_rating = scrapy.Field()
    product_review_ct = scrapy.Field()
    product_price = scrapy.Field()
    product_img = scrapy.Field()
    time_stamp = scrapy.Field()
    pass
