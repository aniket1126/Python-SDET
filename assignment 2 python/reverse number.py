# Reverse a Number:
n = int(input("enter a number"))
rev = 0
while n > 0:
    rev = n%10 + rev*10
    n  = n//10
print(rev)






