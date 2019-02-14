#Replace None with String of index value 8 in list
list1=[1,2,3,4,5,6,7,None,8,9,10]
list1[7]="String"       #updating value with String
print("The Updating list is:",list1)


#In list all 1's are chnages to None
list2=[1,2,3,1,2,3,1,2,3]
res1=list2.index(1)             #finding the index if 1st one
list2[res1]="None1"             #updating to None1
res2=list2.index(1)                #Finding the index of 2nd one
list2[res2]="None2"               #updating to None2
res3=list2.index(1)             #Finding the index of 3nd one
list2[res3]="None3"                #updating to None3
print("The updated list is:",list2)









