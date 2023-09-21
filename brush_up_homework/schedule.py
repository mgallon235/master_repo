#%%
# Get daily stock data
from datetime import date, timedelta
import random
import numpy as np
import pandas as  pd
import time
import schedule
import os
import csv


#%%
path = '/Users/mikelgallo/repos/master_repo/Python_practice'
## Create new file and save it in repository where will be updated
for root, dirs, files in os.walk(path):
    # iterating over the files in exercise 
    for file in files:
        if not file.startswith('schedule_stock'):
            continue
        with open(f'{path}/{file}','a') as f:
            data = generate_data()
            data = data.to_csv()
            writer_obj = f.writer(data, delimiter=",")
            f.write(file.add(data))
            print(file)

        with open('event.csv', 'a') as f_object:
 
    # Pass the file object and a list
    # of column names to DictWriter()
    # You will get a object of DictWriter
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
 
    # Pass the dictionary as an argument to the Writerow()
    dictwriter_object.writerow(dict)
 
    # Close the file object
    f_object.close()
# 
#%%

## Add to new dataframe (csv)
# df=df.add()

# df.to_csv('')

#%%
# Generate list of stocks
def generate_data():
    liston = np.random.randint(30,45,10).tolist()
     # Generate  current date
    my_date=date.today().strftime("%Y-%m-%d")
    # replicate date by the length of the list
    dates = []
    for i in range(len(my_date)):
        dates.append(my_date)
        print(dates)

    # Create dictionary with values and dates
    diction = {'date':dates,'stock':liston}
    return pd.DataFrame(diction)

#%%
## Generate a dataframe
df = pd.DataFrame(diction)

df



#%%

df = pd.DataFrame({'colum':[1,2,3,4,5,7,7,7,7],'val':[1,2,3,4,5,7,7,7,7]})

df.duplicated().sum()

df['subset'][df['subset'].index.duplicated()].count()

df.describe()

df = random.randint(1800,1900)