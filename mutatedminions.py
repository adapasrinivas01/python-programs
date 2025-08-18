n=int(input()) 

for i in range(n):
    t,k=map(int,input().split()) 
    c=0
    a=list(map(int,input().split()))
    for j in a:
        if((j+k)%7==0):
            c=c+1
    print(c)
