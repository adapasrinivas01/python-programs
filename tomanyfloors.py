n=int(input())
for i in range(n):
    a, b=map(int,input().split())
    c=((b-1)//10)-((a-1)//10)
    print(abs(c)) 
