menu = """1. Add Data
2. Delete By Value
3. Delete By Position
4. Sort
5. Reverse
6. Display Data"""

lst=[12,65,48,75]
while True:
	print("\n"+menu)
	ch = int(input("Enter choice (0-Exit) : "))
	if ch==0:
		break;
	if ch==1:
		if input("Add at custom position(y/n): ") == "y": 
			pos = int(input("Enter Position: "))
			if pos < len(lst)+1: lst.insert((pos-1),input("Enter Data: "))
			else:  
				for i in range(len(lst),pos-1):
					lst.append(None)
				lst.insert((pos-1),input("Enter Data: "))
		else:lst.append(input("Enter Data: "))
	elif ch==2:
		lst.remove(input("Enter Data: "))
	elif ch==3:
		del(lst[int(input("Enter Position: "))-1])
	elif ch==4:
		if int(input("Enter sorting order: (1-Asc, 0-Desc) ")) == 1:
			lst.sort()
			print(lst)
		else:
			lst.sort(reverse=True)
			print(lst)
	elif ch==5:
		lst.reverse()
		print(lst)
	elif ch==6:
		ch1 = int(input("Display with numbering (1/0): "))
		for i,j in enumerate(lst):
			if ch1 == 1:print(i+1,j)
			else: print(j)	
	else:print("Invalid input")
