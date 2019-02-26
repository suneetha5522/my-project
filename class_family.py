"""
create a class for family members
1.add a method for family members are the in family class
2. Remove one family member with ID
"""


class Family:

    def __init__(self):
        self.family = []

    def add_member_family(self, name, age, mid):
        d = {"name": name, 'age': age, "id": mid}
        self.family.append(d)
        return True

    def no_of_families(self):
        return len(self.family)

    def remove_one_family_by_id(self, mid):
        self.family.pop(1)
        return mid


x = Family()

x.add_member_family("charan", 23, 12345)
x.add_member_family("ravi", 25, 123456)
x.add_member_family("kumar", 27, 123457)
x.add_member_family("nagesh", 30, 1234556)
x.add_member_family("suneetha", 23, 12345568)
print("The familes are:", x.family)

y = x.no_of_families()
print("The total no.of families are:", y)

z = x.remove_one_family_by_id(12345)
print("The deleted is is:",z)










