'''
a. structure (Tabular) : excel , mysql , postgresql, pl/sql , csv ..... 
b. unstructure (Non Tabular) : json / objective data 
'''
# for reading excel in our python program we have to use library : openpyxl

import openpyxl

# load workbook 
wb = openpyxl.load_workbook(r"C:\Users\Akash\Desktop\Datasets\Online Retail.xlsx")

sheet = wb.active

# until last row is not reached 

for i in sheet.iter_rows(values_only=True , max_row=5):
    print(i[5])