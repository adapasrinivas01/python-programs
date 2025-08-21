# cook your dish here
n=int(input())
for i in range(n):
    a,b,c,d,e=map(int,input().split())
    if (a+b<=d and c<=e) or (a+c<=d and b<=e) or (b+c<=d and a<=e):
        print("YES")
    else:
        print("NO")
        
