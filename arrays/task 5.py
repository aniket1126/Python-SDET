import array
arr=array.array('i',(1,1,2,3,4,5,6,7,8))
mydic = {}
for i in arr:
    if i not in mydic:
        mydic[i]=1
    else:
        mydic[i] += 1

print(mydic)
