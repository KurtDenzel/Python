import os
os.system('cls')

Fare = 10.35
Meters = 250

print("-----"*6)
Distance = float(input("Enter the Distance Traveled by your taxi: "))
print("-----"*6)

Convert = Distance*1000

Divide = Convert/Meters

Cost = Divide*Fare


print("Distance Travled in Kilometers = ", Distance)
print("Distance Traveled in meters =", Convert)
print("Fix Taxi Fare=", Fare, "Every", Meters, "Meters")
print("The Total Cost of your trip is:", Cost)
print("-----"*6)
