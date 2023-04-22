import pandas as pd
import numpy as np
import pygsheets
print("hello world")

#  Connecting to Google Sheets
gc = pygsheets.authorize(service_file='/Users/mikelgallo/repos/master_repo/account_credentials.json')
sh = gc.open_by_key('19qpLpQQKfhSKIuQpQg00ZenFejWNBG9XBiiYZiRXrSM')

sh.title
sh.worksheets()


