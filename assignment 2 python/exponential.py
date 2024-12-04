# calculates the power of base raised to exponent using a loop.
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = 1
if exponent > 0:
    for _ in range(exponent):
        result *= base
elif exponent < 0:
    for _ in range(-exponent):
        result *= base
    result = 1 / result
print(f"{base} raised to the power of {exponent} is: {result}")
