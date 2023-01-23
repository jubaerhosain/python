# num = [int(x) for x in input().split()]
# print(num)

x = int(input())

# works in hackerrank, "zipped" problem
subjects = (map(float, input().split()) for _ in range(x))
print(subjects)
