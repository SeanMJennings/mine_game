from .board import Direction

class Player:
    def __init__(self, x : int, y : int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
      
    def __x(self, value : int):
        self._x = value

    @property
    def y(self):
        return self._y
      
    def __y(self, value : int):
        self._y = value
    
    def move(self, direction: Direction):
        match direction:
            case Direction.up:
                self.__y(self.y + 1)      
            case Direction.down:
                self.__y(self.y - 1)         
            case Direction.left:
                self.__x(self.x - 1)       
            case Direction.right:
                self.__x(self.x + 1)  