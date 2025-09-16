s1=set(input().lower())
s2=set(input().lower())
c=s1.symmetric_difference(s2)
print(''.join(sorted(c)))

