#converts a tuple of numbers to a list, appends a given number to the list, and then converts it back to a tuple.
tuple1 = (2,4,6,8,10)
list1 = list(tuple1)
list1.append(12)
tuple1 = tuple(list1)
print(tuple1)



