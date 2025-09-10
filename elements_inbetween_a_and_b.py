n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in l:
	if a<=i and i<=b:
		count+=1
		print(i,end=" ")
if count==0:
	print(-1)
