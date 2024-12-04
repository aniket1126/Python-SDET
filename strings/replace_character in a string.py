change = input("enter a str")
char1 = input("enter a str to replace")
char2 = input("enter new aplhabet to replace")
n = ""
for i in change:
    if i == char1:
       i = char2
       n+=i
    else:
       n+=i
print(n)



