#write a pgm to given range between odd no..

a=int(input("Enter the range a = "))
b=int(input("Enter the range b = "))
for a in range(a,b):
	if(a%2!=0):
		print(a)
	else:
		continue
