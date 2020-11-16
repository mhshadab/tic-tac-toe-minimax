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
    def wins(self, player):
        state = self.board.get_board()
        win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
        ]
        if [player, player, player] in win_state:
            return True
        else:
            return False


    def evaluate(self):
        if self.wins(COMP):
            score = +1
        elif self.wins(HUMAN):
            score = -1
        else:
            score = 0

        return score

    def game_over(self):
        return self.wins(HUMAN) or self.wins(COMP)

    def minimax(self,state, depth, player):
        
        if player == COMP:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or self.game_over():
            score = self.evaluate()
            return [-1, -1, score]
        
        for cell in self.board.empty_cells():
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.minimax(state, depth - 1, -player)
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == COMP:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

    def ai_turn(self , c_choice, h_choice):
        depth = len(self.board.empty_cells())
        if depth == 0 or self.game_over():
            return

        clean()
        print(f'Computer turn [{c_choice}]')
        self.render(c_choice, h_choice)

        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = self.minimax(self.board.get_board(),depth, COMP)
            x, y = move[0], move[1]

        self.board.set_move(x, y, COMP)
        # Paul Lu.  Go full speed.
        # time.sleep(1)

    def human_turn(self,c_choice, h_choice):
  
        depth = len(self.board.empty_cells())
        if depth == 0 or self.game_over():
            return

        # Dictionary of valid moves
        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        clean()
        print(f'Human turn [{h_choice}]')
        self.render(c_choice, h_choice)

        while move < 1 or move > 9:
            try:
                move = int(input('Use numpad (1..9): '))
                coord = moves[move]
                can_move = self.board.set_move(coord[0], coord[1], HUMAN)

                if not can_move:
                    print('Bad move')
                    move = -1
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')
 

