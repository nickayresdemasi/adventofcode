from utils import parse_fname, read_input


def parse_input(input_str):
    return [row for row in input_str.split('\n') if row != '']


class TobogganRun(object):
    def __init__(self, grid):
        """Initializes TobogganRun object with a grid

        Args:
            - grid (list(str)): grid of trees (#) and open squares (.)

        Returns a TobogganRun object
        """
        self.grid = grid

    def trees_hit(self, start_pos, slope):
        """Calculates the # of trees hit when sledding down a grid

        Args:
            - start_pos (tuple(int, int)): x, y coords of starting position on grid
            - slope (tuple(int, int)): movement in terms of x and y

        Returns number of trees hit as int
        """
        trees_hit = 0
        x, y = start_pos
        for i in range(y, len(self.grid), slope[1]):
            row = self.grid[i]
            trees_hit += row[x] == '#'
            x = (x + slope[0]) % len(row)
        return trees_hit


def main():
    input_str = read_input(*parse_fname(__file__))
    grid = parse_input(input_str)
    toboggan_run = TobogganRun(grid)

    start_pos = (0, 0)
    slope = (3, 1)
    trees_hit = toboggan_run.trees_hit(start_pos, slope)
    print("PART 1")
    print("Trees hit: %i" % trees_hit)
    print()

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_hit = 1
    for slope in slopes:
        trees_hit *= toboggan_run.trees_hit(start_pos, slope)
    print("PART 2")
    print("Product of trees hit: %i" % trees_hit)


if __name__ == '__main__':
    main()
