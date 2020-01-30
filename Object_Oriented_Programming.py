class Employee:
    def __init__(self, ename, esalary, arole):
        self.name = ename
        self.sal = esalary
        self.role = arole


    def printdetail(self):
        return f"Name is {self.name} Salary is {self.sal} and role is {self.role}"
    pass


hanad = Employee("Hanad", 100000, "Data Scientist")
kamil = Employee("Kamil", 100000, "Manager")

print(hanad.name)
print(hanad.__dict__)
print(kamil.__dict__)
# hanad.name= "Hanad"
# hanad.sal= 100000
# hanad.role = ("Data Scienctist")
#
# kamil.name = ("Kamil")
# kamil.sal = (100000)
# kamil.role = ("Manager")
#
# print(hanad.name)
# print(hanad.sal)
# print(hanad.role)
# print(kamil.name)
# print(kamil.sal)
# print(kamil.role)
# print(hanad.__dict__)
# print(kamil.__dict__)
# print(hanad.printdetail())
# print(kamil.printdetail())