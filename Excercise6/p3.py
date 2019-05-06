#3. Write a Python program to remove newline characters from a file.


with open('k1','r') as f:
	with open('k2','w') as fw:
		for line in f:
			if line=='\n':
				pass
			else:		
				fw.write(line)









'''
f=open("k1","r+")
c=0
#while True:
ch=f.read()
c=c+1
print(c)
'''
