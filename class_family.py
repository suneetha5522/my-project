"""
create a class for family members
1.add a method for family members and find no of families
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
        :param name: string,name of the person
        :param age: integer,age of the person
        :param mid: integer,id if the person
        :return: dictionary
        """
        d = {"name": name, 'age': age, "id": mid}
        self.family.append(d)
        return True

    def no_of_families(self):
        """
        finding the total no of families are present in the list
        :return: integer,total no of families
        """
        return len(self.family)

    def remove_one_family_by_id(self, mid):
        """
        delete the one family by using the ID
        :param mid: integer, id of the family class
        :return: boolean, True or False
        """

        for i, d in enumerate(self.family):
            if d.get("id", mid) == mid:
                del self.family[i]
                return True


x = Family()
x.add_member_family("charan", 23, 12345)
x.add_member_family("ravi", 25, 123456)
x.add_member_family("kumar", 27, 123457)
x.add_member_family("nagesh", 30, 1234556)
x.add_member_family("suneetha", 23, 12345568)
print("The families are:", x.family)

y = x.no_of_families()
print("The total no.of families are:", y)
#print(x.family)
z = x.remove_one_family_by_id(12345)
#print(x.family)
print("The deleted family by using id:", z)
