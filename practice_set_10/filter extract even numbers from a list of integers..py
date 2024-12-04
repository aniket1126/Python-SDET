# filter to extract even numbers from a list of integers.
list1=(1,2,3,4,5,6,7,8,9)
evenno=list(filter(lambda x:x%2==0,list1))
print(evenno)