"""
create a class for family members
1.add a method for family members are the in family class
2. Remove one family member with ID
"""


class Person:

    def __init__(self):
        self.person = []

    def add_person(self, p1, p2, p3):
        """
        :param p1: person 1 details as a dictionary
        :param p2: person 2 details as a dictionary
        :param p3: person 3 details as a dictionary
        :return: p1,p2,p3
        """
        self.person.append(p1)     # appending the person1 details
        self.person.append(p2)     # appending the person 2 details
        self.person.append(p3)     # appending the person 3 details
        print("no of families present in the class", len(self.person))   # getting the length of list of dictionaries
        self.person.pop()        # deleting the particular ID with details


x = Person()

# creating the attributes

x.add_person({'name': "charan", 'age': 23, 'id': 345678},
             {'name': "kumar", 'age': 33, 'id': 122365},
             {'name': "ravi", 'age': 25, 'id': 458511})

x.add_person({'name': "rajini", 'age': 23, 'id': 345678998},
             {'name': "naresh", 'age': 33, 'id': 12236789},
             {'name': "suresh", 'age': 25, 'id': 458579898})

print("The list if family details are", x.person)
