import os;
os.system('cls');

print("-------"*5)
print ("Enter ten integers, three consecutive odd integers will raise an error.")
print("-------"*5)

NumberList = [];
Counter = 0

#While Loop len method if NumberList is greater than 10
while len (NumberList) < 10:
    Number = int (input ("Enter an integer: "));
        
    if (Number %2==1):
            Counter = Counter + 1
    else:
            Counter = 0 #Counter to reset back
    
    #Executes if a 3rd Odd Integer is inputted
    if Counter >= 3:
        print ("\nERROR! You have entered three consecutive odd integers. Input even integer.")
        print ()
    else:
        NumberList.append (Number)

print(NumberList)

print("-------"*5)
print("NAME: KURT DENZEL CALACDAY")
print("STUDENT NUMBER: 20201125680")
print("-------"*5)