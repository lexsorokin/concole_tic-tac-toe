from Classes_for_tic_tac_toe import *
import random


def generate_board():
    cell_0 = Cell('[ ]')
    cell_1 = Cell('[ ]')
    cell_2 = Cell('[ ]')
    cell_3 = Cell('[ ]')
    cell_4 = Cell('[ ]')
    cell_5 = Cell('[ ]')
    cell_6 = Cell('[ ]')
    cell_7 = Cell('[ ]')
    cell_8 = Cell('[ ]')

    board = [cell_0, cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8]
    free_cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    return board, free_cells


def win_condition(turn_list, turn):
    win = False
    win_cond_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                     [1, 4, 2], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    turn_list.append(turn)

    for win_cond in win_cond_list:
        if turn_list == win_cond or turn_list == reversed(win_cond):
            win = True
    return win


symb_X = '[X]'
symb_O = '[O]'

board = Board(generate_board()[0])
free_cells = generate_board()[1]

player = Player('John', symb_X)
player_turn_list = []

computer = Player('Computer', symb_O)
computer_turn_list = []

while True:

    try:
        # ход игрока

        board.print_board() # вывод поля
        player_turn = player.turn(free_cells) # ход игрока на клетку
        while player_turn not in free_cells:
            print('Данная клетка уже занята, попробуйте снова:\n') # проверяем занята ли клетка
            player_turn = player.turn(free_cells)
        board.change_symb_on_board(player.symb, player_turn) # занимаем клетку
        free_cells.remove(player_turn) # убираем из списка свободных
        player_win = win_condition(player_turn_list, player_turn) # проверяем выиграл ли игрок

        # ход компьютера

        computer_turn = random.choice(free_cells)
        board.change_symb_on_board(computer.symb, computer_turn)
        free_cells.remove(computer_turn)
        computer_win = win_condition(computer_turn_list, computer_turn)

        if player_win:
            board.print_board()
            print(f'Игрок победил!')
            break
        elif computer_win:
            board.print_board()
            print(f'Компьютер победил!')
            break
    except:
        print('Не осталось больше свободных клеток! Ничья!')