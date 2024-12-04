#for i in range(1,101):
#    print(i)

#TASK 2:
#n =int(input("enter a number"))
#for i in range(0,n +1):
#    n = n+1

#print(n)

#TASK 3:
#print even number from 1 to 20
#even =0
#for i in range(2,21,2):
#    print(i)

#TASK 4:
#num = int(input("enter a number"))
#fact =1
#for i in range( 1,num+1):
#    fact = fact*i

#print(fact)


#TASK 5:
#NUM = int(input("enter a number"))
#for i in range(1,11):
#    result = NUM * i
#    print(f" {NUM}*{i} = {result}")

#n = int(input("enter a number"))
#prime = True
#for i in range(2,int(n/2)+1):
#    if n % i == 0:
#        prime = False
#        break

#if prime:
#    print(f"{n} is a prime number")
#else:
#    print(f"{n} is not prime")

#n = int(input("enter a number"))
#for i in range(1,n+1):
#    for j in range(1,i+1):
#        print(j,end=" ")
#    print()

#fibonacci series count print
#n = int(input("enter a number"))
#num1 =0
#num2 = 1
#for i in range(2,n):
#    fibo = num1+num2
#    num1,num2 = num2,fibo
#print(fibo)

#arm strong
n = int(input("enter a number"))
temp = n
sum = 0
pow = len(str(n))
while temp > 0:
    last = temp % 10
    sum = sum + last ** pow
    temp = temp // 10

if n == sum:
    print("number is armstrong")
else:
    print("number is not armstrong")