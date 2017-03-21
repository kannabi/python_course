class Alive:
    def __init__(self, world):
        self.world = world


class Nuclear (Alive):
    def __init__(self, world):
        super().__init__(world)


class NonNuclear (Alive):
    def __init__(self, world):
        super().__init__(world)


class Virus (Nuclear):
    def __init__(self, world):
        super().__init__(world)


class Bacteria (Nuclear):
    def __init__(self, world):
        super().__init__(world)


class Mashrooms (Nuclear):
    def __init__(self, world):
        super().__init__(world)


class Plants (Nuclear):
    def __init__(self, world):
        super().__init__(world)


class Animals (Nuclear):
    def __init__(self, world):
        super().__init__(world)


class Chordate (Animals):
    def __init__(self, world):
        super().__init__(world)


class Vertebrate (Chordate):
    def __init__(self, world):
        super().__init__(world)


class Mammal(Vertebrate):
    def __init__(self, world):
        super().__init__(world)


class Human (Mammal):
    def __init__(self, world):
        super().__init__(world)
