def palindrome(s):
	if s!=s[::-1]:
		return False
	return True 

if palindrome(input("Enter string").replace(" ","").replace("?","").replace("!","").replace(",","").lower()):
	print("Is a palindrome")
else:
	print("Not a palindrome")
