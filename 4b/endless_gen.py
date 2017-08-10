import sys


def inexhaustible(generator):
    def wrapper():
        return generator()
    return wrapper

@inexhaustible
def some_generator():
    yield 1
    yield 2

x = some_generator()
print(list(x))
print(list(x))
