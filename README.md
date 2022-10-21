# ninjascripts

## Automate very specific work tasks
---
## Project Overview:

**Code and Resources Used**
 - Python 3.9
   - _Pandas_
   - _Matplotlib_
   - _Easygui_
   - _Pyperclip_
 - From the command line, input `pip install -r requirements.txt` from within the project directory to add required modules.
---
### The basics
- Data is copied from DT_export.csv
- This is the default filename using the Export 2.0 tool
- Work website export tool automatically downloads to browser default destination
- Add ninjascript.py and DT_export.csv to same subdirectory
- Run "ninjascript.py"
- All serials are now copied to operating system clipboard (system agnostic)
- Paste in desired work website form
- Total number of machines by type are listed at the end
- Format: Model - Form factor - Processor - Total count

##### Form factors: **T**ower, **D**esktop, **S**mall, **U**ltrasmall, **M**ini