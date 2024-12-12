# to avoid termination we use exception handling
# we use try and except to handle exceptions
#EXCEPTION IS THE SUPER CLASS OF ALL CLASSES

# print('start')
# print('start')
# print('start')
# print('start')
# print('start')
# arr=[1,2,3]
# num1,num2=10,2
# def age(n):
#     if n < 0:
#      raise ValueError()
#     if n%2==0:
#         print('even')
#     else:
#         print('odd')
# n=-1
# try:
    # print(5/0)
    # print(arr[4])
    # result=num1/num2
    # print(result)
#  age(n)
# except ValueError:
#     print('exception in code')
#     print('program terminate')
# except:
#     print('the exception occurred')
# except Exception as e:
#     print(e)
# else:
#     print('no exception occur')


"USER DEFINE EXCEPTIONS"
from idlelib.colorizer import matched_named_groups


#IF WE WANT TO CREATE A CLASS THEN IT WILL INHERIT FROM BUILT IN CLASS
# class customError(Exception):
#     pass
# try:
#     raise customError('this is a error msg')
# except customError as e:
#     print(e)

class negativenumbererror(Exception):
    def __init__(self,msg='-ve values'):
        self.msg=msg
        super().__init__(self.msg)

def checkpositive(n):
    if n < 0:
        raise negativenumbererror('invalid number enter the +ve number')

try:
    n=int(input('enter a number'))
    checkpositive(n)
except negativenumbererror as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)