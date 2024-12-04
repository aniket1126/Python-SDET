#min and max in array
import array
arr =array.array('i',(2,4,6,8,10))
min = max = arr[0]
for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i

print(min,max)
