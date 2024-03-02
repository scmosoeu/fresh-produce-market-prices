# fresh-produce-market-prices

Scrape fresh produce data from johannesburg market website

Create a virtual environment

```bash
python -m venv name
```

Within your virtual environment

```bash
pip install scrapy 
pip install ipython
```

Inside the **scrapy.cfg** below the [settings]
insert:

```bash
shell = ipython
```

Create a scrapy project

```bash
scrapy startproject project_name [project_dir]
```

Create a crawler

```bash
cd project_dir
scrapy genspider mydomain.com
```

Run a spider

```bash
scrapy crawl spider_name
```


For data processing, there are two options:

1. Serializer (inserted in **items.py**)
2. Pipelines

After creating Pipelines, uncomment the ITEM_PIPELINE section in settings.py

Saving data:
Create FEEDS in the settings.py file to create an output file format

custom_settings insider your spider can be used to overwrite settings

pip install mysql mysql-connector-python
