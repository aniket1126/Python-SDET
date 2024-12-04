#Check if two strings are anagrams
n= input("enter a string")
n1 = input("enter 2nd string")
if len(n) == len(n1):
    if sorted(n) == sorted(n1):
        print("the string is anagram")
    else:
        print("ther string is not anagram")
