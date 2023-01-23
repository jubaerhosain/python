x = "one"
y = "two"


def f1():
    x = "fantastic"


def f2():
    global y
    y = "fantastic"


f1()
f2()

print("Python is " + x)
print("Python is " + y)


























