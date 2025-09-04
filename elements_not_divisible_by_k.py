n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(n):
	if l[i]%k!=0:
		c=c+1
print(c)
