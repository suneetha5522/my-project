"""
create a class for family members
1.add a method for family members are the in family class
2. Remove one family member with ID
"""


class Family:

    def __init__(self):
        """
        creating the constructor for the class
        """
        self.family = []

    def add_member_family(self, name, age, mid):
        """
        adding the member to family list
        :param name: variable
        :param age: variable
        :param mid: variable
        :return: appending the variables to family list
        """
        d = {"name": name, 'age': age, "id": mid}
        self.family.append(d)
        return True

    def no_of_families(self):
        """
        finding the how many families are present in the list of families
        :return: length of the family
        """
        return len(self.family)

    def remove_one_family_by_id(self, mid):
        """
        deleting the one family by using the ID
        :param mid: id in family class
        :return: deleted family by id
        """

        for i, d in enumerate(self.family):
            if d.get("id", mid) == mid:
                del i
                return d

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
print("The deleted family by using id:", z)
