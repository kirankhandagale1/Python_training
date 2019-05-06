import os,sys,xlrd
#workbook = xlrd.open_workbook(sys.argv[1])
#worksheet = workbook.sheet_by_index(0)	
workbook=open('kkk.xlsx','r')
k=workbook.read()
print(k)

'''count=0
for a in range(0,3):                                           
	s1=((worksheet.cell(0+count,0).value)) 				
	s2=((worksheet.cell(0+count,1).value))				
	s3=((worksheet.cell(0+count,2).value))
	count=count+1				
print (s1,s2,s3)		
'''
#print(worksheet)
