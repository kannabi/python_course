import argparse
from TrExceptions import ChangeException


class ChangeException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


def change_line(data, translate_rule, delete_rule=None):
    if not isinstance(data, str):
        raise ChangeException("Wrong type of changing item. It should be string.")
    data = tuple(data)

    if delete_rule:
        data = tuple(filter(lambda x: x not in delete_rule, data))

    data = tuple(map(lambda x: translate_rule.get(x, x), data))

    return ''.join(data)


def init_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("file", action="store", nargs=1, type=str)
    parser.add_argument("table1", action="store", nargs=1, type=str)
    parser.add_argument("table2", action="store", nargs=1, type=str)
    parser.add_argument("-d", "--delete", action="store", type=str)

    return parser


def check_params(params):
    if len(res.table1[0]) != len(res.table2[0]):
        raise ChangeException("Wrong translate tables size")

    if True in tuple(map(lambda x: True if list(params.table1[0]).count(x) > 1 else False, params.table1[0])):
        raise ChangeException("Duplicated values in translate table")


res = init_parser().parse_args()

try:
    check_params(res)
except ChangeException as e:
    print(e)
    exit()

translate_dict = dict(zip(list(res.table1[0]), list(res.table2[0])))

delete_chars = None
if res.delete:
    delete_chars = res.delete

fin = open(res.file[0])
fout = open("res.txt", "w")

for line in fin:
    fout.write(change_line(line, translate_dict, delete_chars))

fin.close()
fout.close()
