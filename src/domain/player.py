from .board.board import Direction

class Player:
    
    def __init__(self, position: tuple[int, int]):
        self._x = position[0]
        self._y = position[1]
        self._mines_detonated = 0

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
        
    @property
    def mines_detonated(self):
        return self._mines_detonated
    
    def ___mines_detonated(self, value : int):
        self._mines_detonated += value
    
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
    
    def mine_hit(self):
        self.___mines_detonated(1)