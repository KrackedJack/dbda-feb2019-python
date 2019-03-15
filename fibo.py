def fib(gg):
	a, b = 0, 1
	while a<=gg:
		print(a)
		#print(b)
		a, b = b, a+b
		
	print()
	
fib(int(input("Enter limit> "))) 