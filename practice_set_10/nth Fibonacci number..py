#nth Fibonacci number.
def fibo(n):
    if n == 0:
        return 0
    elif n==2 or n==3:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("enter a number"))
print(fibo(n))






