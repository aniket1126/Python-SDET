#lambda map to double the elements of a list.
list1=(1,2,3,4,5,6,7,8,9)
evenno=list(map(lambda x:x+x,list1))
print(evenno)