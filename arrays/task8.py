import array
arr = [1, 2, 3, 4, 5, 6]
n = int(input("enter a number"))
arr=arr[n:]+arr[:n]
print(arr)