import random as rd
from constants import constants
# This class initializes and defines the game

class game:
    def __init__(self, board, player_white, player_black):
        self.game_id = rd.randint(100000, 999999)
        self.board = board
        self.player_white = player_white
        self.player_black = player_black
        self.num_of_moves = 0
        self.status = constants.IN_PROGRESS
        self.game_stats = {}


    def start(self):
        self.board.assign_pos(self.player_white)
        self.board.assign_pos(self.player_black)

    # game is now set to start, piece in place

    def end(self):
        self.status = constants.DRAW
        self.game_stats = {}
