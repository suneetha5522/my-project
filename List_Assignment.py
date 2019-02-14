'''Remove all Nones in to string without using for loop'''
#Input values given to list
list1=[1,2,3,None,"ram","Ramesh",24,56,None,10]
res=list1.index(None)    #finding the None in List1
list1.remove(None)             #Deleting the None in list1
list1.insert(res,"string")     #updating  First None with String
print(list1)

res1=list1.index(None)    #finding the None in List1
list1.remove(None)             #Deleting the None in list1
list1.insert(res1,"string")    #updating Second None with String
print(list1)





