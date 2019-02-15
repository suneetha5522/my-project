"""
Dictionaries:-
Dictionaries and lists share the following characteristics:
•Both are mutable.
•Both are dynamic. They can grow and shrink as needed.
•Both can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can
 also contain a list, and vice versa.

Dictionaries differ from lists primarily in how elements are accessed:
•List elements are accessed by their position in the list, via indexing.
•Dictionary elements are accessed via keys.
"""

# Defining:-

dict1 = {'name': "nagesh", 'age': 30, 'gender': 'male'}
print("The Dictionary-1 values are:", dict1)

'''Initializing using constructor:
If the key values are simple strings,we can be specified as keyword arguments '''

dict2 = dict(name='ramesh', age=32, gender='male')
print("The Dictionary-2 values are:", dict2)

dict3 = dict([("name", 'suni'), ("age", 27), ("gender", 'female')])
print("The Dictionary-2 values are:", dict3)

# Accessing Dictionary Values
print("Accessing name from dictionaries:", dict1["name"])
print("Accessing age from dictionaries:", dict1.get("age"))

# Accessing the keys & items from dictionary
print("Accessing keys from dict2 :", dict2.keys())
print("Accessing items from dict2 :", dict2.items())

# Add a key and value to existing dict2
dict2["id"] = 3456
print("The new Dictionary is:", dict2)

# Update an entry, you can just assign a new value to an existing key in dict2
dict2["name"] = "ram"
print("updating key value name:", dict2)

# del statement, specifying the key to delete in dict2
del dict2["age"]
print("Deleting the specified key from dict2:", dict2)

# The length of the dict2
print("The length of the dict2:", len(dict2))
print("The type of dict2:", type(dict2))

# Creating a empty dictionary with curly braces
dict4 = dict()
dict4["name"] = "charan"
dict4["age"] = "23"
dict4["children"] = ["ravi", "mani", "hari"]
dict4["pets"] = {"dog": "Fido", "cat": "Sox"}
print("The Dictionary-4 :", dict4)
print("The name in dictionary:", dict4["name"])
print("The children in dict4:", dict4["children"])
print("Last element in sub list children :", dict4["children"][-1])
print("Last item in sub dict in pet :", dict4["pets"]["cat"])

# Built-in Dictionary Methods
# Clear():- Clears the dictionary

dict5 = {'a': 10, 'b': 20, "c": 30}
print("printing the dict-5:", dict5)
# print("clearing the dict-5:", dict5.clear())


'''get(<key>[, <default>]):- provides a convenient way of getting the value of a key from a dictionary without 
checking ahead of time whether the key exists, and without raising an error'''
print("printing the key values in dict5:", dict5.get("a"))
print("printing the keys values not there in dict-5:", dict5.get("e", "not there in dict5"))





