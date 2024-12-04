#EXAMPLE 2
import sys
sys.path.append(r"C:\Users\hp\PycharmProjects\python\modules and packages\pack 1")
sys.path.append(r"C:\Users\hp\PycharmProjects\python\modules and packages\pack 1\pack2")

import module1 as m1
m1.show()

import module2 as m2
m2.fun()

from module1 import *
from module2 import *
show()
fun()


