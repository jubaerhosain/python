print(range(1, 5))
print(*range(1, 5))
print(type(range(1, 5)))
print("".join(map(str, range(1, 6))))

print("-".join(["a", "bcd", "efg"]))

# prints 12345
print(*range(1, 6), sep="")
