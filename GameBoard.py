import random
import pygame

unexplored = pygame.image.load("resources/unexplored.png")
tile_0 = pygame.image.load("resources/tile_0.png")
tile_1 = pygame.image.load("resources/tile_1.png")
tile_2 = pygame.image.load("resources/tile_2.png")
tile_3 = pygame.image.load("resources/tile_3.png")
tile_4 = pygame.image.load("resources/tile_4.png")
tile_5 = pygame.image.load("resources/tile_5.png")
tile_6 = pygame.image.load("resources/tile_6.png")
tile_7 = pygame.image.load("resources/tile_7.png")
tile_8 = pygame.image.load("resources/tile_8.png")
mine = pygame.image.load("resources/mine.png")
mine_hit = pygame.image.load("resources/mine_hit.png")
flag = pygame.image.load("resources/flag.png")

tiles = [tile_0, tile_1, tile_2, tile_3, tile_4, tile_5, tile_6, tile_7, tile_8, mine]

class Cell:
    def __init__(self, row, col, game_screen, cell_type=0, is_flagged=False, is_visible=False):

        super(Cell, self).__init__()
        self.is_flagged = is_flagged
        self.is_visible = is_visible
        self.game_screen = game_screen
        self.cell_type = cell_type
        self.row = row
        self.col = col
        self.game_screen.blit(unexplored, (self.col * 21, self.row * 21))

    def flag(self):
        if self.is_visible:
            return
        else:
            if self.is_flagged:
                self.game_screen.blit(unexplored, (self.col * 21, self.row * 21))
            else:
                self.game_screen.blit(flag, (self.col * 21, self.row * 21))
        self.is_flagged = not self.is_flagged

    def reveal(self):
        self.is_visible = True
        image = tiles[self.cell_type]
        self.game_screen.blit(image, (self.col * 21, self.row * 21))

    def is_adjacent(self, other_cell):
        return abs(other_cell.row - self.row) <= 1 and abs(other_cell.col - self.col) <= 1


class Board:
    def __init__(self, height, width, num_mines, game_screen, game_state=3, ):
        self.grid = [[Cell(row, col, game_screen) for col in range(width)] for row in range(height)]
        self.height = height
        self.width = width
        self.num_mines = num_mines
        # game state
        # 0 = lost
        # 1 = won
        # 2 = In process
        # 3 = Starting
        self.game_state = game_state
        self.game_screen = game_screen

    def set_board(self, first_clear):
        count = 0
        while count < self.num_mines:
            # self.reveal_board()
            # print()
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            random_cell = self.grid[y][x]
            if random_cell.cell_type == 9 or random_cell.is_adjacent(first_clear):
                pass
            else:
                random_cell.cell_type = 9
                self.increment_adjacents(random_cell)
                count += 1

        self.game_state = 2

    def get_adjacent_cells(self, cell):
        adjacency = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]
        x = cell.col
        y = cell.row
        for dx, dy in adjacency:
            if 0 <= (x + dx) < self.width and 0 <= y + dy < self.height:  # boundaries check
                yield self.grid[y + dy][x + dx]

    def increment_adjacents(self, mine_cell):
        adjacents = self.get_adjacent_cells(mine_cell)

        for x in adjacents:
            if x.cell_type == 9:
                pass
            else:
                x.cell_type += 1

    def clear_cell(self, row, col):
        revealed_cells = set()

        target = self.grid[row][col]
        if self.game_state == 3:
            self.set_board(target)

        if target.cell_type == 9:
            self.lose()
        elif target.is_flagged:
            return
        elif target.cell_type != 0:
            target.reveal()
            revealed_cells.add(target)
        else:
            revealed_cells = self.flood_fill(row, col)
        self.check_win()
        return revealed_cells

    def flood_fill(self, row, col, visited=None):
        if visited is None:
            visited = set()
        target = self.grid[row][col]
        if target.cell_type == 9:
            return visited
        else:
            target.reveal()

        visited.add(target)
        for adjacent in self.get_adjacent_cells(target):
            if adjacent not in visited:
                if adjacent.cell_type == 0:
                    visited = self.flood_fill(adjacent.row, adjacent.col, visited)
                if adjacent.cell_type != 9:
                    adjacent.reveal()
                    visited.add(adjacent)
            else:
                pass
        return visited

    def flag_cell(self, row, col):
        target = self.grid[row][col]
        target.flag()

    def check_win(self):
        for x in self.grid:
            for y in x:
                if y.cell_type != 9 and not y.is_visible:
                    return
        self.game_state = 1
        print('You win!')

    def lose(self):
        self.game_state = 0
        self.reveal_board()
        print('You lost!')

    def reveal_board(self):
        for x in self.grid:
            for y in x:
                if y.cell_type ==9:
                    y.reveal()

"""
    def reveal_board(self):
        for x in self.grid:
            for y in x:
                print(y.cell_type, end=' ')
            print()
"""