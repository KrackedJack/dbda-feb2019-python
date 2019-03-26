import os, sys
if os.path.exists("../write.txt"):
	with open("../write.txt") as fr:
		flist = fr.readlines()
else: 
	flist = list()

appendFlag = modifyFlag = False
added  = deleted = 0
lcount = len(flist)
print(lcount, flist)

def addRecord():
	global flist, appendFlag, added
	while True:
		id = int(input("Enter ID: "))
		name = input("Enter name: ")
		dept = input("Enter dept: ")
		job = input("Enter job: ")
		sal = int(input("Enter salary: "))
		flist.append("{}:{}:{}:{}:{}\n".format(id,name,dept,job,sal))
		if input("Add More? (y/n): ") == "n": break
	appendFlag = True
	added = added + 1

def modifyJob():
	global modifyFlag
	while True:
		id = input("Enter id of row: ")
		for ind,line in enumerate(flist):
		 	lst = line.split(":")
		 	print(lst)
		 	if lst[0] == id:
		 		lst[3] = input("Enter new job:")
		 		flist[ind] = "{}:{}:{}:{}:{}".format(lst[0],lst[1],lst[2],lst[3],lst[4])
		 		print("Modified successfully.")
		 		print(lcount, flist)
		 		print(ind, lcount)
		 		if ind<lcount:
		 			modifyFlag = True
		 		break
		else: print("ID not found")
		if input("Modify More? (y/n): ") == "n": break

def modifySalary():
	global modifyFlag
	while True:
		id = input("Enter id of row: ")
		for ind,line in enumerate(flist):
		 	lst = line.split(":")
		 	print(lst)
		 	if lst[0] == id:
		 		lst[4] = int(input("Enter new salary:"))
		 		flist[ind] = "{}:{}:{}:{}:{}\n".format(lst[0],lst[1],lst[2],lst[3],lst[4])
		 		print("Modified successfully.")
		 		print(lcount, flist)
		 		print(ind, lcount)
		 		if ind<lcount:
		 			modifyFlag = True
		 		break
		else: print("ID not found")
		if input("Modify More? (y/n): ") == "n": break

def searchByName():
	name = input("Enter name: ")
	for ind, line in enumerate(flist):
		if name == line.split(":")[1]:	
			print(ind, line)
			break
	else: print("Not found.")

def searchByID():
	id = int(input("Enter ID: "))
	for ind, line in enumerate(flist):
		print(line)
		if id == int(line.split(":")[0]):	
			print(ind, line)
			break
	else: print("Not found.")	

def deleteByID():
	global lcount, modifyFlag, appendFlag, added
	id = int(input("Enter ID: "))
	for ind, line in enumerate(flist):
		if id == int(line.split(":")[0]):	
			print(flist.pop(ind), "removed.")
			print(ind, lcount)
			if not modifyFlag and ind<lcount:
				modifyFlag = True
				lcount = lcount - 1
			else:
				added = added - 1
				if added == 0:
					appendFlag = False
			break
	else: print("Not found.")

def searchByJob():
	job = input("Enter job: ")
	for ind, line in enumerate(flist):
		if job == line.split(":")[3]:	
			print(ind, line)
			break
	else: print("Not found.")	


while True:
	print("1. Add record.\n"
		  "2. Modify salary.\n"
		  "3. Modify job.\n"
		  "4. Search by ID.\n"
		  "5. Search by name.\n"
		  "6. Delete by ID.\n"
		  "7. Search by designation.\n"
		  "8. Display all.\n"
		  "0. Exit.")

	ch = int(input("Enter choice: "))
	if ch == 1:
		addRecord()
	elif ch == 2:
		modifySalary()
	elif ch == 3:
		modifyJob()
	elif ch == 4:
		searchByID()
	elif ch == 5:
		searchByName()
	elif ch == 6:		
		deleteByID()
	elif ch == 7:
		searchByJob()
	elif ch == 8:
		for line in flist:
			print(line)
	elif ch == 0:
		print("a",appendFlag," m",modifyFlag)
		if appendFlag and not modifyFlag:
			with open("../write.txt","a") as fw:
				print("appending")
				for line in flist[lcount]:
					fw.write(line)
		
		elif modifyFlag:
			with open("../write.txt","w") as fw:
				print("writing")
				for line in flist:
					fw.write(line)

		else: print("No change.")

		break
	else: print("Invalid input")