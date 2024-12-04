import animal
obj=animal.color()

import bird
obj=bird.fly()

from animal import *
fly()
color()

from bird import *
fly()
color()

import animal as a
a.fly()
a.color()

import bird as b
b.fly()
b.color()

