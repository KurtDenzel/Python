import os
os.system('cls')
print("Welcome to IT2A Group 1 Airlines")
distance = int(input("Enter the distance in miles traveled by the airplane: "))
speed = 340
time = (distance / speed)*60
print('----'*6)
print("The time taken for the airplane to travel is", time, "minutes.")