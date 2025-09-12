n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
m=0
for i in l:
	if a<=i and b>=i:
		c+=1
		if m<i:
			m=i
if c>0:
	print(m)
else:
	print(-1)
