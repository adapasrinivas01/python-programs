s1=set(input().lower().replace(" ",""))
s2=set(input().lower().replace(" ",""))
c=sorted(s1.intersection(s2))
if len(c)>0:
	print(''.join(c))
else:
	print(-1)
