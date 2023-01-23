# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = int(input())
set1 = set(map(int, input().split()))

_ = int(input())
set2 = set(map(int, input().split()))

union = set1.union(set2)
intersection = set1.intersection(set2)

difference = union.difference(intersection)

for i in sorted(difference):
    print(i)