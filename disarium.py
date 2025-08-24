heren=int(input())
n1=n
m=len(str(n))
s=0
while n>0:
	s=s+pow(n%10,m)
	n=n//10
	m=m-1
if n1==s:
	print("True")
else:
	print("False")
	
