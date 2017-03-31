class Table:
    """
    Attributes
    ------------------
    n : integer
        Number of columns
    m : integer
        Number of lines
        
    Methods
    ------------------
    print()
    add_lines(lines)
    add_columns(columns)
    get(start, end)
    get_width()
    get_height()
    tail(n)
    head(n)
    """
    def __init__(self, n, m):
        self._table = [[str(j) for _ in range(m)] for j in range(n)]
        self._n = n
        self._m = m

    def print(self):
        """
        Print table's values
        """
        for i in range(self._n):
            print(' '.join(self._table[i]))

    def add_lines(self, lines):
        """
        Add lines to table
        """
        self._table.extend(lines)
        self._n += len(lines)

    def add_columns(self, columns):
        """
        Add columns to table
        """
        for i in range(self._n):
            self._table[i].extend(columns[i])
        self._m += 1

    def get(self, start, end):
        """
        Return columns from start to end position
        """
        return [[self._table[i][j] for i in range(self._m)] for j in range(start, end)]

    def get_width(self):
        """
        Return width of table
        """
        return self._n

    def get_height(self):
        """
        Return height of table
        """
        return self._m

    def tail(self, n):
        """
        Return n last columns of table
        """
        return self._table[n:]

    def head(self, n):
        """
        Return n first columns of table
        """
        return self._table[:n]
