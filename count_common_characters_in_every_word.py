s=input().lower().split()
c=set(s[0])
for word in s:
	c=c.intersection(set(word))
if len(c)>0:
	print(min(c))
else:
	print(-1)
