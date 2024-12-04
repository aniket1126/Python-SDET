word = input("enter a string")
occur = {}
for i in word:
    if i in occur:
        occur[i]+=1
    else:
        occur[i]=1

for i in word:
    if occur[i] == 1:
        print(i)
        break


