import array
#arr = [1, 2, 3, 4, 5, 6]
#d = 2
#arr=arr[d:]

arr=array.array('i',[1,2,3,4,5])
sum=0
len= len(arr)
for i in range(len):
    sum+=arr[i]
print(sum)