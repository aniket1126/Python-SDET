#anagrams
n1 = input("enter 1st word")
n2 = input(("enter 2nd word"))
if len(n1) == len(n2):
    if sorted(n1) == sorted(n2):
        print("the str is anagram")
    else:
        print("not anagram")
