n1,n2=10,2
list=[1,2,3,4,5,6]
try:
    result=n1/n2
    print(result)
    print(list[8])
except ZeroDivisionError:
    print('divisonal error')
except IndexError:
    print('index error')