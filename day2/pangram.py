def pangram(s):
	alpha = "qwertyuioplkjhgfdsazxcvbnm"
	for a in alpha:
		if (s.find(a))==-1:
			return False

	return True

if pangram(input("Enter string").replace(" ","").replace("?","").replace("!","").replace(",","").lower()):
	print("Is a pangram")
else:
	print("Not a pangram")