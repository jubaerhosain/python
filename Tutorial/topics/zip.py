subjects = []
for _ in range(3):
    subjects.append(map(float, input().split()))

print(list(zip(*subjects)))

for marks in zip(*subjects):
    print(round(sum(marks)/len(marks), 1))

# From hackerrank
# 1 2 3 4 5 6 7 87
# 3 4 56 6 7 7
# 2 43 5  6 7 78 8
