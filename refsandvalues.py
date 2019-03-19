a = 10 
b = a 

if id(a)==id(b):
	print("same")
else:
	print(" not same")

b=20

if id(a)==id(b):
	print("same")
else:
	print(" not same")
	
a = [5,12,63]
b = a

if id(a)==id(b):
	print("same")
else:
	print(" not same")

c = a.copy()

if id(c)==id(a):
	print("same")
else:
	print(" not same")
