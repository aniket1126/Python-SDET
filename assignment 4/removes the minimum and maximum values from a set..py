#remove the min and max values from a set
set1 = {2, 4, 6, 8, 10, 12, 24}
min_val = float('inf')
max_val = float('-inf')
for i in set1:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i
set1.remove(min_val)
set1.remove(max_val)


print(set1)
