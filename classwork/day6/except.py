
for i in [0,1,2]:

	try:
		
		fh = open("../../write.txt")
		lst  = [1,2,3]
		x = int(input("number: "))
		p = int(input("number: "))
		if p == 0:
			raise ZeroDivisionError("cannot div by 0 nigg")
		print(x/p)
		print(lst[x])
		break
	except ValueError:
		print("enter numeric data.")
	except ZeroDivisionError as e:
		print(e)
		print("can't divide by zero.")
	except:
		print("general exception.")
	finally:
		fh.close()
		print("finally exec.")
		
else:
	print("out of tries.")
