n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    d=(b*3)-((a-b)*1)
    print("PASS" if d>=c else "FAIL")
