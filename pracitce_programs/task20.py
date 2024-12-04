value1 = int(input("enter a number"))
value2 = int(input("enter a number"))

if value1 and value2 > 0:
    print("the value is positive")
elif value1 and value2 < 0:
    print("the value is negative")
if value1 < 0 or value2 > 0:
    print("mixed value")
