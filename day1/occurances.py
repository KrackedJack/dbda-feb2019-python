def occr(s1, s2, ind):
	occ = []
	index = s1.find(s2) 
	if index==-1:
		return occ
	else:
		occ.append(index+ind)
		occ.extend(occr(s1[index+1:],s2,index+ind))
	
	return occ

str1 = input("Enter string: \n> ")
str2 = input("Enter substring: \n> ")

res = occr(str1,str2,0)
if len(res)!=0:
	print(str2, " found at: ", res)
else:print("Not Found")

