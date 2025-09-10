n=int(input())
l=list(map(int,input().split()))
t=True
for i in l:
	if i!=0 and i!=1:
		t=False
		break
if t:
	print(t)
else:
	print(t)
