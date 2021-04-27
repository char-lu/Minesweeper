import GameBoard
import pygame
from pygame.locals import *

print('Enter height: ', end='')
height = int(input())
print('Enter width: ', end='')
width = int(input())
print('Enter number of mines: ', end='')
mineNumber = int(input())

pygame.init()
screen = pygame.display.set_mode([21*width,21*height])

board = GameBoard.Board(height, width, mineNumber, screen)

running = True

while running:
    # Did the user click the window close button?

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN and event.button == BUTTON_LEFT:
            mouse_x, mouse_y = event.pos  # Now it will have the coordinates of click point.
            board.clear_cell(int(mouse_y/21),int(mouse_x/21))
        if event.type == MOUSEBUTTONDOWN and event.button == BUTTON_RIGHT:
            mouse_x, mouse_y = event.pos  # Now it will have the coordinates of click point.
            board.flag_cell(int(mouse_y/21),int(mouse_x/21))


    pygame.display.flip()

pygame.quit()
