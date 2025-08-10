n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    e=(b,c,d,b+c,b+d,c+d,b+c+d)
    print("YES" if a in e else "NO")
