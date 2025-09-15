s=set(input().replace(' ','').lower())
r=set(input().replace(' ','').lower())
d=s.symmetric_difference(r)
print(len(d))
