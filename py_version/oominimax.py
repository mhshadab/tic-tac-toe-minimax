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

    def get_board(self):
        return self._board