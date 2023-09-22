import duckdb
import time

for sf in range (1,5):
    con = duckdb.connect(database=':memory:', read_only=False)

    start = time.time()
    con.sql(f"call dbgen(sf={sf});")
    end = time.time()
    print(f"dbgen sf={sf}: {end - start}")

    for i in range(1,23):
        start = time.time()
        con.sql(f"pragma tpch({i});")
        end = time.time()
        print(f"{i}: {end - start}")

    con.close()
