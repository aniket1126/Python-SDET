# Sum of Even Numbers:
n= int(input("enter a number"))
sum = 0
for num in range(n+1):
    if num%2 == 0:
        sum+=num
        print("Sum of even numbers from 1 to", n, "is:", sum)
