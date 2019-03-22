class A:
	def __init__(self, a):
		self.a = a

	def __str__(self):
		return "A:"+str(self.a)

class B(A):
	def __init__(self, b, **args):
		super().__init__(**args)
		self.b = b

	def __str__(self):
		return super().__str__()+" B:"+str(self.b)

class C(A):
	def __init__(self, c1, c2, **args):
		super().__init__(**args)
		self.c1 = c1
		self.c2 = c2

	def __str__(self):
		return super().__str__()+" C:"+str(self.c1)+","+str(self.c2)

class D(C,B):
	def __init__(self, d1, d2, **args):
		super().__init__(**args)
		self.d1 = d1
		self.d2 = d2

	def __str__(self):
		return super().__str__()+" D:"+str(self.d1)+","+str(self.d2)

if __name__ == '__main__':
	print(D(a=1,b=2,c1=3,c2=3,d1=4,d2=4))