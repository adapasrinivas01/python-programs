n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
t=False
for i in l:
	if i<a or i>b:
		print(i,end=" ")
		t=True
if t==False:
	print(-1)
