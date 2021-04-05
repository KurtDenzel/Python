import os;
os.system('cls');

#Built-in Method Functions to be invoked.
class runner:
    def __init__(instance,name,experience,speed,medal):
        instance.name = name;
        instance.exp = experience;
        instance.spd = speed;
        instance.mdl = medal;
        
    def run(instance, km):
        instance.exp += km;
        if instance.exp >= 100:
            instance.spd +=20;
            instance.mdl += 1;
    
    def displayStat(instance):
        print (instance.name);
        print (instance.exp);
        print (instance.spd);
        print (instance.mdl);


Runner1 = runner("Marina", 0,1,0,);
Runner2 = runner("Bari", 0,1,0,);

#Displays Runner 1 Marina without the changes yet.
Runner1.displayStat();
#Displays Runner 2 Bari without the changes yet.
Runner2.displayStat(); 
print("-------"*5)

#Methods 
Runner1.run(25);
Runner2.run(30);

Runner1.run(20);
Runner2.run(35);

Runner1.run(25);
Runner2.run(15);

Runner1.run(20);
Runner2.run(10);

Runner1.run(15);
Runner2.run(30);

Runner1.run(20);
Runner2.run(25);


#Changes output with methods
Runner1.displayStat(); #Marina
print("-------"*5)
Runner2.displayStat(); #Bari

print("-------"*5)
print("NAME: KURT DENZEL CALACDAY")
print("STUDENT NUMBER: 20201125680")
print("-------"*5)