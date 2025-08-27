n=int(input())
while n>=10:
	s=0
	while n>0:
		s+=pow(n%10,2)
		n//=10
	n=s
if n==1 or n==7:
	print("happy")
else:
	print("unhappy")
