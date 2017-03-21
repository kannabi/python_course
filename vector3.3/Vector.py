class Vector:
    body = []

    def __init__(self, n, initial=None):
        if initial is None:
            initial = []
        self.length = n
        if len(initial) == n:
            self.body.extend(initial)
        else:
            for i in self.length:
                self.body.append(0)

    def sum(self, term):
        for i in self.length:
            self.body[i] += term[i]
        return self.body

    def subtraction(self, subtrahend):
        for i in self.length:
            self.body[i] -= subtrahend[i]
        return self.body

    def const_multiplication(self, factor):
        for i in self.length:
            self.body[i] *= factor[i]
        return self.body

    def equals(self, compared):
        for i in self.length:
            if self.body[i] != compared[i]:
                return True
        return False

    def scalar_product(self, factor):
        res = 0
        for i in self.length:
            res += self.body[i] * factor[i]
        return res

    def size(self):
        return self.length

    def get(self, i):
        return self.body[i]

    def to_string(self):
        return ' '.join(self.body)
