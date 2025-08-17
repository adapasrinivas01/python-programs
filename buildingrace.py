n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    if a*d<b*c:
        print("Chef")
    elif a*d>b*c:
        print("Chefina") 
    else:
        print("Both")
