def fn(*args):
    print(type(args))
    print(len(args))
    print(args[1])
    print(args)


def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)


# fn(3, 2, 3, 4)
print("Factorial: ", factorial(10))


def f(*arg):
    print(arg)


a = [1, 3]
b = [3, 4]
c = [5, 7]
x = [a, b, c]
f(*x)
print(*x)

# Learn *arg vs **arg
