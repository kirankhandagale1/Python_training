#  Write the program to print vowels and consonant letters from gnulinux.

while True:
	print("....print only constant and vowels...")
	input1=raw_input("Enter the char.....")
	if(input1>='0' and input1<='9'):
		print("costant no = ",input1)
	elif(input1=='a' or input1=='e' or input1=='i' or input1=='o' or input1=='u'):		print("These is vowels = ",input1)
	else:
		print("unkonown choice..")
