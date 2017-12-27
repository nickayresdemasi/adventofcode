def build_graph():
    grid = {}
    grid[(0, 0)] = 1
    x, y = 1, 0
    grid[(x, y)] = 1
    while True:
        while x != y:
            y += 1
            grid[(x, y)] = calculate_value(grid, x, y)
            print("({}, {}) = {}".format(x, y, grid[(x, y)]))
            if grid[(x, y)] > 361527:
                print(grid[x, y])
                break
        while -x != y:
            x -= 1
            grid[(x, y)] = calculate_value(grid, x, y)
            print("({}, {}) = {}".format(x, y, grid[(x, y)]))
            if grid[(x, y)] > 361527:
                print(grid[x, y])
                break
        while x != y:
            y -= 1
            grid[(x, y)] = calculate_value(grid, x, y)
            print("({}, {}) = {}".format(x, y, grid[(x, y)]))
            if grid[(x, y)] > 361527:
                print(grid[x, y])
                break
        while -x != y:
            x += 1
            grid[(x, y)] = calculate_value(grid, x, y)
            print("({}, {}) = {}".format(x, y, grid[(x, y)]))
            if grid[(x, y)] > 361527:
                print(grid[x, y])
                break

        x += 1
        grid[(x, y)] = calculate_value(grid, x, y)
        print("({}, {}) = {}".format(x, y, grid[(x, y)]))
        if grid[(x, y)] > 361527:
            print(grid[x, y])
            break


def calculate_value(grid, x, y):
    num = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            coordinates = (x - i, y - j)
            if coordinates in grid.keys():
                num += grid[coordinates]
    return num

if __name__ == '__main__':
    build_graph()
