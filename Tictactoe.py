from random import randint

print('\033[35mДобро пожаловать в игру крестики-нолики\033[0;0m')
gorizontal = (1, 2, 3)
vertical = ('a', 'b', 'c')


board = [['-'] * 3 for i in range(3)]

# Выбор символа
def user():
    while True:
        userChar = input('Выбери символ x, o: ').lower()
        if len(userChar) == 1:
            pass
        else:
            print('\033[31mВыбери один символ\033[0;0m')
            continue
        if userChar != 'x' and userChar != 'o':
            print('\033[31mНе верный символ\033[0;0m')
            continue
        break
    return userChar

# Рисуем доску
def gameBoard(board):
    print(' ', '1', '2', '3')
    for s, v in enumerate(vertical):
        print(v, *board[s])

# Проверка ввода
def position(board):
    while True:
        realVert = 0
        realGorizontal = 0
        coordinate = input('Введите координаты: ').lower()
        cod = list(coordinate)


        if cod != '':
            pass
        else:
            print('\033[31mНи чего не введенно\033[0;0m')
            continue
        if len(cod) == 2:
            pass
        else:
            print('\033[31mМне нужны 2 координаты\033[0;0m')
            continue

        if cod[0] in vertical:
            pass
        else:
            print('\033[31mТакой координаты нет\033[0;0m')
            continue

        if not cod[1].isdigit():
            print('\033[31mНе число\033[0;0m')
            continue
        x = int(cod[1])
        if x in gorizontal:
            pass
        else:
            print('\033[31mТакой горизонтальной координаты нет\033[0;0m')
            continue
        y = cod[0]
        realVert = vertical.index(y)
        realGorizontal = x - 1
        if board[realVert][realGorizontal] == '-':
            pass
        else:
            print('\033[31mЯчейка занята\033[0;0m')
            continue
        break

    return realVert, realGorizontal

# Присваеваем символ оппоненту
def getComputerChar(char):
    return 'o' if userChar == 'x' else 'x'

userChar = user() #x
computerChar = getComputerChar(userChar) #o

# Не работает для оппонента
'''def win(char, board):
    opponentChar = getComputerChar(char)
    # Строки
    for x in range(3):
        if opponentChar not in board[x] and '-' not in board[x]:
            return True
    # Столбцы
    for y in range(3):
        col = board[0][y], board[1][y], board[2][y]
        if opponentChar not in col and '-' not in col:
            return True
    # Диагонали
    diag = board[0][0], board[1][1], board[2][2]
    if opponentChar not in diag and '-' not in diag:
        return True
    diag2 = board[0][2], board[1][1], board[2][0]
    if opponentChar not in diag2 and '-' not in diag2:
        return True
    return False'''


def search_winner(board, user):
    def winner(n1, n2, n3, user):
        if n1 == user and n2 == user and n3 == user:
            return True
    for i in range(3):
        if winner(board[i][0], board[i][1], board[i][2], user) or \
            winner(board[0][i], board[1][i], board[2][i], user) or \
            winner(board[0][0], board[1][1], board[2][2], user) or \
                winner(board[2][0], board[1][1], board[0][2], user):
            return True
    return False

# Выбирает координату
def computerMove(board):
    x, y = randint(0, 2), randint(0, 2)
    while True:
        if board[y][x] != '-':
            y, x = randint(0, 2), randint(0, 2)
        break
    return y, x

step = 0
while True:
    gameBoard(board)
    x, y = position(board)
    board[x][y] = userChar

    if search_winner(board, userChar):
        print('\033[35mТы выиграл!\033[0;0m')
        break
    x, y = computerMove(board)
    board[x][y] = computerChar
    if search_winner(board, computerChar):
        print('\033[35mТы проиграл\033[0;0m')
        break
    if step == 9:
        print('\033[35mНичья\033[0;0m')
        break
    step += 1
gameBoard(board)


