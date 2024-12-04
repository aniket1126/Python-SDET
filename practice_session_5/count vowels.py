# count vowels in a string
n = input("enter a string")
vowels = "aeiouAEIOU"
count = 0
for i in n:
    if i in vowels:
        count+=1

print("no of vowels",count)



