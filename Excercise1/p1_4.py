#find the given input as string|integer|float using type() and str|int|float|bool
while True:
	print("1.integer...")
	print("2.float.....")
	print("3.string....")
	print("4.bool.....")
	c=int(input("enter  your choice to given input= "))
	if(c==1):
		a=int(input("Enter the integer input = "))
		print("type of input = ",type(a),a)
	elif(c==2):
		b=float(input("Enter the float input = "))
		print("type of input = ",type(b),b)
	elif(c==3):
		b=str(input("Enter the string input = "))
		print("type of input =",type(b),b)
	elif(c==4):
		b=bool(input("Enter the bool input = "))
		print("type of input =",type(b),b)
	else:
		print("unknown choice...")
