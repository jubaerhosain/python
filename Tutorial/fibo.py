prev1 = 0
prev2 = 1
current = 0

n = int(input())

for _ in range(2, n+1):
    current = prev1 + prev2
    prev1 = prev2
    prev2 = current

print(len(str(current)))

print(current)
