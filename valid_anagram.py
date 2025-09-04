s=input().lower()
t=input().lower()
if len(s)!=len(t):
	print("Not Anagram")
else:
	if sorted(s)==sorted(t):
		print("Anagram")
	else:
		print("Not Anagram")
