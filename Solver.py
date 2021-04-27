import GameBoard
import pygame
import time
from pygame.locals import *

class Sentence:
    def __init__(self, cell, mine_count):
        adjacents = board.get_adjacent_cells(cell)
        self.target_cell = cell
        self.cells = [y for y in adjacents if y.is_visible is False]
        self.mine_count = mine_count
        #self.num_flags = num_flags

    def remove_from_sentence(self, cell):
        if cell in self.cells:
            self.cells.pop(cell)

    def print_sentence(self):
        print(str(len(self.cells)) + ", ", sep=' ', end='', flush=True)
        for x in self.cells:
            print("(" + str(x.row) + ", " + str(x.col) + ")", sep=' ', end='', flush=True)
        print(" = " + str(self.mine_count))

class Knowledge:
    def __init__(self, board):
        self.knowledge = []
        self.board = board

    def read_board(self):
        self.knowledge = []
        for x in self.board.grid:
            for y in x:
                if y.is_visible and y.cell_type != 0:
                    self.add_sentence(y, y.cell_type)


    def add_knowledge(self, cells):
        for cell in cells:
            self.add_sentence(cell, cell.cell_type)

    def add_sentence(self, cell, mine_count):
        self.knowledge.append(Sentence(cell, mine_count))


    def refine_knowledge(self):
        change = False
        self.read_board()
        flagged_sentences = [sentence for sentence in self.knowledge if len(sentence.cells) == sentence.mine_count]
        for sentence in flagged_sentences:
            for cell in sentence.cells:
                if not cell.is_flagged:
                    time.sleep(0.03)
                    self.board.flag_cell(cell.row, cell.col)
                    change = True

            pygame.display.update()

        for sentence in [sentence for sentence in self.knowledge if sentence not in flagged_sentences]:
            for adj_cell in [adj_cell for adj_cell in self.board.get_adjacent_cells(sentence.target_cell) if adj_cell.is_flagged]:
                sentence.cells.remove(adj_cell)
                sentence.mine_count -= 1
            if sentence.mine_count == 0:
                for adj_cell in [adj_cell for adj_cell in self.board.get_adjacent_cells(sentence.target_cell) if not adj_cell.is_visible and not adj_cell.is_flagged]:
                    time.sleep(0.03)
                    board.clear_cell(adj_cell.row, adj_cell.col)
                    pygame.display.update()
                self.knowledge.remove(sentence)

        if change is True:
            self.refine_knowledge()

    def print_knowledge(self):
        for x in self.knowledge:
            x.print_sentence()




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
            board_knowledge = Knowledge(board)
            board_knowledge.refine_knowledge()
        if board.game_state == 1 or board.game_state == 0:
            running = False

    pygame.display.flip()

pygame.quit()

"""
pygame.init()
screen = pygame.display.set_mode([21*30,21*16])

board = GameBoard.Board(16, 30, 80, screen)
board.clear_cell(7,15)
board_knowledge = Knowledge(board)
pygame.display.update() #####################
# board_knowledge.print_knowledge()
board_knowledge.refine_knowledge()
running = True
print("###########")
board_knowledge.print_knowledge()

while running:
    # Did the user click the window close button?

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
"""
"""
print('Enter height: ', end='')
height = int(input())
print('Enter width: ', end='')
width = int(input())
print('Enter number of mines: ', end='')
mineNumber = int(input())

board = Board(height, width, mineNumber)


def action(input):
    split_input = input.split()
    choice = split_input[0].upper()
    try:
        if int(split_input[1]) <= 0 or int(split_input[2]) <= 0:
            print("as")
            raise IndexError
        elif choice == 'FLAG':
            board.flag_cell(int(split_input[1]), int(split_input[2]))
        elif choice == 'CLEAR':
            board.reveal_cell(int(split_input[1]), int(split_input[2]))
        else:
            raise TypeError
    except IndexError or TypeError:
        print('Invalid action')


while board.game_state != 0 and board.game_state != 1:
    board.show_board()
    print('What is your action? :', end='')
    action(input())
"""