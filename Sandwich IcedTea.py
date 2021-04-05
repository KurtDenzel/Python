import os
os.system

print("Welcome. Products offfered: Sandwich = Php50 & Iced Tea: Php30")
print("Proceed with bill calculation.")
print("-----"*6)

swprice = float(input("Enter no. of sandwich/es: "))
itprice = float(input("Enter no. of iced tea: "))
totalbill = (swprice * 50) + (itprice * 30)

print("The total amount of bill is " , totalbill)

totalpayment = float(input("Enter cash amount for payment."))
totalchange = (totalpayment - totalbill)

print("-----"*6)
print("You're change is " , totalchange)

print("Thank you for your order")

