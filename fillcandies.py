n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if(a%(b*c)==0):
        print(a//(b*c))
    else:
        print(int(a/(b*c))+1)
