# factorial of a number
n = int(input("enter a number"))
fact = 1
while n > 0:
    fact = fact*n
    n-=1
print(fact)