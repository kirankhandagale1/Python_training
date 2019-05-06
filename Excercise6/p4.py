#Write a Python program to combine each line from first file with the corresponding line in second file.

f1=open("k1","r")
f2=open("k2","r")
for l1,l2 in zip(f1,f2):
	print(l1+l2)
