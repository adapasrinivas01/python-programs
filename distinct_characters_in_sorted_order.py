from collections import Counter
s=input().lower().replace(" ","")
f=Counter(s)
l=[i for i in s if f[i]==1]
print(''.join(sorted(l)))
