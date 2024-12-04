import sys
sys.path.append(r"C:\Users\hp\PycharmProjects\python\modules and packages\pack 1")=sys.path.append(r"C:\Users\hp\PycharmProjects\python\modules and packages\pack 1\pack2")

from module3 import *
from module4 import *

obj=employee()
obj.fun('102',200)


obj=student()
obj.display('aniket',23)