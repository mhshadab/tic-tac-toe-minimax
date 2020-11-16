from math import inf as infinity
from random import choice
from random import seed as randomseed       # Paul Lu
import platform
import time
from os import system
"""
Muhtasim Haque Shadab
CCID:  shadab
"""

HUMAN = -1
COMP = +1

class Board:
    
    def __init__(self):
        self._board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ]

    

    def __str__(self):
        return(self.type)

    def __repr__(self):
        s = "<%d> %s" % (id(self), self.type)
        return(s)

    def get_board(self):
        return self._board


    def empty_cells(self):
        cells = []

        for x, row in enumerate(self.get_board()):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def valid_move(self,x,y):
        if [x,y] in self.empty_cells():
            return True
        else:
            return False

    def set_move(self,x, y, player):
        if self.valid_move(x, y):
            self._board[x][y] = player
            return True
        else:
            return False

class State:
    
    def __init__(self, board):
        self.board = board

    def __str__(self):
        return(self.type)

    def __repr__(self):
        s = "<%d> %s" % (id(self), self.type)
        return(s)
    