# craeting an empty set
a = set()
print(type(a))
## accesing the element
# adding an value in empty set
a.add(4)
a.add(5)
# a.add(5) adding a repadetly value cannnot change a set 
a.add(5)
a.add((5,4,6))
# a.add({5,4,6}) cannot add list or dictonary in set

print(a)
## lenth of set
print(len(a)) #print the lenth of this set
## remove from set
a.remove(5)# remove 5 from set(a)
#a.remove(15) # throws an error while try to remove from set (which is not present in set)
print(a)

a.pop()
print(a)
