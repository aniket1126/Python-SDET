#set is unordered collection
#set is mutable(but not elements)
#myset = {1,2,3}
#print(myset)

#myset = {1,2,3,3,4,4,5}
#print(myset)
#myset = {1,2,3}
#myset.add(4)
#print(myset)

#myset = {1,"hello",(3,4)}
#print(myset)

#myset = {1,"hello",[3,4]}
#print(myset)

#create set
#myset = {"apple,cherry"}

#acessing the element
myset = {1,2,3,4}
#for i in myset():
#    print(i)
#set1 = {"mango","cherry"}
#myset.update(set1)
#print(myset)


#remove from set
#remove
#discard
#myset.remove(5)
#print(myset)
#myset.discard(5)    differnce in remove and discard is remove gives error if the element is not in the set and discard dont show error
#print(myset)


#clear = delete the item of te set
#empty = delete the set

#operator on sets
set1 = {1,2,3}
set2 = {3,4,5,6}
#print(set1|set2)
#print((set1.union(set2)))

#print(set1&set2)
#set1.intersection(set2)

#differnce
#print(set1-set2)
print(set1.difference(set2))

#symmetric differnce            dont print common element,print unique elemnts
#print(set1^set2)
#print(set1.symmetric_difference(set2))

#frozen set                these are immutable version of sets.once
#frozenset1 = frozenset([1,2,3])
#print(frozenset1)


#list conversion into set
#mylist = [1,2,3,4,4,5]
#myset = set(mylist)
#print(myset)








