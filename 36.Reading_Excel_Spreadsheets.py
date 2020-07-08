import openpyxl
import os
os.chdir('/home/zabex/Documents/automate_online-materials/')#get to the right directory

workbook1 = openpyxl.load_workbook('example.xlsx') # open the workbook
sheet1 = workbook1.get_sheet_by_name('Sheet1')#select the worksheet you want if you know it

#if you dont know the name of the sheet you want use this to return all the sheet names in the workbook
print(workbook1.get_sheet_names())

cell1 = sheet1['A1'] #once you have the sheet, make a variable for the cells inside it
print(cell1.value)
#You dont actually need to put the cell into a variable, you can just call the print function on it
print(sheet1['B2'].value)
# you can also use the cell method to call the data from the cells
print(sheet1.cell(row=1, column=3).value)