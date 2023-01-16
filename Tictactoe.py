import sys


print(f'\033[35mДобро пожаловать в игру крестики-нолики\033[0;0m')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


gameBoard = [[' -'] * 3 for i in range(3)]


def drawBoard(board):
    print("   0  1  2")
    for i in range(len(gameBoard)):
        print(i, *gameBoard[i])


def coorInput(board):
    while True:
        coordinate = input(f'\nХодит{user}\nВведите координаты: ').split()
        if len(coordinate) != 2:
            print('\033[31mВведите 2 числа через пробел\033[0;0m')
            continue
        if not (coordinate[0].isdigit() and coordinate[1].isdigit()):
            print('\033[31mТолько числа\033[0;0m')
            continue
        x, y = map(int, coordinate)
        if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print('\033[31mДва числа от 0 до 2\033[0;0m')
            continue
        if board[x][y] != ' -':
            print('\033[31mКлетка занята\033[0;0m')
            continue
        break
    return x, y


def search_winner(board, user):
    def winner(n1, n2, n3, user):
        if n1 == user and n2 == user and n3 == user:
            print(f'\033[35mВыиграл{user}\033[0;0m')
            return True
    for i in range(3):
        if winner(board[i][0], board[i][1], board[i][2], user) or \
            winner(board[0][i], board[1][i], board[2][i], user) or \
            winner(board[0][0], board[1][1], board[2][2], user) or \
                winner(board[2][0], board[1][1], board[0][2], user):
            return True
    return False


count = 0
while True:
    if count % 2 == 0:
        user = ' x'
    else:
        user = ' o'
    drawBoard(gameBoard)
    x, y = coorInput(gameBoard)
    gameBoard[x][y] = user
    count += 1
    if count == 9:
        print('Ничья', file=sys.stderr)
    if search_winner(gameBoard, user):
        drawBoard(gameBoard)
        break

