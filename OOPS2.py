class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def newmethod(cls, string):
        params = string.split(",")
        # return cls(params[0], params[1])
        return cls(*string.split(","))
    @staticmethod
    def pr():
        print("This is a static Method")


hanad = Employee("Hanad", 100000)
kamil = Employee.newmethod("kamil,100000")

print(hanad.name)
print(hanad.salary)
print(kamil.name)
print(kamil.salary)
kamil.pr()