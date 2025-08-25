s=input().split()
v="AEIOUaeiou"
mx=0
for word in s:
	w=sum(1 for i in word if i in v)
	mx=max(mx,w)
print(mx)
