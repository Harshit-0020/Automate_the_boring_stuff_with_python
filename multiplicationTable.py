#! python3
# multiplicationTable.py - returns NxN table in excel spreadsheet.

import sys
import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb.active

print("Reading the number...")
try:
    N = int(sys.argv[1])
    print('Preparing the spreadsheet...')

    for x in range(N + 1):
        for y in range(N + 1):
            isHeader = False
            if x == 0 and y == 0:
                n = ''
                isHeader = True

            elif x == 0:
                n = y
                isHeader = True

            elif y == 0:
                n = x
                isHeader = True

            else:
                n = x * y

            cell = sheet.cell(row=x + 1, column=y + 1)
            if isHeader:
                cell.font = Font(bold=True)
            cell.value = n
    print('Saving the spreadsheet...')
    wb.save('multiplicationTable.xlsx')
    print('Done!')

except Exception as e:
    print(e)
