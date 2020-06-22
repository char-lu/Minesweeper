import Board
import pygame

pygame.init()
screen = pygame.display.set_mode([800,600])



running = True

while running:
    # Did the user click the window close button?

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    # Flip the display
    pygame.display.flip()
# Done! Time to quit.

pygame.quit()

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
            board.clear_cell(int(split_input[1]), int(split_input[2]))
        else:
            raise TypeError
    except IndexError or TypeError:
        print('Invalid action')


while board.game_state != 0 and board.game_state != 1:
    board.show_board()
    print('What is your action? :', end='')
    action(input())
