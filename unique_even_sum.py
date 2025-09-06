n=int(input())
l=list(map(int,input().split()))
s=set(l)
a=0
for i in s:
	if i%2==0:
		a+=i
print(a)
