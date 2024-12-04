#the string is anagram or not
a1= input("enter a number")
a2= input("enter a number")
if len(a1) == len(a2):
    if (sorted(a1) == sorted(a2)):
        print("its anagram")
    else:
        print("its not anagram")