# cook your dish here
n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    if a not in (c,d) and b not in (c,d) :
        print(2)
    elif a in (c,d) and b not in (c,d) or a not in (c,d) and b in (c, d):
        print(1)
    else:
        print(0)
        
    
