import os;
os.system('cls');

age=int(input("Kindly enter your age: "));

print("_______"*5);
print("-------"*5);

if age < 18:
	print("UNDERAGE");
	exit();
elif age == 18:
	print("STUDENT LICENSE POSSIBLE");
elif age > 18:
	print("PROFESSIONAL LICENSE POSSIBLE");

print("_______"*5);
print("-------"*5);

result = input("Kindly enter your Drug examination result: ");

if result == "POSITIVE" or result == "Positive" or result == "positive":
	print("HOLD LICENSE");

elif result == "NEGATIVE" or result == "Negative" or result == "negative":
	print("RELEASE LICENSE");