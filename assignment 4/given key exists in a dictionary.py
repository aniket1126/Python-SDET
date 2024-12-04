#given key exists in a dictionary.py
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'
if key_to_check in my_dict:
    print(my_dict[key_to_check])
else:
    print('Key not found')
