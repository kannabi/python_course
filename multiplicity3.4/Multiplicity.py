class Multiplicity:
    def __init__(self, initial=None):
        if initial is None:
            initial = []

        self.space_units = []
        self.space = []
        self.n = 1

        self.space_units.extend(initial)

    def next(self):
        buf = []
        self.n += 1
        for i in range(self.n * len(self.space_units))
            print("yo")
