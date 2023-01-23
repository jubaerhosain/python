class MyClass:
    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return "self"

    def greet(self):
        print(f"Hello {self.x}")


my_class = MyClass(5)
# print(my_class.x)
# my_class.greet()
del my_class.x
print(my_class)
my_class.greet()
