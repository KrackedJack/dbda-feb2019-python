class Person:
	def __init__(self, id, name):
		self.id = id
		self.name = name

	def __str__(self):
		return "ID: {}, Name: {}".format(self.id, self.name)

class Employee(Person):
	def __init__(self, id, name, dept, job):
		super().__init__(id, name) #usage of super
		self.dept = dept
		self.job = job

	def __str__(self):
		return "{}, Dept: {}, Job: {}".format(Person.__str__(self), self.dept, self.job) #useage of superclass name
 
class SalariedEmployee(Employee):
	def __init__(self, id, name, dept, job, sal, bonus):
		super().__init__(id, name, dept, job) 
		self.bonus = bonus
		self.sal = sal

	def __str__(self):
		return "{}, Salary: {}, Bonus: {}, NetSal: {}".format(Employee.__str__(self), self.sal, self.bonus, self.netSal()) 

	def netSal(self):
		return self.sal + (.1*self.sal) + (.15*self.sal) + (.08*self.sal) + self.bonus #sal+ha+hra+pf+bonus

class ContractEmployee(Employee):
	def __init__(self, id, name, dept, job, hrs, rate):
		super().__init__(id, name, dept, job) 
		self.hrs = hrs
		self.rate = rate

	def __str__(self):
		return "{}, Hours: {}, Rate: {}, NetSal: {}".format(Employee.__str__(self), self.hrs, self.rate, self.netSal()) 

	def netSal(self):
		return self.hrs * self.rate

if __name__ == '__main__':
	print(Employee(1,"name","dept","job"))
	print(SalariedEmployee(1,"name","dept","job",1236,65))
	print(ContractEmployee(1,"name","dept","job",1236,65))