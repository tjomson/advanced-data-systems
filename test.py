import duckdb
import psutil

print("bruh")

duckdb.sql('CREATE TABLE test(i INTEGER)')
for process in psutil.process_iter(attrs=['pid', 'name']):
    if process.info['name'] == 'duckdb':
        duckdb_pid = process.info['pid']
        break

duckdb.sql('INSERT INTO test VALUES (42)')
duckdb.sql('from test').show()