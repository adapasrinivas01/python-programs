s=input().split()
for word in s:
	add=0
	for c in word:
		if c.lower() in "aeiou":
			add+=1
	print(add,end=" 
