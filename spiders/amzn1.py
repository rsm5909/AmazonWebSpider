# -*- coding: utf-8 -*-
import scrapy
from ..items import AmznItem
from datetime import datetime as dt
import time

class Amzn1Spider(scrapy.Spider):
    name = 'amzn1'
    page_number = 1
    result_number = 1
    allowed_domains = [
        'https://www.amazon.com',
        'www.amazon.com',
        'amazon.com'
    ]

    # 'https://www.amazon.com/Backpacking-Packs-Backpacks-Bags-Accessories/s?rh=n%3A10208054011&page=1'
    # 'https://www.amazon.com/s?k=hammock&i=sporting&page=2'
    start_urls = [
                    'https://www.amazon.com/s?k=hammock&i=sporting&rh=n%3A3375251%2Cn%3A3143614011&dc'
                  ]

    def parse(self, response):
        items = AmznItem()
        if len(response.xpath('//div[@data-asin and @data-index]')) > 0:
            targetArea = response.xpath('//div[@data-asin and @data-index]')
        else:
            targetArea = response.xpath('//li[@data-asin and @data-index]')
        print('TARGET AREA')

        for target in targetArea:
            print('RESULT NUMBER :::::::::::::::: {}'.format(Amzn1Spider.result_number))
            #ASIN
            if len(target.xpath('./@data-asin').extract())>0:
                product_asin = target.xpath('./@data-asin').extract()[0]
            else:
                product_asin = 'N/A'
            print('ASIN :::::::::::::::: {}'.format(product_asin))
            #TITLE
            if len(target.xpath('.//img[@alt]/@alt').extract())>0:
                product_title = target.xpath('.//img[@alt]/@alt').extract()[0]
            else:
                product_title = 'N/A'
            #RATING
            if len(target.xpath('.//span[@class="a-icon-alt"]')) > 0:
                product_rating = target.xpath('string(.//span[@class="a-icon-alt"])').extract()[0]
            else:
                product_rating = 'N/A'
            #ReviewCT
            if len(target.xpath('.//a[contains(@href,"#customerReviews")]/span')) > 0:
                product_review_ct = target.xpath('string(.//a[contains(@href,"#customerReviews")]/span)').extract()[0]
            elif len(target.xpath('.//a[contains(@href,"#customerReviews")]')) > 0:
                product_review_ct = target.xpath('string(.//a[contains(@href,"#customerReviews")])').extract()[0]
            else:
                product_review_ct = 'N/A'
            #PRICE
            if len(target.xpath('.//span[@class="a-offscreen"]').css('::text').extract()) > 0:
                product_price = target.xpath('.//span[@class="a-offscreen"]').css('::text').extract()[0]
            else:
                product_price = 'N/A'
            if len(target.xpath('.//img[@alt]/@src').extract()) > 0:
                product_img = target.xpath('.//img[@alt]/@src').extract()[0]
            else:
                product_img = 'N/A'

            time_stamp = dt.now()

            items['result_number'] = Amzn1Spider.result_number
            items['product_asin'] = product_asin
            items['product_title'] = product_title
            items['product_rating'] = product_rating
            items['product_review_ct'] = product_review_ct
            items['product_price'] = product_price
            items['product_img'] = product_img
            items['time_stamp'] = time_stamp
            Amzn1Spider.result_number += 1


            yield items
            print(items)

        next_page = Amzn1Spider.allowed_domains[0] + response.css('.a-last a::attr(href)').extract()[0]

        if Amzn1Spider.page_number < 34:
            Amzn1Spider.page_number +=1
            #time.sleep(.2)
            print("YIELDDDDDDDDDDDD")
            yield response.follow(next_page, callback=self.parse)
            print(next_page)
