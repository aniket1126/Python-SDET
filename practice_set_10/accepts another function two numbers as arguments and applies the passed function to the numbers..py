#accepts another function and two numbers as arguments and applies the passed function to the numbers.
def fun(main,a,b):
    return main(a,b)

def a1(x,y):
    return x+y
a=int(input("enter a numbetr"))
b=int(input("enter a number"))
print(fun(a1,a,b))

