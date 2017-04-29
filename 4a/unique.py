import sys


def unique(data):
    prev = str()
    for i in data:
        if i != prev:
            yield i
        prev = i

exec(sys.stdin.read())
