vehicleOwners = {"owner1":"veh1"}

def addRecord(person = None):
	global vehicleOwners
	if person == None:	
		person = input("Enter owners name")
		if person not in vehicleOwners:
			vehicleOwners[person] = list().append(input("Enter vehicle: "))
		else: print("Person already exists. Use MODIFY option.")
			
	else: vehicleOwners[person] = list().append(input("Enter vehicle: "))

def modifyRecord():
	global vehicleOwners
	person = input("Enter owner's name.")
	if person not in vehicleOwners:
		if input("Person doesn't exist, Add? (y/n): ") == y:
			addRecord(person)
		else: print("okay")
	else: vehicleOwners[person].append(input("Enter vehicle: "))

def deleteRecord():
	person = input("Enter owner's name.")
	if person not in vehicleOwners:
		print("Person doesn't exist.")
	else: print(vehicleOwners.pop(person),"removed from records.")

def searchByVehicle():
	vehicle = input("Enter vehicle: ")
	owners = list()
	for k,v in vehicleOwners.items():
		if v == vehicle:
			owners.append(k)
	if len(owners)==0:
		print("No record found.")
	else: 
		for i in owners: print(i)

def searchByOwner():
	person = input("Enter owner: ")
	if person in vehicleOwners:
		print("{} owns {}".format(person, vehicleOwners[person]))
	else: print("Not found.")

def displayOwners():
	for o in vehicleOwners.keys():
		print(o)

def displayVehicles():
	for o in vehicleOwners.values():
		print(o)
		
while True:
	print("\n1. Add Person and Vehicle.\n"
		  "2. Modify Record.\n" 
		  "3. Delete Record.\n"
		  "4. Search by vehicle.\n"
		  "5. Search by owner.\n"
		  "6. Display Owners.\n"
		  "7. Display Vehicles.\n"
		  "0. Exit.")
	ch = int(input("Enter choice: "))
	if ch == 1:
		addRecord()
	elif ch == 2:
		modifyRecord()
	elif ch == 3:
		deleteRecord()
	elif ch == 4:
		searchByVehicle()
	elif ch == 5:
		searchByOwner()
	elif ch == 6:
		displayOwners()
	elif ch == 7:
		displayVehicles()
	elif ch == 0:
		break
	elif ch == 10:
		for i,j in vehicleOwners.items(): print(i,j)
	else: 
		print("Invalid Input.")
