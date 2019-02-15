# In list of dictionaries sort the name and age
# initializing the dictionary values into list
person_dict = [
    {'name': "arjun", 'age': 23, 'gender': "male"},
    {"name": "ramesh", "age": 44, "gender": "male"},
    {"name": "nagesh", "age": 34, "gender": "male"},
    {"name": "suneetha", "age": 27, "gender": "female"}]

print("The sorted list by names:", sorted(person_dict, key=lambda by_name: by_name['name']))
print("The sorted list by ages:", sorted(person_dict, key=lambda by_age: by_age['age']))






