n=int(input())
l=list(map(int,input().split()))
l=l[::-1]
d=0
for i in range(n):
	d+=l[i]*pow(2,i)
print(d)
