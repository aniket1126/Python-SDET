import array
arr=array.array('i',(1,2,3,4,5,6,7,8))
elemnt=4
for i in arr:
    if elemnt == i:
        print("found")
    else:
        print("not")