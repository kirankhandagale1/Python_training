#Arthamatic Calculator For Addition ,Substraction,Multiplication, Division and etc
import math
print("......Calcultor........")
while True:
	a=int(input("Enter the 1st value = "))        #first input for user datatype of integer
	b=int(input("Enter the 2nd value = "))        #second input for user datatype of integer
	print("..........1.addition.............")
	print("..........2.substraction.........")
	print("..........3.multiplicaton........")
	print("..........4.division.............")
	print("..........5.modulous........")
	print("..........6.floor_division.............")
	print("..........7.Exponitional.............")
	c=int(input("Eter your choice...\n"))
	if(c==1):
			r=a+b
			print("result = ",r)
	elif(c==2):
			r=a-b
			print("result = ",r)
	elif(c==3):
			r=a*b
			print("result = ",r)
	elif(c==4):
			r=a/b
			print("result = ",r)
	elif(c==5):
			r=a%b
			print("result = ",r)
	elif(c==6):
			r=a//b
			print("result = ",r)
	elif(c==7):
			r=a**b
			print("result = ",r)
	else:
			print("unknown choice..plz try again..")
