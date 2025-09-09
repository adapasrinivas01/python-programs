  n=int(input())
l=list(map(int,input().split()))
m=100
for i in l:
	if m>i:
		m=i
s=0
s=sum(1 for i in l if len(str(m))==len(str(i)))
print(s)
