class myClass:
    # cannot be seen from outside
    __privateVar = 27

    def __init__(self, x):
        self.x = x
        self.__private = 3

    # cannot be seen from outside
    def __privMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        print("Private Variable value: ", myClass.__privateVar)
        myClass.__privMeth(self)
        self.__privMeth()


foo = myClass(5)
foo.hello()

# cannot access from outside
# foo.__privMeth()
# foo.__private

# all self variables can be seen from here
print(foo.__dict__)
print(foo._myClass__private)

print(myClass.__dict__)

