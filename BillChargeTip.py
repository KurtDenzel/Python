import os;
os.system('cls');
TotalBill = float(input("Enter Total Bill: "))
LiquorCharge = float(input("Enter Liquor Charge: "))
TipPercentage = float (input("Enter Tip Percentage (in decimal): "))
Tip = (TotalBill - LiquorCharge)*TipPercentage
print("Your Tip is", Tip)