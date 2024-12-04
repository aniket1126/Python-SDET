#create the string
#s = 'aniket'
#s="aniket"
#s=str("aniket")
#s=str('aniket')

#create empty string
#name = ''
#name = ""
#name = str()

#immutable string example (
#name = "aniket"
#print(name)
#name[3] ="x"
#print(name)

#check the address of the string
#message = "aniket"
#print(id(message))               ans is 1491582101872
#message = message+"to pyhton"
#print(id(message))              ans is  1491582250736

# + and * with string
#str = "welcome"
#print(str + " to the world")        ans is welcome to the world

#print(str*2)                        ans is  welcomewelcome

#slicing
#str = "welcome"
#print(str[1:3])          ans is el
#print(str[:6])            ans is welcom
#print(str[2:])             ans is lcome
#print(str[1:-2])           ans is  elco
#print(str[-4:-1])          ans is com

#ord() and chr()
#  ord (return the ASCII CODE OF THE CHARCTER)
#print(ord('A'))             ans is 65
#print(ord('b'))              ans is 98
#print(chr(65))                ans is A

#max() , min() , len()
#print(max("abc"))                ans is c
#print(min("abc"))                 ans is a
#print(len("abc"))                 ans is 3

# in, not in operator
#str = "welcome"                    (combination is there to be true)
#print("come" in str)                ans is True
#print("come" not in str)            ans is False  (not is opposite of in)

#string comparison
#print("tim"=="tie")                  ans is False
#print("Free"!="Freedom")             ans is True
#print("arrow">"aron")                ans is True
#print("teeth"<"tee")                 ans is False
#print("yellow"<="fellow")            ans is False
#print("abc">' ')                     ans is True
#print("aniket">"jangra")             ans is False

#testing string
#s = "welcome"
#print(s.isalnum())                    ans is True
#print(len(s))7
#print('welcome to bebo'.isalpha())    ans is False
#print("2012".isdigit())                ans is True
#print(s.isidentifier())                ans is True
#print('if'.isidentifier())             ans is True
#print(s.islower())                     ans is True
#print("WELCOME".isupper())             ans is True
#print(" ".isspace())                    ans is True

#searching in the string
#s = "welcome to bebo"
#print(s.endswith("bo"))                       ans is True
#print(s.startswith("wel"))                    ans is True
#print(s.find("come"))                          ans is 3
#print('hcome'.find("hello"))                   ans is -1
#print(s.count("o"))                            ans is 3
#print(s.count(" "))                            ans is 2


#converting string
#s ="string in python"
#print(s.capitalize())
#print(s.title())
#print("WELCOME".lower())
#print(s.upper())
#print(s.swapcase())
#print("hello".swapcase())
#print(s.replace(_old:"in", _new:"on"))
#print(s.replace(__old="py",__new="on"))

#revese a string in python
#s="welcome"
#rev_str=""
#for i in s:                                    (method 1)
#    rev_str=i+rev_str
#    print("the reverse string is ",rev_str)

#method 2
#rev_str=s[::-1]
#print(rev_str)


#rev = a[::-1]
#if a == rev:
#    print("is plaendrome")
#else:
#    print("is not palendrome")








