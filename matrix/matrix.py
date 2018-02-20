class Matrix(object):
    def __init__(self, matrix_string: str) -> None:
        self._rows = [[int(x) for x in str_row.split()] for str_row in matrix_string.split('\n')]
        self._columns = [[x[i] for x in self._rows] for i in range(len(self._rows[0]))]

    def row(self, index: int) -> list:
        return self._rows[index]

    def column(self, index: int) -> list:
        return self._columns[index]
