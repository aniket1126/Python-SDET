print("select operator")
print("1.  add")
print("2.  subtract")
print("3.  multiply")
print("4.  divide")
op_choice = int(input("enter operator number(1,2,3,4)"))
n = float(input("enter first number"))
n2= float(input("enter second number"))

if op_choice == 1:
    print(f"{n} + {n2} = {n+n2}")
elif op_choice == 2:
    print(f"{n} - {n2} = {n-n2}")
elif op_choice == 3:
    print(f"{n} * {n2} = {n * n2}")
elif op_choice ==4:
    if n2 != 0:
        print(f"{n} / {n2} = {n/n2}")
    else:
        print("error! divide by zero")
else:
    print("invalid input , plz enter valid input")





