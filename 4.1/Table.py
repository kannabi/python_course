class Table:
    def __init__(self, table):
        if not isinstance(table, list):
            raise TableException("Wrong table init format.")
        else:
            for i in table:
                if not isinstance(i, list):
                    raise TableException("Wrong table init format.")

        self._table = table[:]
        self._width = len(self._table)
        self._height = len(self._table[0])

        for it in self._table:
            if len(it) > self._height:
                raise TableException("Init columns have different length.")

    def __str__(self):
        return ''.join(list(map(lambda x: ' '.join(x) + '\n', list(zip(*self._table)))))

    def add_columns(self, columns):
        self._table.extend(columns)
        self._width += len(columns)

    def add_lines(self, lines):
        for i in range(self._width):
            self._table[i].extend(lines[i])
        self._height += 1

    def get_columns(self, start, end):
        return [[self._table[i][j] for i in range(self._height)] for j in range(start, end)]

    def get(self, index):
        return self._table[index]

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def tail(self, n):
        return self._table[n:]

    def head(self, n):
        return self._table[:n]


class TableException(Exception):
    def __init__(self, message=""):
        self._msg = message

    def __str__(self):
        return str(self._msg)
