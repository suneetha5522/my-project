#Set Methods with examples

#can set allow duplicates
set1={22,33,44,11,22,33,44,55,66}
print(set1)
#print(dir(set1))
#Initialization of set in different ways
set2=set("hello good morning")
set2={1,2,3,4,5,2,6,1}
print(set2)
y=(set("hellogoodmorning"))
print(y)
#is sets allow tuples and lists
x=set((("apple"),("orange"),("banana")))
#z=set(([1,2,3],[3,5,6]))
print(x)

#frozen set
b=frozenset((1,2,3,4,5))
print(x)


'''Set operations
Add(Element):-
A method which adds an element, which has to be immutable, to a set.'''

set1={"apple","orange","banana"}
set1.add("guva")
print(set1)

'''clear()
All elements will removed from a set'''

set1.clear()
print(set1)

'''Copy
Creates a shallow copy, which is returned'''
fruits={"guva","orange","banana"}
fruits_backup=fruits.copy()
#fruits_backup=fruits
fruits.clear()
print(fruits)
print(fruits_backup)

'''difference()
This method returns the difference of two or more sets as a new set'''
s1={1,2,3,2,3,4,5,6,7,8}
s2={0,3,4,6}
s3={45,67}
print(s1.difference(s2).difference(s3))
#print(s1-s2-s3)

'''difference_update()
The method difference_update removes all elements of another set from this set. x.difference_update(y) is the same as "x = x - y" '''
print(s2.difference_update(s1))

'''discard(el)
An element el will be removed from the set, if it is contained in the set. If el is not a member of the set, nothing will be done.'''

s1.discard(10)
s1.discard(7)
print(s1)

'''remove()
works like discard(), but if el is not a member of the set, a KeyError will be raised'''
s1.remove(1)
#s1.remove(20)
print(s1)

'''intersection()
Returns the intersection of the instance set and the set s as a new set. In other words: A set with all 
the elements which are contained in both sets is returned'''

x={"a","b","c","d"}
y={"c","d"}
z={"e","f"}
print(x.intersection(y))
print(z&y)

'''isdisjoint() - This method returns True if two sets have a null intersection'''
print(y.isdisjoint(x))
#print(x=y)



'''issubset()-x.issubset(y) returns True, if x is a subset of y. "<=" is an abbreviation for "Subset of" and ">=" for "superset of" 
"<" is used to check if a set is a proper subset of a set'''

print(y.issubset(x))
print(y<=x)

'''issuperset():- x.issuperset(y) returns True, if x is a superset of y. ">=" is an abbreviation for "issuperset of" 
">" is used to check if a set is a proper superset of a set'''

print(y.issuperset(x))
print(x>y)

'''pop():- pop() removes and returns an arbitrary set element. The method raises a KeyError if the set is empty'''
print(x.pop())
print(x)
print(x.pop())
print(x)

















