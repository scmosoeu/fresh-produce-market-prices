# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MarketScraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        field_names = adapter.field_names()
        # Convert to lowercase
        string_fields = ['commodity', 'container', 'product_combination']
        for field_name in field_names:
            if field_name in string_fields:
                value = adapter.get(field_name)
                adapter[field_name] = value.lower()

        return item
