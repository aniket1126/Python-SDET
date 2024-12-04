n = input("enter a str")
words = n.split()
max_length = ""
for i in words:
    if len(max_length) < len(i):
        max_length = i
        print(f"{max_length},{len(max_length)}")


