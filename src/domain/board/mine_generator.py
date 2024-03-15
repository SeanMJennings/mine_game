import random
from src.domain.board.mine import Mine
class MineGenerator:
    
    def __init__(self, random_generator: random, board_dimensions: tuple[int,int]):
        self.random_generator = random_generator
        self.board_dimensions = board_dimensions
    def generate_mines(self):
        mines = []
        for x in range(self.board_dimensions[0]):
            for y in range(self.board_dimensions[1]):
                if (self.random_generator.random() == 1.0):
                    mines.append(Mine((x,y)))
        return mines
                    