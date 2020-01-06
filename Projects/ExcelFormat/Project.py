import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')
sheet1 = wb['Sheet1']
cell = sheet1['a1']
cell = sheet1.cell(1,1)
print(cell)