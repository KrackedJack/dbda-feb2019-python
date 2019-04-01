x=20 

def func():
	global x
	x = 30
	print("x:",x)
	def infunc():
		#nonlocal x
		global x
		x = 45
		print("x:",x)
	print("calling infunc()")
	infunc()

func()
print("x: ",x)