n1=int(input("enter a number"))
n2=int(input('enter a number'))
try:
    result=n1+n2
    print(result)
except ValueError:
    print('value should be int type')