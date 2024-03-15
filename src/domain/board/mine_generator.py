import random
from ..mine import Mine
class MineGenerator:
    
    def __init__(self, random_generator: random, board_dimensions: tuple[int,int]):
        self._random_generator = random_generator
        self._board_dimensions = board_dimensions
    def generate_mines(self):
        mines = []
        for x in range(self._board_dimensions[0]):
            for y in range(self._board_dimensions[1]):
                if (self._random_generator.random() == 1.0):
                    mines.append(Mine((x,y)))
        return mines
                    