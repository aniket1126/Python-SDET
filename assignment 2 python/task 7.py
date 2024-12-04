#Write a program that accepts a username and password
#from the user and checks if they match the pre-set username and password
n = input("enter username")
n1 = input("enter password")
username = "aniket"
password = "ansh"
if n == username  and n1 == password:
    print("The credentials are matched")
else:
    print("The credentials are wrong! try again")
