if __name__ == '__main__':
    x = 5
    grid = [i for i in range(x)]
    print(grid)
    grid = [[i, j] for i in range(x) for j in range(3)]
    print(grid)
    grid = [[i, j] for j in range(3) for i in range(x)]
    print(grid)

