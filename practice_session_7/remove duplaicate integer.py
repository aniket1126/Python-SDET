#numbers = [1, 2, 2, 8, 3, 4, 5, 4]
#unique_numbers = list(set(numbers))
#print(f"List after removing duplicates: {unique_numbers}")
#list1 = [1,1,2,2,3,4,4]
list1 = [1,1,2,3,3,4,5]
i=0
while i<len(list1):
    j=i+1
    while j < len(list1):
        if list1[i] == list1[j]:
            list1.pop(j)
        else:
            j=j+1
    i+=1
print(list1)