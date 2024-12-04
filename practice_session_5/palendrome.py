#palendrome of a number
n =int(input("enter a number"))
previousnumber = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
if previousnumber == rev:
    print("the number is palendrome")
else:
    print("no palendrome")
