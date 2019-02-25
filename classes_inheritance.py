"""
create a class for family
1.How many family members are the in family class
2. Remove one family member with ID
"""


class Family:
    total_family = 0

    '''
    Constructor of family class
    '''
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        Family.total_family = Family.total_family+1
    '''
        method for counting the total families present in the class
    '''
    def display_count(self):
        print("Total family members = %d" % Family.total_family)

        '''
        method for Displaying the family with fileds
        '''

    def display_family(self):
        print(f"family: {Family.total_family}", "Name:", self.name, "age:", self.age, "id:", self.id)

# creating the instances of the class family

family_1 = Family("Charan", 23, 78899)
family_1.display_family()
family_2 = Family("Ram", 43, 57899)
family_2.display_family()
family_3 = Family("Santosh", 45, 5798)
family_3.display_family()
print("Total families are:", Family.total_family)
