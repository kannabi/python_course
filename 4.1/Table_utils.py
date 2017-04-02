import argparse


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


def print_data(data):
    print(''.join(list(map(lambda x: ' '.join(x) + '\n', data))))


def get_table_from_file(file_name):
    with open(file_name) as fin:
        data = fin.read()
    data = data.split('\n')
    data = list(map(lambda x: x.split(';'), data))
    try:
        return [[data[i][j] for i in range(len(data[j]))] for j in range(len(data))]
    except IndexError:
        print("Wrong table format!")


def paste(first_file, second_file):
    try:
        work_table = Table(get_table_from_file(first_file))
        work_table.add_columns(get_table_from_file(second_file))
        print(work_table)
    except TableException as e:
        print(e)


def cut(file_name, indexes_list):
    try:
        work_table = Table(get_table_from_file(file_name))
        columns = list(map(lambda x: work_table.get(int(x)), indexes_list))
        print_data(list(zip(*columns)))
    except TableException as e:
        print(e)
    except ValueError:
        print("Wrong column index")
    except IndexError:
        print("Column index out of range")


def head(file_name, n):
    try:
        work_table = Table(get_table_from_file(file_name))
        print_data(list(zip(*work_table.head(n))))
    except TableException as e:
        print(e)
    except IndexError:
        print("Column index out of range")


def tail(file_name, n):
    try:
        work_table = Table(get_table_from_file(file_name))
        print_data(list(zip(*work_table.tail(n))))
    except TableException as e:
        print(e)
    except IndexError:
        print("Column index out of range")


def init_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser_name")

    paste_parser = subparsers.add_parser("paste")
    paste_parser.add_argument("first_file", action="store", nargs=1, type=str)
    paste_parser.add_argument("second_file", action="store", nargs=1, type=str)

    cut_parser = subparsers.add_parser("cut")
    cut_parser.add_argument("file", action="store", nargs=1, type=str)
    cut_parser.add_argument("-f", action="store", nargs=1, type=str, required=True)

    head_parser = subparsers.add_parser("head")
    head_parser.add_argument("file", action="store", nargs=1, type=str)
    head_parser.add_argument("-n", action="store", nargs=1, type=int, required=True)

    tail_parser= subparsers.add_parser("tail")
    tail_parser.add_argument("file", action="store", nargs=1, type=str)
    tail_parser.add_argument("-n", action="store", nargs=1, type=int, required=True)

    return parser


res = init_parser().parse_args()

if res.subparser_name == "cut":
    cut(res.file[0], res.f[0].split(','))
elif res.subparser_name == "paste":
    paste(res.first_file[0], res.second_file[0])
elif res.subparser_name == "head":
    head(res.file[0], res.n[0])
elif res.subparser_name == "tail":
    tail(res.file[0], res.n[0])
