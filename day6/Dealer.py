class Dealer:
	def __init__(self, id, name, mob, addr):
		self.id = id
		self.name = name
		self.mob = mob
		self.addr = addr

	def __str__(self):
		return "ID: {}, Name: {}, Mobile: {}, Address: {}".format(self.id, self.name, self.mob, self.addr)

	def getMob(self): return self.mob

dealers =  [Dealer(1, "dealer1", "mobile1", "pune"), Dealer(2, "dealer2", "mobile2", "mumbai"), Dealer(3, "dealer3", "mobile3", "pune"), Dealer(4, "dealer4", "mobile4", "delhi"), 
Dealer(5, "dealer5", "mobile5", "pune")]

print(dealers)
print("dealers from pune:")
for dealer in dealers:
	if dealer[3] == "pune": print(dealer)