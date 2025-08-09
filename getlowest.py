# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    print((a+b+c)-min(a,b,c))
