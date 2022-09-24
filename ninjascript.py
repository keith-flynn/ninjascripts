import pandas as pd
import pyperclip

# import and save the SERIAL column from DT_export.csv
# the csv is the default format of the Export 2.0 tool
serial_scan = pd.read_csv('DT_export.csv', usecols=['SERIAL', 'SKU'])

# this printout is a visual failsafe to compare clipboard contents
serials_col = list(serial_scan['SERIAL'])
print(serials_col)

# convert column contents to iterated string on new lines
# this will be proper format to paste into work website form
clipboard = ''
for s in serial_scan.SERIAL:
    clipboard = clipboard + s + '\n'

#copy clipboard variable to OS (system agnostic) clipboard
pyperclip.copy(clipboard)
