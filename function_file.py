
import pandas as pd
import numpy as np
import db_dtypes

## Running queries

def readquery(filename):
    #Open and read the file and save it in a variable
    fd = open(filename, "r")
    sqlfile = fd.read()
    fd.close()
    return sqlfile

def runquery(queryfile):
    df = client.query(queryfile).to_dataframe()
    return df


## Cleaning dates for gsheets

def date_cols(dataset):
    dates = dataset.select_dtypes(include= ['datetimetz','dbdate','datetime','timedelta']).columns.tolist()
    return  dates

def dtobject(columnas):
    dtypes  =  pd.to_datetime(columnas,  format = '%Y-%m-%d')
    objects = dtypes.dt.strftime("%Y-%m-%d")
    return objects

def date_trans (dataset):
    dates = date_cols(dataset)
    for i in dataset.columns:
        if i in dates:
            dataset[i] = dtobject(dataset[i])
        else:
            dataset[i] = dataset[i]
    return dataset

## Cleaning numeric for gsheets

def numeric_cols(dataset):
    numerics = dataset.select_dtypes(include= np.number).columns.tolist()
    return numerics

def numeric_trans(dataset):
    numbers = numeric_cols(dataset)
    for i in dataset.columns:
        if i in numbers:
            dataset[i] = dataset[i].astype(float)
        else:
            dataset[i] = dataset[i]
    return dataset