import os;
os.system('cls')
UnitRate = 1545
MiscFee = 0.15
BlanketFee = 200

#At the university of the University of the East, every unit is worth P1,545 in enrollment fee. An Additional 15% of this amount is paid in miscellaneous fees with a blanket fee of P200 regardless of the load. Design a python program that will enter the number of the UNITS a student in and output the tuition fee to be paid.

print("------"*6)
Unit = int(input('Enter the total number of units: '))

print("------"*6)
UnitPrice = Unit*UnitRate
TotalMiscFee = UnitPrice*MiscFee+BlanketFee
TotalTuitionFee = UnitPrice+TotalMiscFee

print("------"*6)
print("The Unit price is: ", UnitPrice)
print("The Total Miscellaneous Fee is: ", TotalMiscFee)
print("The Total Tuition Fee is: ", TotalTuitionFee)