class Multiplicity:
    def __init__(self, initial=None):
        if initial is None:
            initial = []

        self.space_units = {}
        self.space = []
        self.n = 1

        for i in range(len(initial)):
            self.space_units.update({i: initial[i]})
        print(self.space_units)

    def next(self):
        buf = []
        self.n += 1

        for i in range(len(self.space_units) ** self.n):
            blank = i
            while blank > 0:
                buf.append(self.space_units.get(blank % len(self.space_units)))
                blank //= len(self.space_units)

            while len(buf) < self.n:
                buf.append(self.space_units.get(0))

            buf.reverse()
            print(buf)
            buf.clear()

    def get_space(self):
        return self.space


test_mult = Multiplicity(['_', 'A'])
for i in range(5):
    test_mult.next()
    print("================================================================================")
# print(test_mult.get_space())
