def _():
    count = 0

    def inner():
        nonlocal count
        count = count + 1
        return count

    return inner


increment = _()
print(increment())
print(increment())
print(increment())
print(increment())
print(increment())
