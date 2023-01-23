def wrapper(fn):
    def fun(l):
        # complete the function
        fn([f"+91 {p[-10:-5]} {p[-5:]}" for p in l])

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)