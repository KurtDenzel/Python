import os
os.system('cls')

#A driver will be fined P500 if his SPEED goes beyond 80 kph, and P800 if it goes beyond 100 kph.
#Design a python program that will input the car’s speed and output the fine.

Speed = float(input("Enter your speed in kph: "))
if Speed > 80 and Speed <= 100:
    print("You will be Charged Php500 for Exceeding 80kph.")
elif Speed > 100:
    print("You will be Charged Php800 for Exceeding 100kph.")
else:
    print("Have a Safe trip.")