# -*- coding: utf-8 -*-

board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'X'
print(board)

weird_board = [['_'] * 3] * 3
print(weird_board)

#: Placing a mark in row1, column 2,
#: reveals that all rows are aliases referring to the same object.
weird_board[1][2] = '0'
print(weird_board)

