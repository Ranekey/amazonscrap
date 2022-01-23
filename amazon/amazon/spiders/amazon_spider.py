import scrapy
from ..items import AmazonItem
from scrapy.loader import ItemLoader
import selectors
import logging

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [input("Entre l'url a scrapper ")]
    def parse(self, response):
        products = response.css('.sg-col-inner')
        links = products.css('.s-no-outline ::attr(href)').getall()
        for link in links :
            yield response.follow(link, callback=self.parseLink)

    def parseLink(self, response):
        items = AmazonItem()
        items['product_name'] = response.css('#productTitle::text').get()
        items['product_link'] = response.request.url
        items['product_price'] = response.css('.a-price-whole ::text').get(default = '0') +'.'+ response.css('.a-price-fraction ::text').get(default = '.0')
        items['product_numbersOfRating'] = response.css('#acrCustomerReviewText::text').get()
        items['product_rating'] = response.css('.a-icon-alt::text').get()

        
        yield  items

