#string is palendrome
def pal(n):
    previousstr=n
    rev = ""
    rev = n[::-1]
    if previousstr == rev:
        return True
    else:
        return False

n = input("enter a string")
print(pal(n))