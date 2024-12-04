#stars in increasing order up to a given number of rows.
def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print()


n=int(input("enter a number"))
pattern(n)