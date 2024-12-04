#integer as input and repeatedly finds the sum of its digits until a single-digit number
number = int(input("Enter an integer: "))
sum = 0
while number > 0:
    l=number%10
    sum+=l
    number=number//10

print(sum)


