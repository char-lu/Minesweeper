import Board


class Sentence:
    def __init__(self, cell, mine_count):
        adjacents = board.get_adjacent_cells(cell)
        self.cells = [y for y in adjacents if y.appearance == '█']
        self.mine_count = mine_count

    def remove_from_sentence(self, cell):
        if cell in self.cells:
            self.cells.pop(cell)


class Knowledge:
    def __init__(self):
        self.knowledge = []

    def add_sentence(self, cell, mine_count):
        self.knowledge.append(Sentence(cell, mine_count))

    def remove_from_knowledge(self, sentence):
        if sentence in self.knowledge:
            del self.knowledge[sentence]











board = Board(5, 5, 5)
board.clear_cell(3, 3)
sentence = Sentence(board.grid[1][1], board.grid[1][1].cell_type)

for x in sentence.cells:
    x.appearance = "F"

board.show_board()

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