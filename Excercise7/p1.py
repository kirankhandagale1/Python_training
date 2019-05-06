# Write a Python class to implement pow(x, n)

def power(x,y):
	if (y==0):
		return 1
	elif ((y%2)==0):
		return (power(x,(y/2))*power(x,(y/2)))
	else :
	 	return (x*(power(x,(y/2))*power(x,(y/2))))

print("                    ")
print(".......Power of x \n")
print("                    ")
while True:
	x=int(input("Enter the value of x = "))
	y=int(input("Enter the value of y = "))
	ret=power(x,y)
	print("power of ",x," = ",ret)
