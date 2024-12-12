mydic = {'apple':150,'mango':200,'cherry':120}
name=(input("enter a fruit name"))
try:
    print(mydic[name])
except KeyError:
    print(f'{name} is not in dictionary')