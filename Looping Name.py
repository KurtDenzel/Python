import os
os.system('cls')

List = []

for x in range (0, 10): #Up to 10 only. With the index of array 9
	Name = input ("Enter Name: ")
	if (len(Name)<5): #len counts the inputed Name on the Variable
		List.insert(0,Name) #Inserted to the "0" Index which is the first one
	else:
		List.append(Name)
	print(List)
print("\nNAME: KURT DENZEL CALACDAY")
print("\nSTUDENT NUMBER: 20201125680")