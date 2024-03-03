import scrapy
from market_scraper.items import ProductStats


class FreshProduceProductSpider(scrapy.Spider):
    name = "fresh_produce_product"
    allowed_domains = ["joburgmarket.co.za"]
    start_urls = [
        "https://joburgmarket.co.za/jhbmarket/jhb-market/dailyprices.php"]

    def parse(self, response):
        dropdown = response.css("select option:not(:first-child)")

        for commodity in dropdown:
            value = commodity.css("::attr(value)").get()

            page_url = f"https://joburgmarket.co.za/jhbmarket/jhb-market/dailyprices.php?commodity={value}&containerall=2"

            yield response.follow(page_url, callback=self.extract_product_stats)

    def extract_product_stats(self, response):

        information_date = response.css("#right2 p b ::text").get()
        fresh_produce = response.css(".statistics b::text").get()
        price_table = response.css("tbody tr")

        for market_data in price_table:

            product_stats = ProductStats()

            product_stats["information_date"] = information_date
            product_stats["commodity"] = fresh_produce,
            product_stats["container"] = market_data.css(
                "td:first-child ::text").get()
            product_stats["unit_mass"] = market_data.css(
                "td:nth-child(2) ::text").get()
            product_stats["product_combination"] = market_data.css(
                "td:nth-child(3) ::text").get()
            product_stats["total_value_sold"] = market_data.css(
                "td:nth-child(4) ::text").get()
            product_stats["total_quantity_sold"] = market_data.css(
                "td:nth-child(5) ::text").get()
            product_stats["total_kg_sold"] = market_data.css(
                "td:nth-child(6) ::text").get()
            product_stats["average"] = market_data.css(
                "td:nth-child(7) ::text").get()
            product_stats["highest_price"] = market_data.css(
                "td:nth-child(8) ::text").get()
            product_stats["average_price_per_kg"] = market_data.css(
                "td:nth-child(9) ::text").get()
            product_stats["highest_price_per_kg"] = market_data.css(
                "td:nth-child(10) ::text").get()

            yield product_stats
