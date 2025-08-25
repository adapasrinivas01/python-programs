n=int(input())
fib1,fib2=0,1
while fib2<n:
	fib1,fib2=fib2,fib1+fib2
d1=abs(n-fib1)
d2=abs(n-fib2)
if d1<d2:
	print(fib1)
elif d1>d2:
	print(fib2)
else:
	print(fib1,fib2)
