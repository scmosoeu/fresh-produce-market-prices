IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'extract_stats') AND type in (N'U'))
BEGIN
	CREATE TABLE extract_stats (
		information_date VARCHAR(30) NOT NULL
	);
END