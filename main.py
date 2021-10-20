import random
winner = False

def display_board(board):
    for x in board:
        for y in x:
            print('{0:<1}'.format(y), end="")
        print()

def freeSpaces(board):
    global winner
    if ((board[2][4] == 'x' or board[2][4] == 'o') and (board[2][12] == 'x' or board[2][12] == 'o') and (board[2][20] == 'x' or board[2][20] == 'o') and (board[6][4] == 'x' or board[6][4] == 'o') and
            (board[6][12] == 'x' or board[6][12] == 'o') and (board[6][20] == 'x' or board[6][20] == 'o') and (board[10][4] == 'x' or board[10][4] == 'o') and (board[10][12] == 'x' or board[10][12] == 'o') and (board[10][20] == 'x' or board[10][20] == 'o')):
        print("It's a tie!")
        winner = True

def enter_move(board):
    valid = False
    while not valid:
        move = int(input("Enter your move: "))
        if move == 1:
            if board[2][4] == 'o' or board[2][4] == 'x':
                print("Invalid! Try again.")
                continue
            else:
                board[2][4] = "o"
                display_board(board)
                valid = True
                break
        elif move == 2:
            if board[2][12] == 'o' or board[2][12] == 'x':
                print("Invalid! Try again.")
                continue
            else:
                board[2][12] = "o"
                display_board(board)
                valid = True
                break
        elif move == 3:
            if board[2][20] == 'o' or board[2][20] == 'x':
                print("Invalid! Try again.")
                continue
            else:
                board[2][20] = "o"
                display_board(board)
                valid = True
                break
        elif move == 4:
            if board[6][4] == 'o' or board[6][4] == 'x':
                print("Invalid! Try again.")
                continue
            else:
                board[6][4] = "o"
                display_board(board)
                valid = True
                break
        elif move == 6:
            if board[6][20] == 'o' or board[6][20] == 'x':
                print("Invalid! Try again.")
                continue
            else:
                board[6][20] = "o"
                display_board(board)
                valid = True
                break
        elif move == 7:
            if board[10][4] == 'o' or board[10][4] == 'x':
                print("Invalid! Try again.")
                continue
            else:
                board[10][4] = "o"
                display_board(board)
                valid = True
                break
        elif move == 8:
            if board[10][12] == 'o' or board[10][12] == 'x':
                print("Invalid! Try again.")
                continue
            else:
                board[10][12] = "o"
                display_board(board)
                valid = True
                break
        elif move == 9:
            if board[10][20] == 'o' or board[10][20] == 'x':
                print("Invalid! Try again.")
                continue
            else:
                board[10][20] = "o"
                display_board(board)
                valid = True
                break
        elif move == 5:
            print("Invalid! Try again.")
            continue

def victory_for(board, sign):
    global winner

    if sign == 'o':
        if board[2][4] == board[2][12] == board[2][20]:
            print("You Won!")
            winner = True
        elif board[10][4] == board[10][12] == board[10][20]:
            print("You Won!")
            winner = True
        elif board[2][4] == board[6][4] == board[10][4]:
            print("You Won!")
            winner = True
        elif board[2][20] == board[6][20] == board[10][20]:
            print("You Won!")
            winner = True
        elif freeSpaces(board):
            print("Its a tie!")
            winner = True
    else:
        if board[2][4] == board[2][12] == board[2][20]:
            print("You Lost!")
            winner = True
        elif board[6][4] == board[6][12] == board[6][20]:
            print("You Lost!")
            winner = True
        elif board[10][4] == board[10][12] == board[10][20]:
            print("You Lost!")
            winner = True
        elif board[2][4] == board[6][4] == board[10][4]:
            print("You Lost!")
            winner = True
        elif board[2][12] == board[6][12] == board[10][12]:
            print("You Lost!")
            winner = True
        elif board[2][20] == board[6][20] == board[10][20]:
            print("You Lost!")
            winner = True
        elif board[2][4] == board[6][12] == board[10][20]:
            print("You Lost!")
            winner = True
        elif board[2][20] == board[6][12] == board[10][4]:
            print("You Lost!")
            winner = True
        elif freeSpaces(board):
            print("Its a tie!")
            winner = True

def draw_move(board):
    valid = False
    while not valid:
        move = random.randint(1, 9)
        if move == 1:
            if board[2][4] == 'o' or board[2][4] == 'x':
                continue
            else:
                board[2][4] = "x"
                display_board(board)
                valid = True
                break
        elif move == 2:
            if board[2][12] == 'o' or board[2][12] == 'x':
                continue
            else:
                board[2][12] = "x"
                display_board(board)
                valid = True
                break
        elif move == 3:
            if board[2][20] == 'o' or board[2][20] == 'x':
                continue
            else:
                board[2][20] = "x"
                display_board(board)
                valid = True
                break
        elif move == 4:
            if board[6][4] == 'o' or board[6][4] == 'x':
                continue
            else:
                board[6][4] = "x"
                display_board(board)
                valid = True
                break
        elif move == 6:
            if board[6][20] == 'o' or board[6][20] == 'x':
                continue
            else:
                board[6][20] = "x"
                display_board(board)
                valid = True
                break
        elif move == 7:
            if board[10][4] == 'o' or board[10][4] == 'x':
                continue
            else:
                board[10][4] = "x"
                display_board(board)
                valid = True
                break
        elif move == 8:
            if board[10][12] == 'o' or board[10][12] == 'x':
                continue
            else:
                board[10][12] = "x"
                display_board(board)
                valid = True
                break
        elif move == 9:
            if board[10][20] == 'o' or board[10][20] == 'x':
                continue
            else:
                board[10][20] = "x"
                display_board(board)
                valid = True
                break
        elif move == 5:
            continue

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('Professor! here is programming assignment 4.')
    board = [
        ['+', '-', '-', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-','-', '-', '+'],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
        ['|', '', '', '', '1', '', '', '', '|', '', '', '', '2', '', '', '', '|', '', '', '', '3', '', '', '', '|'],
        ['|', '', '', '', '', '', '', '', '|', '', '', '', '', '', '', '', '|', '', '', '', '', '', '', '', '|'],
        ['+', '-', '-', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-','-', '-', '+'],
        ['|', '', '', '', '', '', '', '', '|', '', '', '', '', '', '', '', '|', '', '', '', '', '', '', '', '|'],
        ['|', '', '', '', '4', '', '', '', '|', '', '', '', 'x', '', '', '', '|', '', '', '', '6', '', '', '', '|'],
        ['|', '', '', '', '', '', '', '', '|', '', '', '', '', '', '', '', '|', '', '', '', '', '', '', '', '|'],
        ['+', '-', '-', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-','-', '-', '+'],
        ['|', '', '', '', '', '', '', '', '|', '', '', '', '', '', '', '', '|', '', '', '', '', '', '', '', '|'],
        ['|', '', '', '', '7', '', '', '', '|', '', '', '', '8', '', '', '', '|', '', '', '', '9', '', '', '', '|'],
        ['|', '', '', '', '', '', '', '', '|', '', '', '', '', '', '', '', '|', '', '', '', '', '', '', '', '|'],
        ['+', '-', '-', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '-','-', '-', '+']]

    display_board(board)
    while not winner:
        enter_move(board)
        victory_for(board, 'o')
        if winner == True: break
        draw_move(board)
        victory_for(board, 'x')
        if winner == True: break

abcdefg




