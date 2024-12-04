# string is palindrome or not
n =input("enter a string")
previousnumber = n
rev = n[::-1]
if previousnumber == rev:
    print("the string is palendrome")
else:
    print("no palendrome")