class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year_of_graduation = year

    def printname(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.year_of_graduation)


student = Student("Md. Jubaer", "Hosain", 2024);
student.printname()
