# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
def replace_virgule(value):
    return value.replace(',','.').strip()
def clean_rating(value):
    if ',' in value: return replace_virgule(value[:3])
    return value[0]
def clean_numberrating(value):
    return value.replace('\xa0', '').strip()
def no_price(value):
    if value is None:
        return '0'
    return value
def link(value):
    return 'amazon.fr'+value

def clean_name(value):
    value = value[value.index("r") + 2:]
    return value[:value.index('/')]


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field(input_processor = MapCompose(), output_proccessor = TakeFirst())
    product_price = scrapy.Field(input_processor = MapCompose(no_price,replace_virgule ), output_proccessor = TakeFirst())
    product_rating = scrapy.Field(input_processor = MapCompose(clean_rating), output_proccessor = TakeFirst())
    #product_imgLink = scrapy.Field(input_processor = MapCompose(), output_proccessor = TakeFirst())
    product_numbersOfRating = scrapy.Field(input_processor = MapCompose(clean_numberrating), output_proccessor = TakeFirst() )
    product_link = scrapy.Field(input_processor = MapCompose(), output_proccessor = TakeFirst())
