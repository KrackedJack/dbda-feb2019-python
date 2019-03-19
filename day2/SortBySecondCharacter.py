def SortBySecondCharacter(d,lst):	
	for i in range(0,len(lst)):
		if((lst[i])[1] == d[1]):
			lst.insert(i,d)
			return

		if(i==len(lst)-1):
			lst.append(d)
			return

lst = ["cat","bat","rat","abc","cbd","acc","bcc"]

SortBySecondCharacter("ced",lst)
print(lst)