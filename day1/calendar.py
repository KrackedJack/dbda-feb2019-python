days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
startDay = int(input("Enter starting day:\n>"))
nDays = int(input("Enter no. of days:\n>"))

for day in days:print(day,"\t", end=" ")
print( )

for day in range(1, nDays+startDay):
	#print(day, end=" ")
	if day >= startDay:
		print("%3d\t" %(day-startDay+1), end=" ")
	else:
		print("\t", end=" ")
	if day%7==0:
		print( )
