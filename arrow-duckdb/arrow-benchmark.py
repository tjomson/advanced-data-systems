import pyarrow.parquet as pq
import pyarrow as pa
import pyarrow.dataset as ds
import duckdb
import pandas as pd
import time


# DuckDB

lineitem = pq.read_table('lineitemsf1.snappy.parquet')
con = duckdb.connect()
start = time.time()
# Transforms Query Result from DuckDB to Arrow Table
con.execute("""SELECT sum(l_extendedprice * l_discount) AS revenue
                FROM
                lineitem;""").fetch_arrow_table()
end = time.time()

print(f"DuckDB: {end-start} sec")

# Pandas

arrow_table = pq.read_table('lineitemsf1.snappy.parquet')

start = time.time()
# Converts an Arrow table to a Dataframe
df = arrow_table.to_pandas()
# Runs aggregation
res =  pd.DataFrame({'sum': [(df.l_extendedprice * df.l_discount).sum()]})

# Creates an Arrow Table from a Dataframe
new_table = pa.Table.from_pandas(res)
end = time.time()

print(f"pandas: {end-start} sec")