from collections import Counter
s=input().lower().replace(" ","")
f=Counter(s)
t=False
for i in s:
	if f[i]==1:
		print(i)
		t=True
		break
if not t:
	print(-1)
