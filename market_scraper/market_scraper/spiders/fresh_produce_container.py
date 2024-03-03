import scrapy
from market_scraper.items import ContainerStats


class FreshProduceContainerSpider(scrapy.Spider):
    name = "fresh_produce_container"
    allowed_domains = ["joburgmarket.co.za"]
    start_urls = [
        "https://joburgmarket.co.za/jhbmarket/jhb-market/dailyprices.php"]

    def parse(self, response):
        dropdown = response.css("select option:not(:first-child)")

        for commodity in dropdown:
            value = commodity.css("::attr(value)").get()

            page_url = f"https://joburgmarket.co.za/jhbmarket/jhb-market/dailyprices.php?commodity={value}&containerall=1"

            yield scrapy.Request(
                url=page_url, callback=self.extract_container_stats
            )

    def extract_container_stats(self, response):

        information_date = response.css("#right2 p b ::text").get()
        fresh_produce = response.css(".statistics b::text").get()
        price_table = response.css("tbody tr")

        for market_data in price_table:

            yield {
                "information_date": information_date,
                "commodity": fresh_produce,
                "container": market_data.css(".tleft2 ::text").get(),
                "quantity_available": market_data.xpath("(.//td[@class='tleft'])[1]/text()").get(),
                "value_sold": market_data.xpath("(.//td[@class='tleft'])[2]/text()").get(),
                "value_sold_mtd": market_data.xpath("(.//td[@class='tleft'])[2]/br/following-sibling::text()").get(),
                "quantity_sold": market_data.xpath("(.//td[@class='tleft'])[3]/text()").get(),
                "quantity_sold_mtd": market_data.xpath("(.//td[@class='tleft'])[3]/br/following-sibling::text()").get(),
                "kg_sold": market_data.xpath("(.//td[@class='tleft'])[4]/text()").get(),
                "kg_sold_mtd": market_data.xpath("(.//td[@class='tleft'])[4]/br/following-sibling::text()").get(),
                "average_price_per_kg": market_data.css("td.tleft:last-child ::text").get()
            }
