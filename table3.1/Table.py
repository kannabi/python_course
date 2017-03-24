# n -- столбцы, m -- строки


class Table:
    def __init__(self, n, m):
        self._table = [[str(j) for _ in range(m)] for j in range(n)]
        self._n = n
        self._m = m

    def print(self):
        for i in range(self._n):
            print(' '.join(self._table[i]))

    def add_lines(self, lines):
        self._table.extend(lines)
        self._n += len(lines)

    def add_columns(self, columns):
        for i in range(self._n):
            self._table[i].extend(columns[i])
        self._m += 1

    def get(self, start, end):
        return [[self._table[i][j] for i in range(self._m)] for j in range(start, end)]

    def get_width(self):
        return self._n

    def get_height(self):
        return self._m

    def tail(self, n):
        return self._table[n:]

    def head(self, n):
        return self._table[:n]
