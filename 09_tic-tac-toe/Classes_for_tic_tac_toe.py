class Cell:

    def __init__(self, square):
        self.square = square

class Board:

    def __init__(self, board):
        self.board = board

    def print_board(self):
        print('\n')
        for i in range(0, 3):
            print(self.board[i].square, end = '   ')
        print('\n')
        for i in range(3, 6):
            print(self.board[i].square, end = '   ')
        print('\n')
        for i in range(6, 9):
            print(self.board[i].square, end = '   ')
        print('\n')

    def change_symb_on_board(self, symb, turn):
        self.board[turn].square = symb



class Player:

    def __init__(self, name, symb):
        self.name = name
        self.symb = symb


    def turn(self, free_cells):
        turn = int(input(f'Выберите номер клетки для хода из незанятых - {free_cells}: '))
        return turn


