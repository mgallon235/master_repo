import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas.io.sql as sqlio
import psycopg2
import json

# Importing credentials
with open('query_credentials.json') as f:
   parms = json.load(f)

conn = psycopg2.connect(database= parms['database'],user= parms['user'],
                       password=parms['password'],host=parms['host'],port= parms['port'])

sql = "SELECT * FROM public.iris;"
dat = sqlio.read_sql_query(sql, conn)

dat.head()
dat2 = dat.copy()

################################ calculating probabilitites

'''Preparing the data'''
################# Multiply all numeric columns by 10

numerics = dat2.select_dtypes(include= np.number).columns.to_list()

for i in dat2[numerics].columns:
   dat2[i] = dat2[i] * 10

dat2[numerics].info()
dat2[numerics] = dat2[numerics].applymap(int)

dat2[numerics].head()

############################### Calculiting probabilitites

## Sepal length
nums = dat2['sepal_length'].value_counts()
nums = nums.reset_index()
counts1 = dat2['sepal_length'].value_counts()/dat2['sepal_length'].count()
counts1 = counts1.reset_index().sort_values(by='index',ascending=True)

############################# Join series
## chinging column names
counts1.columns = ['sepal_length', 'prob']
nums.columns = ['sepal_length', 'count']


dataset = counts1.merge(nums, on='sepal_length',how='left')
dataset

## calculating expected value
expected_value = np.mean(counts1['prob'])


###### Plotting experiments
plt.hist(counts1['sepal_length'])
plt.vlines(np.mean('sepal_length'),colors = 'black',linestyles='--')
plt.show()

n = np.size(dat2['sepal_length'])
num_bins = np.sqrt(n)
counts, bins = np.histogram(x, bins=num_bins)
bins = bins[:-1] + (bins[1] - bins[0])/2
probs = counts/float(counts.sum())
print probs.sum() # 1.0
plt.bar(bins, probs, 1.0/num_bins)
plt.show()