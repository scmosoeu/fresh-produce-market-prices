IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'product_stats') AND type in (N'U'))
BEGIN
	CREATE TABLE product_stats (
		information_date VARCHAR(30) NOT NULL,
		commodity VARCHAR(30) NOT NULL,
		container VARCHAR(50) NOT NULL,
        unit_mass VARCHAR(10) NOT NULL, 
        product_combination VARCHAR(50) NOT NULL,
		total_value_sold FLOAT NOT NULL,
		total_quantity_sold INT NOT NULL,
		total_kg_sold FLOAT NOT NULL,
		average FLOAT NOT NULL,
		highest_price FLOAT NOT NULL,
        average_price_per_kg FLOAT NOT NULL,
		highest_price_per_kg FLOAT NOT NULL  
	);
END