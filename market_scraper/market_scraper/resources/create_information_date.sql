IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'extract_date') AND type in (N'U'))
BEGIN
	CREATE TABLE extract_date (
		information_date VARCHAR(30) NOT NULL
	);
END