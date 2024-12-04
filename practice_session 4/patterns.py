#pattern 1
#n = int(input("enter a number"))
#for i in range(n):
#    for j in range(i):
#        print("*",end=" ")
#    print()

#    *
#    * *
#    * * *
#   * * * *

#pattern 2
#n = int(input("enter a number"))
#for i in range(n):
#    for j in range(n-i):
#        print("*",end=" ")
#    print()

#    * * * * *
#    * * * *
#    * * *
#    * *
#    *

#pattern 3
#n = int(input("enter a number"))
#for i in range(n):
#    for j in range(i):
#        print(" ",end=" ")
#    for k in range(n-i):
#        print("*",end=" ")
#    print()
#* * * * *
#  * * * *
#    * * *
#      * *
#        *

#pattern 4
#n = int(input("enter a number"))
#for i in range(n):
#    for j in range(n-i):
#        print(" ",end=" ")
#    for k in range(i):
#        print("*",end=" ")
#    print()

#        *
#      * *
#    * * *
#  * * * *

#pattern 5
#n = int(input("enter a number"))
#for i in range(1,n+1):
#    print(" "*(n-i),end=" ")
#    print("*" * (2 * i-1))

#     *
#    ***
#   *****
#  *******
# *********

#pattern 6
#n = int(input("enter a number"))
#for i in range(n,0,-1):
#    print(" "*(n-i),end=" ")
#    print("*" * (2 * i-1))

# *********
#  *******
#   *****
#    ***
#     *

#pattern 7
#n = int(input("enter a number"))
#for i in range(1,n+1):
#    print(" "*(n-i),end=" ")
#    print("*" * (2 * i-1))


#for i in range(n-1,0,-1):
#    print(" "*(n-i),end=" ")
#    print("*" * (2 * i-1))

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#   ***
#    *