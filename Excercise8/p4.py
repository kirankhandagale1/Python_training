
import xlrd
from xlrd import open_workbook, cellname

book = open('kkk.xlsx', 'r')
sheet = book.sheet_by_index(1)

dict_list = []

for row_index in range(sheet.nrows):
    for col_index in range(sheet.ncols):
        d = {}
        	for i in sheet.row(0):
           		d[str(i)] = sheet.cell(row_index, col_index).value
         		  dlist.append(d)

