
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


list2=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]
for n,i in enumerate(list2):
   if i==1:
    list2[n]=10
print(list2)




