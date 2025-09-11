n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
u=[]
c=0
for i in l:
	if a<=i and b>=i:
		u.append(i)
		c+=1
if c==0:
	print(-1)
else:
	print(min(u))
