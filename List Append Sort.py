import os
os.system('cls')

ListA = []
for x in range(5):
	A = input("Enter number of characters: ")
	ListA.append(A) #Appends whatver you input on Variable A, will append/added to the ListA

print("The Alphabetical Order is: ")
ListA.sort() #Sort method is default to be alphabetical order
print(ListA)
print("------"*5)

print("The Alphabetical Order in reversed is: ")
ListA.reverse() #While reversed method is self explanatory
print("------"*5)
print(ListA)

print("Name: Kurt Denzel Calacday")
print("Student No.: 20201125680")