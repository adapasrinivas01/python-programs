n=int(input())
l=list(map(int,input().split()))
unique=[]
for i in range(n):
	if l[i] not in unique:
		unique.append(l[i])
print(*unique)
