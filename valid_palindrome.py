s=input().lower()
#it allows the alphabets and numbers
s="".join(c.lower() for c in s if c.isalnum()) 
if s==s[::-1]:
	print("palindrome")
else:
	print("Not palindrome")
