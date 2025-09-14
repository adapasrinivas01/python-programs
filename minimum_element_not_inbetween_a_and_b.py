n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=10
c=0
for i in l:
	if i<a or i>b:
		if i<m:
			m=i
			c+=1
if c>0:
	print(m)
else:
	print(-1)
	
