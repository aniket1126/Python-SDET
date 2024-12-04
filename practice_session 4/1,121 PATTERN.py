n = 5
for i in range(n):
    print(" " * (n - i - 1), end="")
    for k in range(1, i + 2):
        print(k, end="")
    for l in range(i, 0, -1):
        print(l, end="")
    print()