from functools import reduce


class VectorException(Exception):
    def __init__(self, msg):
        self._message = msg

    def __str__(self):
        return self._message


class Vector:
    def __init__(self, data):
        if not isinstance(data, list):
            raise Vector('Wrong data type')

        self._body = data[:]
        self._n = len(self._body)

    def __str__(self):
        return ' '.join(tuple(map(lambda x: str(x), self._body)))

    def __add__(self, other):
        return Vector(list(map(lambda i: other[i] + self._body[i], range(self._n))))

    def __iadd__(self, other):
        return Vector(list(map(lambda i: other[i] + self._body[i], range(self._n))))

    def __sub__(self, other):
        return Vector(list(map(lambda i: self._body[i] - other[i], range(self._n))))

    def __isub__(self, other):
        return Vector(list(map(lambda i: self._body[i] - other[i], range(self._n))))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return reduce(lambda a, i: a + self._body[i] * other[i], range(self._n), 0)
        else:
            return Vector(list(map(lambda x: x * other, self._body)))

    def __eq__(self, other):
        return reduce(lambda a, i: a and self._body[i] == other[i], range(self._n), True)

    def __len__(self):
        return self._n

    def __getitem__(self, item):
        return self._body[item]
