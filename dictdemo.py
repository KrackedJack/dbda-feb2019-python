mydict = {1:"a", 2:"b", 3:"c"}

print("dict: ",mydict)

s = input("enter alpha to search: ")
for k,v in mydict.items():
	if v==s:
		print("found at ",k)
		break
else: print("not found")