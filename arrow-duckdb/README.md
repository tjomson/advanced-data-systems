# Benchmark DuckDB vs pandas

Based on this: https://duckdb.org/2021/12/03/duck-arrow.html

Get data from: https://github.com/cwida/duckdb-data/releases/download/v1.0/lineitemsf1.snappy.parquet

DuckDB: 0.10748720169067383 sec
Pandas: 4.676659822463989 sec

DuckDB is able to multithread and perform query optimizations automatically.
