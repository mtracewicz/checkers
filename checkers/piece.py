from .constants import *

class Piece():
    def __init__(self,row,column,color):
        self.row = row
        self.column = column
        self.color = color
        self.king = False

    def __repr__(self):
        return f'[{self.row},{self.column}] - {self.color}'

    def get_cords(self):
        return (SQUARE_SIZE * self.column + SQUARE_SIZE //2, SQUARE_SIZE * self.row + SQUARE_SIZE //2,)

    def make_king(self):
        self.king = True
