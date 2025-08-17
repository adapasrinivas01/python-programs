import math
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    d=(a+(c//30))
    print(math.ceil(d/b))
