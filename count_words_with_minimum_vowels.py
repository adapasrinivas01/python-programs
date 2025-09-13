s=input().split()
m=min(sum(1 for c in w if c.lower() in "aeiou") for w in s)
min_count=sum(1 for w in s if sum(1 for c in w if c.lower() in "aeiou")==m)
print(min_count)
