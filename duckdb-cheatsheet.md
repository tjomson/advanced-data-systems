# Handy DuckDB things

## Building

### Build for debugging in python

Install Python dependency

`sudo dnf install python3-devel`

then

`sudo BUILD_PYTHON=1 make debug -j10`

Automatically adds entry to pip

### Attaching to python program

Add `launch.json` to duckdb repo

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Attach",
            "type": "cppdbg",
            "request": "attach",
            "program": "${workspaceFolder}/build/debug/duckdb",
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                },
                {
                    "description": "Set Disassembly Flavor to Intel",
                    "text": "-gdb-set disassembly-flavor intel",
                    "ignoreFailures": true
                }
            ]
        }
    ]
}
```

Run a python program, for example just open interactive in terminal `python3`.

Run debugger for duckdb. Choose the python-process

## Benchmarking

`install tpch;`

`load tpch;`

Scale factor is size of database (exponential). Calling dbgen again will not override previous db, but add to it.

`call dbgen(sf=1);`

View generated tables.

`call duckdb_tables();`

Run benchmark, replace the number with any 1-22 for tpc-h

`pragma tpch(1)`

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

