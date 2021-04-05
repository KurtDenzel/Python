import os;
os.system('cls');

A = []
B = []
C = []
setA = {}
setB = {}
setC = {}

for x in range (0,5):
	console = int(input("Enter 5 Integers for Set A: "))
	A.append(console)

print("--------"*5)
print("SET A")
setA = set(A);
print("",setA)
print("--------"*5)

for x in range (0,5):
	console = int(input("Enter 5 Integers for B: "))
	B.append(console)

print("--------"*5)
print("Set B")
setB = set(B);
print(setB)
print("--------"*5)

for x in range (0,5):
	console = int(input("Enter 5 Integers for Set C: "))
	C.append(console)

print("--------"*5)
print("Set C")
setC = set(C);
print(setC)

print("--------"*5)
print("\tYour List of Sets")
print("\nSET A",setA)
print("SET B",setB)
print("SET C",setC)

print("--------"*5)
print("\tSet Operations")

#Union
print("\nUnion of sets A and C")
print(setA | setC)

#Intersection 
print("\nIntersection of sets A and B")
print(setA & setB)

#Symmetric Difference 
print("\nSymmetric Difference of sets B and C")
print(setB ^ setC)

print("--------"*5)
print("Name: Kurt Denzel Calacday")
print("Student No.: 20201125680")