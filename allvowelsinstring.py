s=set(input())
a=sum(1 for c in s if c in "aeiou")
if a>=5:
	print("True")
else:
	print("False")
