n=int(input())
l=list(map(int,input().split()))
t=True
for i in range(n-1):
	if l[i]<l[i+1]:
		t=False
		break
if t:
	print("yes")
else:
	print("no")
