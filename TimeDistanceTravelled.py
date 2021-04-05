import os;
os.system('cls')

#A car travels at a constant speed of 50 kilometers per hour. Make a python program that will input TOME in minutes that a trip took and output the DISTANCE in kilometers that the car traveled.

speed = 50
time = int(input('Enter the time in minutes: '))
distance = speed*time
print("The distance in kilometers that the car travelled is: ", distance)
