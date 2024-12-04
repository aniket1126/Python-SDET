#Longest substring without repeating characters
s = input("Enter a string: ")
start = 0
max_len = 0
char_set = set()
for i in range(len(s)):
    while s[i] in char_set:
        char_set.remove(s[start])
        start += 1
    char_set.add(s[i])
    max_len = max(max_len, i - start + 1)
print(max_len)
