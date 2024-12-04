#remove duplicate characters from a string while preserving the order of characters
input_string = input("Enter a string: ")
seen = set()
result = []
for char in input_string:
    if char not in seen:
        result.append(char)
        seen.add(char)
print("String after removing duplicates:", ''.join(result))
