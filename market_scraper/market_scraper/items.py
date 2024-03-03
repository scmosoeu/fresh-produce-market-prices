# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MarketScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FreshProduceStats(scrapy.Item):
    information_date = scrapy.Field()
    commodity = scrapy.Field()
    total_value_sold = scrapy.Field()
    total_value_sold_mtd = scrapy.Field()
    total_quantity_sold = scrapy.Field()
    total_quantity_sold_mtd = scrapy.Field()
    total_kg_sold = scrapy.Field()
    total_kg_sold_mtd = scrapy.Field()
    quantity_available = scrapy.Field()


class ContainerStats(scrapy.Item):
    information_date = scrapy.Field()
    commodity = scrapy.Field()
    container = scrapy.Field()
    quantity_available = scrapy.Field()
    value_sold = scrapy.Field()
    value_sold_mtd = scrapy.Field()
    quantity_sold = scrapy.Field()
    quantity_sold_mtd = scrapy.Field()
    kg_sold = scrapy.Field()
    kg_sold_mtd = scrapy.Field()
    average_price_per_kg = scrapy.Field()


class ProductStats(scrapy.Item):
    information_date = scrapy.Field()
    commodity = scrapy.Field()
    container = scrapy.Field()
    unit_mass = scrapy.Field()
    product_combination = scrapy.Field()
    total_value_sold = scrapy.Field()
    total_quantity_sold = scrapy.Field()
    total_kg_sold = scrapy.Field()
    average = scrapy.Field()
    highest_price = scrapy.Field()
    average_price_per_kg = scrapy.Field()
    highest_price_per_kg = scrapy.Field()
