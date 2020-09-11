from .constants import *
from .piece import *
import pygame

class Board():
    def __init__(self,screen):
        self.screen = screen
        self.board = [];
        for row in range(BOARD_SIZE):
            self.board.append([])
            for col in range(BOARD_SIZE):
                if (col%2 == (row+1)%2):
                    if(row < BLUE_ROWS):
                        self.board[row].append(Piece(row,col,BLUE))
                    elif (row > RED_ROWS):
                        self.board[row].append(Piece(row,col,RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self):
        self._draw_board()
        self._draw_pieces()

    def _draw_board(self):
        self.screen.fill(WHITE)
        for row in range(BOARD_SIZE):
            for col in range(row%2, BOARD_SIZE, 2):
                pygame.draw.rect(self.screen, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def _draw_pieces(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                piece = self.board[row][col]
                if (piece != 0):
                    pygame.draw.circle(self.screen, BORDER_COLOR, piece.get_cords(), RADIUS+OFFSET)
                    pygame.draw.circle(self.screen, piece.color, piece.get_cords(), RADIUS)