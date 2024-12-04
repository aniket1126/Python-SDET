#use of default values for some of them.
def large(a,b=5):
    if a>b:
        return a
    else:
        return b

n=int(input("enter a number"))
print(large(n))