#find and return the index of all occurances of a specified element in a list
lst = [2, 4, 2, 6, 2, 8, 10]
occur = {}
for i in range(len(lst)):
    value = lst[i]
    if value not in occur:
        occur[value] = [i]
    else:
        occur[value].append(i)


print(occur)
