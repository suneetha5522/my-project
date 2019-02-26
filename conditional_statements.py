"""
Types of conditional statements:
3.comparision operators are <,>,==,!=
4. logical operators are and,or,not
5.bitwise operators are OR,XOR,NOR
6.identity operators are is, is not
7.membership operators are inn not in

"""
# Example - 1:-

x, y = 5, 2
print("sum of numbers", x + y)              # addition of two numbers
print("multiplication", x * y)               # Multiplication of numbers
print("subtraction", x - y)                 # Subtraction of numbers
print("Square root", x ** y)                # square root of numbers
print("division", x/y)                      # Division of numbers
print("Modular", x%y)                       # It will give remainder
print("Mod", x//y)                          # If decimal is there it will rounding the number

# Example - 2 - Finding the odd and even numbers in given list
list1 = [1, 2, 5, 6, 7, 8, 9, 3, 5, 7, 8, 9, 33, 77, 88, 55, 44, 99, 100]
for each in range(len(list1)):
    if each % 2 == 0:
        print("The Even Numbers are:", each)
    else:
        print("The Odd Numbers are:", each)

# find 22 is there in given list
list3 = [11, 22, 33, 44]
for each in list3:
    if each == 22:
        print("true")
    else:
        print("false")
        break

# example on if elif and else conditions
a, b = 6, 5
if a > b:
    print("a is max")
elif b > a:
    print("b is max")
else:
    print("both are equal")


# Example - 3 - generating the run time list by using loops

list2 = []
for each in range(20):
    if each % 2 == 0:                 # finding Even numbers in given range
        list2.append(each)          # Appending Even Numbers to list
print("The Even Numbers in list:", list2)

# Example - 4 - Generating run time tuple
tuple1 = []
for i in range(10):
    if i % 2 != 0:
        tuple1.append(i)
tuple1 = tuple(tuple1)
print(f"The odd numbers are in tuple format", tuple1)


# Example - 5 - Generating the run time set:-

set1 = set()
z = list(set1)
for each in range(0, 6):
    z.append(each)
print("0-5 numbers are in set", set(z))

# Generating the runtime dictionary:-

key = int(input("Enter the key (int) to be added:"))
value = int(input("Enter the value for the key to be added:"))
d = {}
d.update({key: value})
print("Updated dictionary is:", d)


# find how many times duplicates are repeated in given list
list1 = [1, 2, 3, 2, 2, 2, 3, 2]
list2 = []
for each in list1:
    if each not in list2:
        print("{} is repeated {} times".format(each, list1.count(each)))
    list2.append(each)


# delete the all 1's in given list using while loop

x = [1, 2, 3, 1, 1, 4, 1]
while x.count(1):
    x.remove(1)
    print("The list after deleting 1's", x)

# printing the two subsequent number ony by one in list
my_list = [11, 22, 33,  44, 55]
for each in range(0, len(my_list)):
    if each+1 == len(my_list):
        print(f"The Sub sequent list are",my_list[each], ",", 0)
    else:
        print(f"The Sub sequent list are", my_list[each], ",", my_list[each+1])


























