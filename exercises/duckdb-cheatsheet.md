# Handy DuckDB things

- Open db file:
`duckdb /data/myawesomedb.db`
- Attach db file if db is already open: `ATTACH DATABASE '/path/to/your/database.db' AS mydb;`
- Read data from csv: `CREATE TABLE netflix_top10 AS SELECT * FROM read_csv_auto('path/to/your/file.csv');`