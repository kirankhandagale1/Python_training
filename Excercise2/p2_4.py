 #  Write the program to break the loop if user give n as input, if y continue
a=0
while True:
	c=str(raw_input("Enter your choice 'n'= break, 'y'=continue    "))
	if(c=='n'):
		print(" break ")
		break
	elif(c=='y'):
		print(" continue ")
		continue
