#1. Write a program to count no of lines in a text file.
f=open("k1","r")
c=0
while True:
	ch=f.read(1)
#for ch1 in f:	
	if(ch=='\n'):
			c=c+1
			print("total line of file == ",c)
			
