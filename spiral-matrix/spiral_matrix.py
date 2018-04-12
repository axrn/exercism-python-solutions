from itertools import cycle


def spiral(size: int) -> list:
    n = size

    direction = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    res = [[None for x in range(n)] for x in range(n)]

    x, y = 0, 0
    d = next(direction)

    for i in range(1, n ** 2 + 1):
        try:
            if res[x][y] is None:
                res[x][y] = i
                x, y = x + d[0], y + d[1]
            else:
                x, y = x - d[0], y - d[1]
                d = next(direction)
                x, y = x + d[0], y + d[1]

                res[x][y] = i
                x, y = x + d[0], y + d[1]
        except IndexError:
            x, y = x - d[0], y - d[1]
            d = next(direction)
            x, y = x + d[0], y + d[1]

            res[x][y] = i
            x, y = x + d[0], y + d[1]

    return res
