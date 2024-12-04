#counts the occurrences of a specific element in a tuple.
lst = [2, 4, 2, 6, 2, 8, 10]
occur = {}
for i in lst:
    if i not in occur:
        occur[i]=1
    else:
        occur[i]+=1

occur_tuple = tuple(occur)
print(occur_tuple)
