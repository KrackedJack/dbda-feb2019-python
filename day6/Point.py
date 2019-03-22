class Point:
	def __init__(self, x=0,y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return "x:{}, y:{}".format(self.x,self.y)

	def __add__(self,other):
		if isinstance(other,Point):
			return Point(self.x + other.x, self.y + other.y)
		return Point(self.x + other, self.y + other)

	def __radd__(self,other):
		return Point(self.x + other, self.y + other)

	def __mul__(self,other):
		if isinstance(other,Point):
			return Point(self.x * other.x, self.y * other.y)
		return Point(self.x * other, self.y * other)

	def __rmul__(self,other):
		return Point(self.x * other, self.y * other)

	def __sub__(self,other):
		if isinstance(other,Point):
			return Point(self.x - other.x, self.y - other.y)
		return Point(self.x - other, self.y - other)

	def __rsub__(self,other):
		return Point(self.x - other, self.y - other)

	def __truediv__(self,other):
		if isinstance(other,Point):
			return Point(self.x / other.x, self.y / other.y)
		return Point(self.x / other, self.y / other)

	def __rtruediv__(self,other):
		return Point(self.x / other, self.y / other)




if __name__ == '__main__':
	p1 = Point(5,2)
	p2 = Point(10,40)
	print("add:",p2+p1)
	print("radd:",p2+10)
	print("mul:",p2*p1)
	print("rmul:",p2*10)
	print("sub:",p2-p1)
	print("rsub:",p2-10)
	print("div:",p2/p1)
	print("rdiv:",p2/10)
