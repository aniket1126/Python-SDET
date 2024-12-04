n = list(map(int, input("enter a list").split(",")))
largest = second = n[0]
for i in n:
    if i>largest:
        second = largest
        largest = i
    elif i > second and i!= largest:
        second = n
print(second)
