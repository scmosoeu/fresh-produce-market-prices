import scrapy
from market_scraper.items import PriceDate


class ExtractDateSpider(scrapy.Spider):
    name = "fresh_produce_date"
    allowed_domains = ["joburgmarket.co.za"]
    start_urls = [
        "https://joburgmarket.co.za/jhbmarket/jhb-market/dailyprices.php"]

    custom_settings = {
        'ITEM_PIPELINES': {
            "market_scraper.pipelines.SaveScrapingDateToMSSQLPipeline": 300
        }
    }

    def parse(self, response):
        information_date = response.css("#right2 p b ::text").get()

        price_date = PriceDate()

        price_date['information_date'] = information_date

        yield price_date
