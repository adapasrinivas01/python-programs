n = int(input())
l = list(map(int, input().split()))
s = sum(sum(int(j) for j in str(i)) for i in l)
print(s)
