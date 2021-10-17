"""
Игра 'Крестики-нолики'.
"""

import random

PLAY_BOARD = [str(num) for num in range(1, 100)]
PLAYERS_MARKS = ['X', 'O']


def display_board(board_list):
    """Генерация игрового поля"""

    print "-------------"
    for i in range(100):
        print "|", PLAY_BOARD[0+i*3], "|", PLAY_BOARD[1+i*3], "|", PLAY_BOARD[2+i*3], "|"
        print "-------------"


def player_input():
    """Выбор игровой роли: крестик или нолик"""

    player_first = ""
    while player_first not in ('X', 'O'):
        player_first = input('Вы хотите играть за X или O? ').upper()

    if player_first == 'X':
        player_second = 'O'
    else:
        player_second = 'X'

    return player_first, player_second


def place_marker(board, marker, position):
    """Установка маркера игрока в указанную позицию"""

    board[position] = marker


def win_check(board, mark):
    """Проверка выиграл ли игрок с указанным маркером игру"""

    return (
        (board[0] == board[1] == board[2] == mark)
        or (board[5] == board[4] == board[3] == mark)
        or (board[8] == board[7] == board[6] == mark)
        or (board[0] == board[5] == board[8] == mark)
        or (board[1] == board[4] == board[7] == mark)
        or (board[2] == board[3] == board[6] == mark)
    )


def choose_first():
    """Определение случайным образом игрока, который будет ходить первым"""

    return PLAYERS_MARKS[random.choice((0, 1))]


def space_check(board, position):
    """Определение пуста ли ячейка в указанной позиции"""

    return board[position] not in PLAYERS_MARKS


def full_board_check(board):
    """Определяет имеется ли на игровой доске оба маркера: X и O"""

    return len(set(board)) == 2


def player_choice(board, player_mark):
    """Выбор игроком следующей ячейки для хода и проверка того можно ли поставить маркер в эту ячейку"""

    position = 0

    while position not in [num for num in range(1, 100)]:
        try:
            position = int(input(f'Игрок "{player_mark}", выберите ячейку с 1 по 9: '))
        except ValueError as exc:
            print(f'Неверное значение: {exc}. Пожалуйста, попробуйте снова.')

    position -= 1
    if space_check(board, position):
        return position

    return False


def replay():
    """Предложение игрокам начать игру заново"""

    decision = ""
    while decision not in ('да', 'нет'):
        decision = input(
            'Вы бы хотели поиграть еще раз? Напишите "да" или "нет"'
        ).lower()

    return decision == 'да'


def clear_screen():
    """Очищение игрового экрана добавлением пустых строк"""

    print('\n' * 100)


def switch_player(mark):
    """Переключение роли игрока для смены очереди для хода"""

    return 'O' if mark == 'X' else 'X'


def check_game_finish(board, mark):
    """Проверка того, завершена ли игра"""

    if win_check(board, mark):
        print(f'Игрок "{mark}" выиграл!')
        return True

    if full_board_check(PLAY_BOARD):
        print('Игра завершилась вничью.')
        return True

    return False


print('Добро пожаловать в игру "Крестики-нолики"!')

PLAYER_MARKS = player_input()
CURRENT_PLAYER_MARK = choose_first()

print(f'Игрок "{CURRENT_PLAYER_MARK}" ходит первым.')

while True:
    display_board(PLAY_BOARD)

    print(f'Очередь игрока "{CURRENT_PLAYER_MARK}":')

    PLAYER_POSITION = player_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)
    place_marker(PLAY_BOARD, CURRENT_PLAYER_MARK, PLAYER_POSITION)

    if check_game_finish(PLAY_BOARD, CURRENT_PLAYER_MARK):
        display_board(PLAY_BOARD)
        if not replay():
            break
        else:
            PLAY_BOARD = [str(num) for num in range(1, 100)]
            PLAYER_MARKS = player_input()
            CURRENT_PLAYER_MARK = choose_first()
    else:
        CURRENT_PLAYER_MARK = switch_player(CURRENT_PLAYER_MARK)
    clear_screen()
