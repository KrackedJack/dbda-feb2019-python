import os, sys
if os.path.exists("../write.txt"):
	with open("../write.txt")as fr:
		flist = fr.readlines()
else: 
	flist = list()

appendFlag = modifyFlag = False
lcount = len(flist)


def addRecord():
	global flist, appendFlag
	while True:
		id = int(input("Enter ID: "))
		name = input("Enter name: ")
		dept = input("Enter dept: ")
		job = input("Enter name: ")
		sal = int(input("Enter name: "))
		flist.append("{}:{}:{}:{}:{}\n".format(id,name,dept,job,sal))
		if input("Add More? (y/n): ") == "n": break
	appendFlag = True

def modifyJob():
	global modifyFlag
	modifyFlag = True

while True:

	print("""1. Add record.
	2. Modify salary.
	3. Modify job.
	4. Search by ID.
	5. Search by name.
	6. Delete by ID.
	7. Search by designation.
	8. Display all.
	0. Exit.""")

	ch = int(input("Enter choice: "))
	if ch == 1:
		addRecord()
	elif ch == 2:
		modifyJob()
	elif ch == 3:
		pass
	elif ch == 4:
		pass
	elif ch == 5:
		pass
	elif ch == 6:		
		pass
	elif ch == 7:
		pass
	elif ch == 8:
		for line in flist:
			print(line)
	elif ch == 0:
		print("a",appendFlag," m",modifyFlag)
		if appendFlag and not modifyFlag:
			with open("../write.txt","a") as fw:
				print("[wr]")
				for line in flist[lcount]:
					fw.write(line)
		
		if modifyFlag and not appendFlag:
			pass
		
		break
	else: print("Invalid input")

