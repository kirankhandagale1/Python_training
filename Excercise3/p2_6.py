'''  Write a Python program to check the validity of password input by users. A list of validations are,
 At least 1 letter between [a-z] and 1 letter between [A-Z].
 At least 1 number between [0-9].
 At least 1 character from [$#@].
 Minimum length 6 characters.
 Maximum length 16 characters. '''
password=str(raw_input("Enter the password "))
password=' '
while True:
	for i in range(0,10):
		if(passord[i]>='a' and password[i]<='z'):
				print("vaid")
		elif(passord[i]>='0' and password[i]<='9'):
				print("vaid")
		elif(passord[i]>='0' and password[i]<='9'):













'''input1=str(input("Enter the password   "))
input1=[]
for i in range(0,10):
	if((len(input1)>=6 and len(input1)<=16)): 
					print("correct...")
#and (input1[i]>=0 and input1[i]<=9) and (input1[i]>='a' and input1[i]<='z') and (input1[i]>='A'and input1<='Z')):
'''
