import pandas as pd
import re

# import and save the SKU column from DT_export.csv
# the csv is the default format of the Export 2.0 tool
data = pd.read_csv('DT_export.csv', usecols=['SERIAL', 'SKU'])

# create a list of the unique models in receiving format
models_scan = []
for i in data.SKU:
    if i not in models_scan:
        models_scan.append(i)

# iterate through models list removing receiving format
# and add total count
for elem in models_scan:
    model = re.sub(r"REC-", "", elem)
    print(model, data.SKU.value_counts()[elem])
