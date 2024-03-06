CREATE TABLE IF NOT EXISTS daily_prices(
    information_date TEXT,
    commodity TEXT,
    total_value_sold FLOAT(2), 
    total_value_sold_mtd FLOAT(2),
    total_quantity_sold INT,
    total_quantity_sold_mtd INT,
    total_kg_sold FLOAT(2),
    total_kg_sold_mtd FLOAT(2),
    quantity_available INT 
)