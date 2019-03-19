mydict = {"idk": ["act1"], 'jkr': ['jkr1', 'act1'], 'fgh': ['fgh1']}
menu = """1. Insert
2. Add actor in movie
3. Modify movie
4. Delete actor from movie
5. Delete movie
6. Display dict
7. Find movie by actor
0. Exit"""

def addActors(actors):
	while True:
		actor = input("Enter name of actor: (0 to stop) ")
		if actor == "0": break
		if actor in actors: print("Already added!")
		else: actors.append(actor)

def searchByValue(value, dict):
	matched = list()
	for k,v in dict.items():
		if v == value:
			matched.append(v)
	return matched 

while True:
	print("\n"+menu)
	ch = int(input("Enter choice: "))
	if ch==0: break
	if ch==1:
		movie = input("Enter movie: ")
		if movie in mydict:
			print("Already added!")
		else:
			mydict[movie] = list() #check if it works without explicit initialisation
			addActors(mydict[movie])
	elif ch==2:
		movie = input("Enter movie: ")
		if movie in mydict:
			addActors(mydict[movie])
		else:
			print("Movie doesn't exist")
	elif ch==3:
		movie = input("Enter movie: ")
		if movie in mydict:
			actors = mydict.pop(movie)
			movie = input("Enter updated movie name: ")
			mydict[movie] = actors
		else: print("Movie doesn't exist")
	elif ch==4:
		movie = input("Enter movie: ")
		if movie not in mydict: print("Movie doesn't exist!")
		else: 
			actor = input("Enter actor's name: ")
			if actor in mydict[movie]: 
				print(mydict[movie].pop(actor), "removed from", mydict[movie])
			else: print("This actor is not in this movie!")
	elif ch==5:
		movie = input("Enter movie: ")
		if movie not in mydict: print("Movie doesn't exist!")
		else: 
			if int(input("Are you sure you want to delete {}? (1/0)".format(movie)))==1: 
				mydict.pop(movie)
				print(movie,"removed.")
			else: print("ok.")
	elif ch==6: print(mydict)
	elif ch==7:
		matched = searchByValue(input("Enter actor: "), mydict)
		if len(matched)>0:
			print("found in", matched)
	else: print("Invalid input")	