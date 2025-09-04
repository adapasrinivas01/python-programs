n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
	rev=str(l[i])[::-1]
	if l[i]==int(rev):
		c=c+1
print(c)
