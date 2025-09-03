s=input().lower()
s=s.replace(" ","")
s=sorted(set(s))
print("".join(s))
