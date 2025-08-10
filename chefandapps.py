n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    if (a-(b+c))>=d:
        print(0)
    elif (a-b)>=d or (a-c)>=d:
        print(1)
    else:
        print(2)
    
