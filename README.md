# fresh-produce-market-prices

Scrape fresh produce data from [johannesburg market website](https://joburgmarket.co.za/jhbmarket/jhb-market/dailyprices.php?) using a [scrapy](https://docs.scrapy.org/en/latest/) framework. The scrapped data is processed and stored in a database, for this project the database used is MS SQL Server.


## Setup

Create a virtual environment

```bash
python -m venv name
```

Within your virtual environment

```bash
pip install scrapy 
pip install ipython
```

The *ipython* installation enables easier access to scrapy inside the terminal to test the **css** and **xpath** connections to HTML elements within a website.

Inside the **scrapy.cfg** below the [settings] section, insert:

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
scrapy genspider spidername mydomain.com
```

Run a spider

```bash
scrapy crawl spider_name
```

Run a spider and write to file

```bash
scrapy crawl spider_name -O filename.extension
```

## Scrapy File System

### items.py

Define the fields in your data

### pipelines.py

For data processing, validation, writing to a database

For data processing, there are two options:

1. Serializer (inserted in **items.py**)
2. Pipelines

### Settings.py

Define the **ITEM_PIPELINE** which will be responsible for the order at which the script runs. This could include data processing, connecting to a database, writting to a database, etc...

**FEEDS** section can be created when you want to create an output file of scrapped data. This could be in a .json, or .csv format.


For multiple scrappers following different pipelines, a **custom_settings** inside the spider can be created to assign each spider to a different pipeline. The **custom_settings** inside your spider can be used to overwrite settings

## Database Connection

The database used to store the scrapped data is MS SQL Server, hence the *pyodbc* module was installed. 

```bash
pip install pyodbc
```
