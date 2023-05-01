import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
import json
from sqlalchemy import create_engine
from pydataset import data


# Importing credentials
with open('query_credentials.json') as f:
   parms = json.load(f)

#creating a connection
conn_string = parms['connection_string']

db = create_engine(conn_string)
conn1 = db.connect()

conn = psycopg2.connect(database= parms['database'],user= parms['user'],
                       password=parms['password'],host=parms['host'],port= parms['port'])


# import the csv file to create a dataframe
#data = pd.read_csv("Sales.csv")
df = data('iris')


########## Creating a cursor object to excecute changes in the database:
conn.autocommit = True
cur = conn.cursor()  

# drop table if it already exists
cur.execute('drop table if exists iris')

## Collecting data columns from iris
df.info()

# change naming for table
df.columns = df.columns.str.replace(".", "_")
df.columns = df.columns.str.lower()


# creating new table
sql = '''CREATE TABLE iris(sepal_length float(24),\
sepal_width float(24), petal_length float(24), petal_width float(24),\
species char(45));'''

# excecuting query into the dbs
cur.execute(sql)
 
# converting data to sql
df.to_sql('iris', con = conn1, if_exists='replace')

######################### Finish importing process

## Running query to validate data:
sql1 = "SELECT * FROM public.iris limit 100;"
dat2 = sqlio.read_sql_query(sql1, conn)

#### Commiting changes and closing connection

conn.commit()

## closing connection
# 1 = disconnected , 0 = connected
cur.close()
cur.closed

# 1 = disconnected , 0 = connected
conn.close()
conn.closed

# 1 = disconnected , 0 = connected
conn1.close()
conn1.closed