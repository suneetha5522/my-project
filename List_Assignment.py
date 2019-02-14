#Replace None with String in list
list1=[1,2,3,4,5,6,7,None,8,9,10]
list1[7]="String"       #updating value with String
print("The Updating list is:",list1)


#In list all 1's are chnages to None
list2=[1,2,3,1,2,3,1,2,3]
res1=list2.index(1)             #finding the index is 1st one
list2.remove(1)                 #Removing the 1st one
list2.insert(res1,None)         #inserting 1 with None
#print(list2)

res2=list2.index(1)             #finding the index is 1st one
list2.remove(1)                 #Removing the 1st one
list2.insert(res2,None)         #inserting 1 with None
#print(list2)

res3=list2.index(1)              #finding the index is 1st one
list2.remove(1)                  #Removing the 1st one
list2.insert(res3,None)          #inserting 1 with None
print("The updating List is :",list2)











