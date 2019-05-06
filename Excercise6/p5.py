c=0
list=["k1","k2"]
for i in list:
	f1=open(i,"r")
	if(ch=='\n'):
		ch=f1.read(1)
		c=c+1
	print(c)
