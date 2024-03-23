class Mine:

    def __init__(self, position: tuple[int, int]):
        self.__position = position
        self.__detonated = False

    @property
    def position(self):
        return self.__position

    @property
    def detonated(self):
        return self.__detonated

    def detonate(self):
        self.__detonated = True
