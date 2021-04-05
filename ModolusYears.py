import os;
os.system('cls');

#Every leap year is divisible by 4.
#Create a python program that will input YEAR and display whether the year is “LEAP YEAR or “ORDINARY YEAR”.

Year=int(input("Please Enter a Year to be Checked: "))

print("_____"*5);
print("-----"*5);

if(Year %4 == 0 and Year % 100 != 0 or Year % 400 == 0):
    print(Year, "LEAP YEAR");
else:
    print(Year, "ORDINARY YEAR");