NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self._bearing = bearing
        self._x, self._y = x, y

    @property
    def bearing(self) -> int:
        return self._bearing

    @property
    def coordinates(self) -> tuple:
        return self._x, self._y

    def turn_right(self) -> None:
        self._bearing = (self._bearing + 1) % 4

    def turn_left(self) -> None:
        self._bearing = (self._bearing - 1) % 4

    def advance(self) -> None:
        adv_map = {NORTH: (0, 1), EAST: (1, 0), SOUTH: (0, -1), WEST: (-1, 0)}
        self._x += adv_map[self._bearing][0]
        self._y += adv_map[self._bearing][1]

    def simulate(self, commands: str) -> None:
        cmd_map = {'R': self.turn_right, 'L': self.turn_left, 'A': self.advance}
        for command in list(commands):
            cmd_map[command]()
