# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import logging


class AmazonPipeline:

    def __init__(self):
        self.con = sqlite3.connect("amazonscrap.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute(""" CREATE TABLE IF NOT EXISTS amazon (
                    name TEXT PRIMARY KEY,
                    price REAL,
                    rating REAL,
                    numbersOfRating REAL,
                    link TEXT
                    
                    )""")

    def process_item(self, item, spider):
        """
        self.cur.executemany( INSERT OR IGNORE INTO amazon VALUES (?,?,?,?,?),
                            (item['product_name'], item['product_price'], item['product_rating'],
                            item['product_numbersOfRating'], item['product_link']))
        self.con.commit()
        """
        return item
