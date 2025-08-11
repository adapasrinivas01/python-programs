n=int(input())
for i in range(n):
    a=int(input())
    print(a//10 if a%10==0 else (a//10)+1)
