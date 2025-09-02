s=input().split()
m=10
for w in s:
	a=sum(1 for c in w if c.lower() in  "aeiou")
	m=min(m,a)
print(m)
