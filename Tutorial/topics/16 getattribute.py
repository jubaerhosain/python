n = int(input())
s = set(map(int, input().split()))

N = int(input())
for i in range(N):
    attribute, *args = input().split()
    print(len(s))
    try:
        getattr(s, attribute)(*map(int, args))
    except KeyError:
        pass

print(sum(s))

# see: 0 asterisk variable.py
