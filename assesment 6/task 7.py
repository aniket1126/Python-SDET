def sum_of_squares(*args):
    return sum(x**2 for x in args)
result = sum_of_squares(1, 2, 3)
print(result)
result = sum_of_squares(4, 5, 6, 7, 8)
print(result)
result = sum_of_squares()
print(result)  
