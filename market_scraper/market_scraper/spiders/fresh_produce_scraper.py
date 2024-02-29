import scrapy


class FreshProduceScraperSpider(scrapy.Spider):
    name = "fresh_produce_scraper"
    allowed_domains = ["joburgmarket.co.za"]
    start_urls = [
        "https://joburgmarket.co.za/jhbmarket/jhb-market/dailyprices.php"]

    def parse(self, response):
        information_date = response.css("#right2 p b ::text").get()

        price_table = response.css("tbody tr")

        for market_data in price_table:

            yield {
                "commodity": market_data.css("td.tleft2 ::text").get(),
                "total_value_sold": market_data.xpath("(.//td[@class='tleft'])[1]/text()").get(),
                "total_value_sold_mtd": market_data.xpath("(.//td/br)[1]/following-sibling::text()").get(),
                "total_quantity_sold": market_data.xpath("(.//td[@class='tleft'])[2]/text()").get(),
                "total_quantity_sold_mtd": market_data.xpath("(.//td/br)[2]/following-sibling::text()").get(),
                "total_kg_sold": market_data.xpath("(.//td[@class='tleft'])[3]/text()").get(),
                "total_kg_sold_mtd": market_data.xpath("(.//td/br)[3]/following-sibling::text()").get(),
                "quantity_available": market_data.css("td:last-child.tleft ::text").get()
            }
