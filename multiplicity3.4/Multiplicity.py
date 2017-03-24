class Multiplicity:
    def __init__(self, initial=None):
        if initial is None:
            initial = []

        self.space = []
        self.counter = 0

        self.space_units = tuple(initial)
        self.space.append(self.space_units[0])

    def next(self):
        self.counter += 1
        blank = self.counter
        self.space.clear()

        while blank > 0:
            self.space.insert(0, self.space_units[blank % len(self.space_units)])
            blank //= len(self.space_units)

    def get_space(self):
        return self.space
