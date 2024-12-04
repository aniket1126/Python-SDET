# find the min and max in the list
n = input("Enter a list")
numbers = list(map(int, n.split(',')))  # Convert the comma-separated string into a list of integers
max_ = numbers[0]
min_ = numbers[0]
for i in numbers:
    if i < min_:
        min_ = i
    elif i > max_:
        max_ = i
result = (min_, max_) #store as a tuple
print("Min and Max:", result)
