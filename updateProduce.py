#! python3
# updateProduce.py - updates the price of the produce in the given excel file.


import openpyxl
import os

os.chdir(r'C:\Coding\Automate the boring stuff with python\All files used in this book\automate_online-materials')
wb = openpyxl.load_workbook('produceSales.xlsx')
os.chdir(r'C:\Coding\Automate the boring stuff with python\Automating Tasks\updating spreadsheet')
sheet = wb['Sheet']

# The produce types and their updated prices.
priceUpdates = {'Garlic': 3.07,
                'Celery': 1.19,
                'Lemon': 1.27
}

print("Updating the prices...")
# Skip the first row.
for row in range(2, sheet.max_row+1):
    produceName = sheet['A'+str(row)].value
    if produceName in priceUpdates:
        sheet['B'+str(row)].value = priceUpdates[produceName]


wb.save('updatedProduceSales.xlsx')
