# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .database_settings.config import load_config
import os

import pyodbc


class FreshProduceScraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # Convert Commodity to lowercase
        value = adapter.get('commodity')
        adapter['commodity'] = value.lower()

        # Create float fields
        float_fields = [
            'total_value_sold',
            'total_value_sold_mtd',
            'total_kg_sold',
            'total_kg_sold_mtd'
        ]

        for float_field in float_fields:
            value = adapter.get(float_field)
            if '_mtd' in float_field:
                value = value.split(':')[1].strip()
            value = value.replace('R', '').replace(',', '')
            adapter[float_field] = float(value)

        # Create int fields
        int_fields = [
            'total_quantity_sold',
            'total_quantity_sold_mtd',
            'quantity_available'
        ]

        for int_field in int_fields:
            value = adapter.get(int_field)
            if '_mtd' in int_field:
                value = value.split(':')[1].strip()
            value = value.replace(',', '')
            adapter[int_field] = int(value)

        return item


class FreshProduceContainerPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # Convert Commodity  lowercase
        value = adapter.get('commodity')
        if isinstance(value, tuple):
            value = value[0].lower()
        else:
            value = value.lower()
        adapter['commodity'] = value

        # Convert container to lowercase
        value = adapter.get('container')
        adapter['container'] = value.lower()

        # Create float fields
        float_fields = [
            'value_sold',
            'value_sold_mtd',
            'kg_sold',
            'kg_sold_mtd',
            'average_price_per_kg'
        ]

        for float_field in float_fields:
            value = adapter.get(float_field)
            if '_mtd' in float_field:
                value = value.split(':')[1].strip()
            value = value.replace('R', '').replace(',', '')
            adapter[float_field] = float(value)

        # Create int fields
        int_fields = [
            'quantity_sold',
            'quantity_sold_mtd',
            'quantity_available'
        ]

        for int_field in int_fields:
            value = adapter.get(int_field)
            if '_mtd' in int_field:
                value = value.split(':')[1].strip()
            value = value.replace(',', '')
            adapter[int_field] = int(float(value))

        return item


class FreshProduceProductPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # Convert Commodity  lowercase
        value = adapter.get('commodity')
        if isinstance(value, tuple):
            value = value[0].lower()
        else:
            value = value.lower()
        adapter['commodity'] = value

        # Convert container and product_combination to lowercase
        for field_name in ['container', 'product_combination']:
            value = adapter.get(field_name)
            adapter[field_name] = value.lower()

        # Create float fields
        float_fields = [
            'unit_mass',
            'total_value_sold',
            'total_kg_sold',
            'average',
            'highest_price',
            'average_price_per_kg',
            'highest_price_per_kg'
        ]

        for float_field in float_fields:
            value = adapter.get(float_field)
            value = value.replace('R', '').replace(',', '')
            adapter[float_field] = float(value)

        # Convert total_quantity_sold to int fields
        value = adapter.get('total_quantity_sold')
        value = value.replace(',', '')
        adapter['total_quantity_sold'] = int(float(value))

        return item


class SaveDailyPricesToMSSQLPipeline:

    def __init__(self) -> None:
        config = load_config()
        self.conn = pyodbc.connect(**config)

        self.cur = self.conn.cursor()
        self.cwd = os.getcwd().replace('\\', '/')

        with open(self.cwd + '/market_scraper/resources/create_daily_prices.sql', 'r') as sql_script:

            self.cur.execute(sql_script.read())

    def process_item(self, item, spider):
        with open(self.cwd + '/market_scraper/resources/insert_daily_prices.sql', 'r') as sql_script:
            script = sql_script.read()
            self.cur.execute(
                script.format(
                    item['information_date'],
                    item['commodity'],
                    item['total_value_sold'],
                    item['total_value_sold_mtd'],
                    item['total_quantity_sold'],
                    item['total_quantity_sold_mtd'],
                    item['total_kg_sold'],
                    item['total_kg_sold_mtd'],
                    item['quantity_available']
                )
            )

            # Execute insert of data into database
            self.conn.commit()

            return item

    def close_spider(self, spider):

        # Close cursor & connection to database
        self.conn.close()
        self.cur.close()


class SaveContainerStatsToMSSQLPipeline:

    def __init__(self) -> None:
        config = load_config()
        self.conn = pyodbc.connect(**config)

        self.cur = self.conn.cursor()
        self.cwd = os.getcwd().replace('\\', '/')

        with open(self.cwd + '/market_scraper/resources/create_container_stats.sql', 'r') as sql_script:

            self.cur.execute(sql_script.read())

    def process_item(self, item, spider):
        with open(self.cwd + '/market_scraper/resources/insert_container_stats.sql', 'r') as sql_script:
            script = sql_script.read()
            self.cur.execute(
                script.format(
                    item['information_date'],
                    item['commodity'],
                    item['container'],
                    item['quantity_available'],
                    item['value_sold'],
                    item['value_sold_mtd'],
                    item['quantity_sold'],
                    item['quantity_sold_mtd'],
                    item['kg_sold'],
                    item['kg_sold_mtd'],
                    item['average_price_per_kg']
                )
            )

            # Execute insert of data into database
            self.conn.commit()

            return item

    def close_spider(self, spider):

        # Close cursor & connection to database
        self.conn.close()
        self.cur.close()
