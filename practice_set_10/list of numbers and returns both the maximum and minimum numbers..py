#list of numbers and returns both the maximum and minimum numbers.
def min_max(list):
    min = max =list[0]
    for i in list:
        if i < min:
            min = i
        if i > max:
            max = i
    return min,max

list=[2,4,6,8,10]
print(min_max(list))

