# n -- столбцы, m -- строки
from functools import reduce


class T:
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


class TableException(Exception):
    def __init__(self, msg=''):
        self._message = msg

    def __str__(self):
        return self._message


class Table:
    def __init__(self, data):
        if not isinstance(data, list):
            raise TableException('Wrong table data type')
        if not reduce(lambda a, x: a and isinstance(x, list), data, True):
            raise TableException('Wrong table data type')

        self._table = [[i for i in j] for j in data]
        self._width = len(self._table)
        print(self._width)
        self._height = len(self._table[0])
        print(self._height)

        if not reduce(lambda a, x: a and len(x) == self._height, data, True):
            raise TableException('Wrong table size')

    def __str__(self):
        return ''.join(list(map(lambda x: ' '.join(x) + '\n', list(zip(*self._table)))))

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def tail(self, n):
        return self._table[n:]

    def head(self, n):
        return self._table[:n]

    def add_columns(self, adding_table):
        self._table.extend(adding_table.get_adding_table(range(adding_table.get_width())))
        self._width += adding_table.get_width()

    def add_rows(self, adding_table):
        lines = tuple(zip(*adding_table.get_rows(range(self._height))))
        print(lines)
        for i in range(self._width):
            self._table[i].extend(lines[i])
        self._height += len(lines[0])

    def get_columns(self, indexes):
        return [[self._table[j][i] for i in range(self._height)] for j in indexes]

    def get_rows(self, indexes):
        return [[self._table[i][j] for i in range(self._width)] for j in indexes]

t1 = Table([['1', '2'], ['1', '3'], ['1', '2']])

t2 = Table([['13', '24'], ['11', '33'], ['22', '99']])

# t1.add_columns(t2)
t1.add_rows(t2)
print(t1)


# print(t1.get_rows([1]))
