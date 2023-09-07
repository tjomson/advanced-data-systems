# Handy DuckDB things

## Tooling

- Open db file:
`duckdb /data/myawesomedb.db`
- Attach db file if db is already open: `ATTACH DATABASE '/path/to/your/database.db' AS mydb;`
- Read data from csv: `CREATE TABLE netflix_top10 AS SELECT * FROM read_csv_auto('path/to/your/file.csv');`

## Adding to and creating tables

```sql
CREATE TABLE cities (
    name VARCHAR,
    lat  DECIMAL,
    lon  DECIMAL
);
```

```sql
INSERT INTO cities
VALUES ('San Francisco', -194.0, 53.0);
```

## Querying

Get distinct cities with rain and order

```sql
select distinct city from weather where prcp > 0.1 order by date, city;
```

Left join tables such that cities in weather are included even if they are not in cities table

```sql
select * from weather left outer join cities on weather.city = cities.name;
```

Get row where temp_lo is the highest

```sql
select * from weather where temp_lo = (select max(temp_lo) from weather);
```

Group by city. All shown columns must be part of group by or be aggregate function.
Having is like WHERE, but can be done with aggregate after group by

```sql
select city, max(temp_lo) as maximum from weather group by city having maximum > 40;
```

