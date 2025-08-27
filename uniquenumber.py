n=int(input())
m=list(str(n))
s=set(m)
if len(m)==len(s):
    print("unique number")
else:
    print("not unique number")
