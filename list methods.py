
#print(dir(list))

#append Method:-

fruits=["orange","grape","apple","guva","apple"]
fruits.insert(2,"banana")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits1=["pine apple","watermelon"]
fruits2=("mosamber","mustmelon")
fruits.append("lemon")
fruits.append(fruits1)
fruits.append(fruits2)
print("updated list:",fruits)
print(len(fruits))
index=fruits.index(["pine apple","watermelon"])
print(index)
#print(fruits.clear())
#del fruits [:]
print(fruits.count("apple"))
print(fruits.remove("apple"))
print(fruits.pop(0))
print(fruits)

#extend:-

l1=[1,2]
l2=[3,4,5,6,7]
l1.extend(l2)
print(l1)


#copy():-

list=["suneetha","nagesh","charan"]
new_list=list.copy()
new_list.append("mani")
print(new_list)
new_list1=list[:]
new_list.append("rajini")
print(new_list)




"""__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
 '', '', '', '', '', '', '', '', '', '', ''"""
