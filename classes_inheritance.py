"""
create a class for Person details
1.How many family members are the in family class
2. Remove one family member with ID
"""


class Person:
    total_Persons = 0

    '''
    Constructor of Person class
    '''
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        Person.total_Persons = Person.total_Persons+1
    '''
        method for counting the total persons present in the class
    '''
    def display_count(self):
        print("Total family members" % Person.total_Persons)

        '''
        method for Displaying the person details with fields
        '''

    def display_person_details(self):
        print(f"person: {Person.total_Persons}", "Name:", self.name, "age:", self.age, "id:", self.id)

# creating the instances of the class family


person_1 = Person("Charan", 23, 78899)
person_1.display_person_details()
person_2 = Person("Ram", 43, 57899)
person_2.display_person_details()
person_3 = Person("Santosh", 45, 5798)
person_3.display_person_details()
print("Total persons are:", Person.total_Persons)
