IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'daily_prices') AND type in (N'U'))
BEGIN
	CREATE TABLE daily_prices (
		information_date VARCHAR(30) NOT NULL,
		commodity VARCHAR(30) NOT NULL,
		total_value_sold FLOAT NOT NULL, 
		total_value_sold_mtd FLOAT NOT NULL,
		total_quantity_sold INT NOT NULL,
		total_quantity_sold_mtd INT NOT NULL,
		total_kg_sold FLOAT NOT NULL,
		total_kg_sold_mtd FLOAT NOT NULL,
		quantity_available INT NOT NULL 
	);
END