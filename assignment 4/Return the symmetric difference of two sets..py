#Return the symmetric difference of two sets.
set1=set(map(int,(input("enter the set1").split(","))))
set2=set(map(int,(input("enter the set1").split(","))))
print(set1^set2)
print(set1.symmetric_difference(set2))