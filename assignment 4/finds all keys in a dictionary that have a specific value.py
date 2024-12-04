#finds all keys in a dictionary that have a specific value.
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 4, 'e': 1}
target_value = 1
value = []
for i,j in my_dict.items():
    if j == target_value:
        value.append(i)

print(value)


