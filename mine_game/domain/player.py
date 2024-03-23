from mine_game.domain.board.direction import Direction


class Player:

    def __init__(self, position: tuple[int, int]):
        self.__x = position[0]
        self.__y = position[1]
        self.__mines_detonated = 0

    @property
    def x(self):
        return self.__x

    def __set_x(self, value: int):
        self.__x = value

    @property
    def y(self):
        return self.__y

    def __set_y(self, value: int):
        self.__y = value

    @property
    def mines_detonated(self):
        return self.__mines_detonated

    def __set_mines_detonated(self, value: int):
        self.__mines_detonated += value

    def move(self, direction: Direction):
        match direction:
            case Direction.up:
                self.__set_y(self.y + 1)
            case Direction.down:
                self.__set_y(self.y - 1)
            case Direction.left:
                self.__set_x(self.x - 1)
            case Direction.right:
                self.__set_x(self.x + 1)

    def mine_hit(self):
        self.__set_mines_detonated(1)
