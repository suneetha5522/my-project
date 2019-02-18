# In list of dictionaries sort the name and age
# initializing the dictionary values into list
person_dict = [
    {'name': "arjun", 'age': 23, 'gender': "male"},
    {"name": "ramesh", "age": 44, "gender": "male"},
    {"name": "nagesh", "age": 34, "gender": "male"},
    {"name": "suneetha", "age": 27, "gender": "female"}]

print("The sorted list by names:", sorted(person_dict, key=lambda by_name: by_name['name']))
print("The sorted list by ages:", sorted(person_dict, key=lambda by_age: by_age['age']))


# What is the difference between the copy, deep copy and shallow copy :-
"""in general copy we use = operator to create a copy of an object. This will not 
 creates a new object. It only creates a new variable that shares the 
 reference of the original object"""
my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = my_dict
new_dict['d'] = 4                       # updating values to new_dict
print('my_dict:', my_dict)
print('ID of my_dict:', id(my_dict))
print('new_dict:', new_dict)
print('ID of my_dict:', id(new_dict))

# shallow copy():-
"""
A shallow copy creates a new object which stores the reference of the original elements.
So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. 
This means, a copy process does not create copies of nested objects itself
"""
person_dict1 = [
    {'name': "arjun", 'age': 23, 'gender': "male"},
    {"name": "ramesh", "age": 44, "gender": "male"},
    {"name": "nagesh", "age": 34, "gender": "male"},
    {"name": "suneetha", "age": 27, "gender": "female"}]
new_person_dict1 = person_dict1.copy()
print('person_dict1:', person_dict1)
print('ID of person_dict1:', id(person_dict1))
print('new_person_dict1:', new_person_dict1)
print('ID of new_person_dict1:', id(new_person_dict1))

# adding to person_dict1

person_dict1.append({'name': "suresh", 'age': 45, 'gender': "male"})
print('person_dict1:', person_dict1)
print('new_person_dict1:', new_person_dict1)

# if we want to change the value with in the dictionary :-
person_dict1[0]["name"] = "surekha"     # it is updating to old and new list
print('person_dict1:', person_dict1)
print('ID of person_dict1:', id(person_dict1))
print('new_person_dict1:', new_person_dict1)
print('ID of new_person_dict1:', id(new_person_dict1))

""" deep copy():-A deep copy creates a new object and recursively adds the copies of nested objects present 
in the original elements"""

person_dict2 = [
    {'name': "arjun", 'age': 23, 'gender': "male"},
    {"name": "ramesh", "age": 44, "gender": "male"},
    {"name": "nagesh", "age": 34, "gender": "male"},
    {"name": "suneetha", "age": 27, "gender": "female"}]

new_person_dict2 =



