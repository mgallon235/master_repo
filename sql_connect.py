import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
import json

# Importing credentials
with open('query_credentials.json') as f:
   parms = json.load(f)

con = psycopg2.connect(database= parms['database'],user= parms['user'],password=parms['password'],host=parms['host'],port= parms['port'])
sql = "SELECT * FROM public.sales_table;"
dat = sqlio.read_sql_query(sql, con)

dat


sql1 = "SELECT purchase_amount FROM public.sales_table where dates <= '2009-07-01';"
dat2 = sqlio.read_sql_query(sql1, con)

dat2

## When the output is 0 means that the connection is open
print(con.closed)

con.close()

## When the output is 1 means that the connection is closed
print(con.closed)