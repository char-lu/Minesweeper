import random

class Cell:
    def __init__(self, cell_type, row, col, is_flagged=False, is_visible=False):
        self.is_flagged = is_flagged
        self.is_visible = is_visible
        self.appearance = '█'
        self.cell_type = cell_type
        self.row = row
        self.col = col

    def flag(self):
        if not self.is_visible:
            self.is_flagged = not self.is_flagged
            self.appearance = '▒'
            return True
        else:
            if self.appearance != self.cell_type:
                self.appearance = '█'
            return False
            pass

    def reveal(self):
        self.is_visible = True
        self.appearance = self.cell_type

    def is_adjacent(self, other_cell):
        return abs(other_cell.row - self.row) <= 1 and abs(other_cell.col - self.col) <= 1


class Board():
    def __init__(self, height, width, numMines, game_state=3, numFlags=0):
        self.grid = [[Cell(0, row, col) for col in range(width)] for row in range(height)]
        self.height = height
        self.width = width
        self.numMines = numMines
        self.numFlags = numFlags
        # game state
        # 0 = lost
        # 1 = won
        # 2 = In process
        # 3 = Starting
        self.game_state = game_state

    def set_board(self, first_clear):
        count = 0
        while count < self.numMines:
            # self.reveal_board()
            # print()
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            random_cell = self.grid[y][x]
            if random_cell.cell_type == 'X' or random_cell.is_adjacent(first_clear):
                pass
            else:
                random_cell.cell_type = 'X'
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

    def increment_adjacents(self, mine):
        adjacents = self.get_adjacent_cells(mine)

        for x in adjacents:
            if str(x.cell_type) == 'X':
                pass
            else:
                x.cell_type += 1

    def show_board(self):
        for x in self.grid:
            for y in x:
                print(y.appearance, end=' ')
            print()
        print()

    def clear_cell(self, row, col):
        target = self.grid[row - 1][col - 1]

        if self.game_state == 3:
            self.set_board(target)

        if target.cell_type == 'X':
            self.lose()
        else:
            self.flood_fill(row, col)
        self.check_win()

    def flood_fill(self, row, col, visited=None):
        if visited is None:
            visited = set()
        target = self.grid[row - 1][col - 1]
        if target.cell_type == 'X':
            pass
        else:
            target.reveal()

        visited.add((row - 1, col - 1))
        for adjacent in self.get_adjacent_cells(target):
            if (adjacent.row, adjacent.col) not in visited:
                if adjacent.cell_type == 0:
                    self.flood_fill(adjacent.row + 1, adjacent.col + 1, visited)
                if adjacent.cell_type != 'X':
                    adjacent.reveal()
                    visited.add((adjacent.row, adjacent.col))
            else:
                pass

    def flag_cell(self, row, col):
        if self.grid[row - 1][col - 1].flag():
            self.numFlags += 1
        self.check_win();

    def check_win(self):
        if self.numFlags != self.numMines:
            return
        for x in self.grid:
            for y in x:
                if y.cell_type == 'X' and y.appearance == '▒' or y.cell_type == y.appearance:
                    pass
                else:
                    return
        self.game_state = 1
        self.show_board()
        print('You win!')

    def reveal_board(self):
        for x in self.grid:
            for y in x:
                print(y.cell_type, end=' ')
            print()

    def lose(self):
        self.game_state = 0
        print('You lost!')
        self.reveal_board()

