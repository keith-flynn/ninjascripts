import pandas as pd
import re
import pyperclip

# import and save the SERIAL, SKU columns from DT_export.csv
# the csv is the default format of the Export 2.0 tool
data = pd.read_csv('DT_export.csv', usecols=['SERIAL', 'SKU'])

# this printout is a visual failsafe to compare clipboard contents
serials_col = list(data['SERIAL'])
print(serials_col)

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

# convert column contents to iterated string on new lines
# this will be proper format to paste into work website form
clipboard = ''
for s in data.SERIAL:
    clipboard = clipboard + s + '\n'

#copy clipboard variable to OS (system agnostic) clipboard
pyperclip.copy(clipboard)
