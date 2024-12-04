start_index = int(input("Enter a start index: "))
end_index = int(input("Enter an end index: "))
prime = []
for i in range(start_index, end_index + 1):
    if i>1:
        is_prime = True  # Assume i is prime unless proven otherwise
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)
print(f"Prime numbers between {start_index} and {end_index}: {prime}")
