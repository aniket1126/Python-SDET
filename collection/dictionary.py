#dictionary = key , value pairs {"abc":10,'xyz',20}
#ordered, changable , and indexed
#key must be unique , must be immutable
#value = can be of any type
from email.policy import default
from os import remove
from traceback import print_tb

from collection.set import myset

#create dictionary
#mydict = {}
#print(mydict)

#mydict = {"name":"aniket","age":23,"address":"ambala"}
#rint(mydict)

#using list of tuples                    list is not possible because list is mutuable
#mydict =dict([("name","aniket"),("age",23),("address","ambala")])
#print(mydict)

#using dict() constructor
#mydict = dict(name="aniket",age="23")
#print(mydict)

#acessing the element
#print(mydict["name"])
#print(mydict["age"])
#print(mydict["dept"])

#using get method
#print(mydict.get("name"))
#print(mydict.get("age"))

#modifying dictionary (add or delete a complete pair)
#print(mydict)
#mydict ["age"] = 31
#print(mydict)

#delete key value pair
#del mydict["age"]
#print(mydict)

#pop method
#mydict.pop("name")
#print(mydict)
#mydict.popitem()
#print(mydict)

#method of dictionary
#key()  return the object of all the keys/only set of keys
#print(mydict.keys())
#print(mydict.values())

#item()
#print(mydict.items())

#update   inserting multiple values in dictionary
#mydict2 = {"dept":101,"city":"ambala"}
#mydict2.update(mydict)
#print(mydict2)

#copy
#mydict2=mydict.copy()
#print(mydict2)

#from keys        (create the copy of dictionary with specified key and a single value)
#keys = [1,2,3,4]
#default_value = "welcome"
#mydic = dict.fromkeys(keys,default_value)
#print(mydic)

#set default
#mydict.setdefault("age":21)
#print(mydict)

#using loop
#for i in mydict:
#    print(i)

#iterate over values
#for i in mydict.values():
#    print(i)

#for keys,values in mydict.items():
#    print(f"{keys}:{values}")

#dicntionary comprehension
#{0:0,1:1,2:4}
#square = {x: x**2 for i in range(0,11)}
#print()

#nested dictionarty
#mydic4 = {
#"person1":{"name":"bob","age":23},
#"person2":{"name":"bob","age":21},
#}
#print(mydic4["person1"]["name"])
#print(mydic4["person2"]["age"])


#merging dictionary using union operator
#dic5 = {"a":1,"b":2,"c":3}
#dic6 = {"a":1,"E":2,"F":3}


#mydic5 = {"name":"aniket","age":23}
#mydic6 = {"name":"aniket","dept":"it"}
#a = set(mydic5.values())
#b = set(mydic6.values())
##same = a&b
#p#rint(same)

#mydic5 = {"name":"aniket","age":23}
#a = set(mydic5.keys())
#print(a)

#mydic5 = {"name":"aniket","age":23,"name":"aniket"}
#a = set(mydic5.values())
#print(a)

##mydic5 = {"name":"aniket","age":23}
#a= {"name":"aniket"}


#update the key and value
#mydic = {"name":"aniket","score":85,"emma":97}
#mydic2 = {"emma":76}
#m#ydic.update(mydic2)
#print(mydic)

#sum of value
#mydic = {"a":2,"b":4,"c":97}
#for i in mydic.values():
#  a=  sum(mydic.values())

#print(a)

#tuple to list covert in ans
#tuple1 = (2,4,6,8,10)
#a = list(tuple1)
#a.append(12)
#print(a)
#b = tuple(a)
#print(b)

# code to remove the min and max value from set
#list = {10,20,30,56,40}
#min = float('inf')
#max = float('-inf')
#for i in list:
#    if i < min:
#        min = i
#    if i > max:
#        max = i

#list.remove(min)
#list.remove(max)
#print(list)

#symmetric values
#set1 = {1,2,3,3}
#set2 = {3,4,5}
#set1=set(map(int,(input("enter the set1").split(","))))
#set2=set(map(int,(input("enter the set1").split(","))))
#print(set1^set2)
#print(set1.symmetric_difference(set2))

#
#mylist = [1,2,3,2,4,2]
#idx=[]
#for i in range(0,len(mylist)):
#    if mylist[i] == 2:
#        idx.append(i)

#print(idx)


dic = {"a":"aniket","age":23,"b":"aniket","dept":"it"}
list=[]
for i,j in dic.items():
    if j=="aniket":
        list.append(i)

print(list)















