#number is even or odd and returns a boolean value.
def even(n):
    if n%2 ==0:
        return True
    else:
        return False

n=int(input("enter a number"))
print(even(n))