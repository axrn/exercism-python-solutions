class Matrix(object):
    def __init__(self, matrix_string: str) -> None:
        self._rows = [[int(x) for x in str_row.split()] for str_row in matrix_string.splitlines()]
        self._columns = [list(x) for x in zip(*self._rows)]

    def row(self, index: int) -> list:
        return self._rows[index][:]

    def column(self, index: int) -> list:
        return self._columns[index][:]
