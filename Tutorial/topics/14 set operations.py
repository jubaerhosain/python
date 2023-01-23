# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = int(input())
set1 = set(map(int, input().split()))

_ = int(input())
set2 = set(map(int, input().split()))

# (AuB) = (A) + (B) - (AnB)
ans = sorted(list(set1 ^ set2))
[print(num) for num in ans]
