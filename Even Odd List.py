import os
os.system('cls')

EvenList = []
OddList = []

Number = int(input("Enter an Integer: "))

while (Number!=0): #Until it is 0, It will end the loop.
	if (Number%2 !=0):
		OddList.append(Number)
	else:
		EvenList.append(Number)
	os.system('cls')
	print("Even Numbers: ", EvenList) #Your Text then comma then call the variable
	print("Odd Numbers: ", OddList) #Your Text then comma then call the variable
	Number = int (input("Enter an Integer: "))
if (len(EvenList)>len(OddList)):
	EvenList.extend(OddList)
elif (len(OddList)>len(EvenList)):
	OddList.extend(EvenList)
print("~~~~~"*10)
print("EvenList:", EvenList)
print("OddList", OddList)
print("\nNAME: KURT DENZEL CALACDAY")
print("\nSTUDENT NUMBER: 20201125680")