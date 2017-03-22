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
        self._table.append(lines)
        self._n += 1

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


table = Table(6, 6)
# table.print()
# print(table.get(2, 4))
table.add_columns([[str(j) for _ in range(3)] for j in range(table.get_height())])
table.print()
# table.add_lines([str(table.get_height()) for i in range(table.get_height())])
# table.print()

print("----------------------------------------")

