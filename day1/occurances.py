def occr(s1, s2, ind, occ):
	index = s1.find(s2) 
	if index==-1:
		return 
	else:
		print("append",index+ind)
		occ.append(index+ind)
		occr(s1[index+1:],s2,index+ind,occ)
	
	return occ

str1 = input("Enter string: \n> ")
str2 = input("Enter substring: \n> ")
occ = []
res = occr(str1,str2,0, occ)
if len(res)!=0:
	print(str2, " found at: ", res)
else:print("Not Found")

