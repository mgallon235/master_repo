import pandas as pd
import matplotlib.pyplot as plt

years = list(range(1800, 2023))

years1 = list(map(str, years))
print(years1)
####  Now that we created our list of possible values

df = pd.DataFrame({'colum':[1,2,3,4,5,6,7,8,9,10,11,12],'val':['1869', '1870', '1871', '1872', '1873', '1874', '1875', '1876', '1877','1877-90','1890 78','[1900]']})

## New dataframe
print(df)

df['val'] = df['val'].apply(lambda x: x.replace('-',''))
df['val'] = df['val'].apply(lambda x: x.replace('[','').replace(']',''))
df['val'] = df['val'].apply(lambda x: x.replace(' ',''))

subset =pd.Series(df.apply(lambda row: row['val'] not in years1, axis=1))

## create a subset with diff formats
df['is_date'] = subset

gg = df[df['is_date'] ==True]

gg['val'] = gg['val'].apply(lambda x: x.replace(' ','').replace('[','').replace(']','').replace('-','').strip(''))

gg['new'] = gg['val'].str[:4]
gg['last'] = gg['val'].str[-2:]

gg


gg2 = gg['val'].tolist

for i in gg2:


###  -----------------------------------
df2 = pd.read_csv('/Users/mikelgallo/repos/master_repo/python_brushup/datasets/books_pset.csv')

lista = df2['Place of Publication'].value_counts()

lista = df2['Place of Publication'].unique().tolist()

liston = lista.reset_index()
liston.describe()

liston[liston['index']!='London'].plot.scatter(x='index', y='Place of Publication')
plt.show()








