def find_max(a,b,c):
    if a > b:
        return a
    elif b > c:
        return b
    elif c > a:
        return c

print(find_max(166,240,11))