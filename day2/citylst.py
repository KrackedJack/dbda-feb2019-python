cities = []
locations = []

while True:
	cities.append(input("Enter City: "))
	if(input("Add more:? (y/n) ")!="y"):
		break;

while True:
	locations.append(input("Enter Location: "))
	if(input("Add more:? (y/n) ")!="y"):
		break;

print(cities)
print(locations)

for i in zip(cities, locations):
	print("{}\t{}".format(i[0],i[1]))	

