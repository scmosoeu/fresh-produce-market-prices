# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


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

        # Convert Commodity and container to lowercase
        for field_name in ['commodity', 'container']:
            value = adapter.get(field_name)
            adapter[field_name] = value.lower()

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
        adapter['commodity'] = value[0].lower()

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
