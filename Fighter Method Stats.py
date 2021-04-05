import os
os.system('cls')

#Built-in Method Functions to be invoked.
class fighter:
	def __init__(self, name, lives, heart, rank, level):
		self.name = name
		self.lives = lives
		self.heart = heart
		self.rank = rank
		self.level = level
	#Instance method
	def attack(self, xp):
		self.rank += xp
		if self.rank >= 100:
			self.level += 1
			self.rank -=100
	#Another Instance method
	def damage(self, hurt):
		self.heart -= hurt
		if self.heart <= 0:
			self.lives -=1
			self.heart = 100
		self.gameover()	
	#Another Instance method
	def dead(self):
		self.lives -= 1
		self.heart = 100
		self.gameover()
	#Another Instance method
	def gameover(self):
		if self.lives == 0:
			print ("Game Over")
			del (self)
	#Another Instance method
	def display(self):
		print (self.name)
		print (self.lives)
		print (self.heart)
		print (self.rank)
		print (self.level)


f1 = fighter("Karrie", 5, 100, 0, 1)
f2 = fighter("Claude", 5, 100, 0, 1)

#Methods
def attackf2(num):
	f1.attack(num)
	f2.damage(num)
def attackf1(num):
	f2.attack(num)
	f1.damage(num)
def displayF(): #Displays/Prints outputs the Fighers at the Same time. 
	f1.display()
	f2.display()


print("Fighter's Attributes Name, Lives, Hearts, Rank, and Level")
print("-------"*5)
displayF()#Displays/Prints the Fighers without the Attacks yet/No Changes yet


attackf1(30)
attackf2(60)#100 - 60 Deals to = 40
print("-------"*5)
displayF()

print("-------"*5)
print("NAME: KURT DENZEL CALACDAY")
print("STUDENT NUMBER: 20201125680")
print("-------"*5)