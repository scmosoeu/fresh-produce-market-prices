import scrapy


class FreshProduceScraperSpider(scrapy.Spider):
    name = "fresh_produce_scraper"
    allowed_domains = ["joburgmarket.co.za"]
    start_urls = ["https://joburgmarket.co.za/jhbmarket/jhb-market/dailyprices.php"]

    def parse(self, response):
        pass
