# cook your dish 
n=int(input())
for i in range(n):
    a=int(input())
    t=a//7+(1 if a%7>=2 else 0)
    print(t)
