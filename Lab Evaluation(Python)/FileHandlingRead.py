import os,sys
if os.path.exists("empdata.txt"):
	with open("empdata.txt")as fr:
		flist = fr.readlines()
else: 
	print("File Empty.")
	sys.exit(0)

for ind, line in enumerate(flist):
	emp = line.split(":")
	if "manager" == emp[3].lower():	
		print("ID: {}, Name: {}, Salary: {}, Job: {}".format(emp[0], emp[1], int(emp[2])+2000, emp[3]))
		
	elif "analyst" == emp[3].lower():	
		print("ID: {}, Name: {}, Salary: {}, Job: {}".format(emp[0], emp[1], int(emp[2])+1500, emp[3]))
		
	else:	
		print("ID: {}, Name: {}, Salary: {}, Job: {}".format(emp[0], emp[1], int(emp[2])+1000, emp[3]))
			
		