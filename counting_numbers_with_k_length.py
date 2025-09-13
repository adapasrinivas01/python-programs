n,k=map(int,input().split())
l=list(map(int,input().split()))
s=sum(1 for i in l if len(str(abs(i)))==k)
print(s)
