import os
os.system('cls')

List = []

Number = int(input("Enter an integer: "))

while (Number !=0): #Until it is 0, It will end the loop.
	List.append(Number) #Adds integers to your list container
	os.system('cls')
	print (List) #Prints your List every time you input an integer
	Number = int(input("Enter an integer: "))
os.system('cls') #Clear Screen


print("Your inputted List:")
print(List)
print("\nNAME: KURT DENZEL CALACDAY")
print("\nSTUDENT NUMBER: 20201125680")
print("[~~~~~END~~~~~]")