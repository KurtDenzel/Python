import os
os.system('cls')

#Built-in Method Functions to be invoked.
class student:
	def __init__(self, studentname, age, yr, course):
		self.name = studentname
		self.age = age
		self.yrlevel = yr
		self.course = course
	def advanceyear(self):
		self.yrlevel += 1
	def shift_course(self, course):
		self.course = course
	def celebbday(self):
		self.age +=1
	def display(self):
		print (self.name)
		print (self.age)
		print (self.yrlevel)
		print (self.course)

s1 = student("JUAN", 21, 2, "IT")
s2 = student("LUCAS", 13, 1, "CS")

print("The List Follows Student Name, Age, YearLevel, Course")

print("-------"*5)
s1.display()#Student 1 Juan without the changes yet Output

#Methods
s1.advanceyear()#Advance year function to 21 to 22 increment
s1.celebbday()#Celebday function From 2 to 3
s1.shift_course("CS")#From Course IT to CS

print("-------"*5)
s1.display()

if s1.age>10:
	print ("OK")

print("-------"*5)
s2.display()#Student 2 Lucas outout

print("-------"*5)
print("NAME: KURT DENZEL CALACDAY")
print("STUDENT NUMBER: 20201125680")
print("-------"*5)