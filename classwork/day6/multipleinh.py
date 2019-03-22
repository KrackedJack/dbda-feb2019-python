class A:
	def __init__(self, a):
		self.a = a

	def __str__(self):
		return "A:"+str(self.a)

class B:
	def __init__(self, a):
		self.a = a

	def __str__(self):
		return "B:"+str(self.a)

class C(A,B):
	def __init__(self, a, b, c):
		A.__init__(self,a)
		B.__init__(self,b)
		self.c = c

	def __str__(self):
		return "{}, {}, C: {}".format(A.__str__(self), B.__str__(self), self.c)		

if __name__ == '__main__':
	print(C(1,2,3))
