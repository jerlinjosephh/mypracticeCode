class Parent:
    def __init__(self, firstName, lastName) -> None:
        self.fname = firstName
        self.lname = lastName
    def printName(self):
        print(self.fname, self.lname)

class Child(Parent):
    pass
x = Child("Jerlin", "Joseph")
x.printName()
        