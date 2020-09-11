import pygame
from checkers.constants import *
from checkers.board import *

FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Checkers')
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    board = Board(screen)

    while run:
        clock.tick(FPS)
        board.draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
