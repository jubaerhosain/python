def my_decorator(to_be_decorated):
    def inner():
        print("before decoration")
        to_be_decorated()
        print("after decoration")

    return inner


# same code is written using @wrapper
# def my_func():
#     print("decorated")
#
#
# my_func = my_decorator(my_func)
# my_func()

@my_decorator
def my_func():
    print("decorated")


my_func()
