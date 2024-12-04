#a = 12
#b = 11

#print(a and b)
#print(a or b)

n=int(input("enter a number"))
num = 1
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print(num,end=" ")
        num+=1
    print()

