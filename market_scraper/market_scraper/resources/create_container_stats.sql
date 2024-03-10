IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'container_stats') AND type in (N'U'))
BEGIN
	CREATE TABLE container_stats (
		information_date VARCHAR(30) NOT NULL,
		commodity VARCHAR(30) NOT NULL,
		container VARCHAR(50) NOT NULL, 
		quantity_available INT NOT NULL,
		value_sold FLOAT NOT NULL,
		value_sold_mtd FLOAT NOT NULL,
		quantity_sold INT NOT NULL,
		quantity_sold_mtd INT NOT NULL,
		kg_sold FLOAT NOT NULL,
        kg_sold_mtd FLOAT NOT NULL,
		average_price_per_kg FLOAT NOT NULL  
	);
END