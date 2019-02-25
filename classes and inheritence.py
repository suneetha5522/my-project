class Family:
    total_family = 0

    def __init__(self, name, age, fid):
        self.name = name
        self.age = age
        self.id = fid
        Family.total_family = Family.total_family+1

    def display_count(self):
        print("Total family members = %d" % Family.total_family)

    def display_family(self):
        print(f"The Family {Family.total_family}:", "Name:", self.name, "age:", self.age, "id:", self.fid)


family_1 = Family("Charan", 23, 78899)
family_1.display_family()
family_2 = Family("Ram", 43, 57899)
family_2.display_family()
family_3 = Family("Santosh", 45, 5798)
family_3.display_family()
print("Total families are:", Family.total_family)
print("Total families are:", Family.total_family)
