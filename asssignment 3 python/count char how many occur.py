n = input("Enter a string: ")
result = ""
count = 1
for i in range(1, len(n)):
    if n[i] == n[i - 1]:
        count += 1
    else:
        result+=(n[i - 1] + str(count))
        count = 1
result+=(n[-1] + str(count))
print("Compressed", result)
