# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class AmznPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_tables()

    def create_connection(self):
        self.conn = sqlite3.connect("Hammocks.db")
        self.curr = self.conn.cursor()

    def create_tables(self):
        self.curr.execute("""DROP TABLE IF EXISTS hammocks_tb""")
        self.curr.execute("""create table hammocks_tb(
                        result_number text,
                        product_title text,
                        product_price text,
                        product_rating text,
                        product_review_ct text,
                        product_asin text,
                        product_img text,
                        time_stamp text
                        )""")


    def process_item(self, item, spider):
        self.store_db(item)
        print('ITEM :::::::::::::::: ')
        return item


    def store_db(self, item):
        self.curr.execute("""insert into hammocks_tb values (?,?,?,?,?,?,?,?)""",(
            item['result_number'],
            item['product_title'],
            item['product_price'],
            item['product_rating'],
            item['product_review_ct'],
            item['product_asin'],
            item['product_img'],
            item['time_stamp']
        ))
        self.conn.commit()
