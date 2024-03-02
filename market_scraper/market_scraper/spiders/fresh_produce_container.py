import scrapy


class FreshProduceContainerSpider(scrapy.Spider):
    name = "fresh_produce_container"
    allowed_domains = ["joburgmarket.co.za"]
    start_urls = ["https://joburgmarket.co.za/jhbmarket/jhb-market/dailyprices.php"]

    def parse(self, response):
        pass
