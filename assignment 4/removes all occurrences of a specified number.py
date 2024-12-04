#removes all occurrences of a specified number
list1 = [1, 2, 3, 4, 2, 5, 2, 6]
number_to_remove = 2
new = []
for i in list1:
    if i != number_to_remove:
        new.append(i)
print("Modified List:", new)

