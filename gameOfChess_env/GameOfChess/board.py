from constants import constants

# This class initializes and defines the board
class board:
    def __init__(self):
        self.pos_map = {f'{letter}{num}' : None for letter in 'abcdefgh' for num in range(1, 9)}
        self.board_history = [self.pos_map] 

    def assign_pos(self, player):
        for attr, piece in vars(player).items():
            if hasattr(piece, 'pos'):
                if(not self.pos_map[piece.pos]):
                    self.pos_map[piece.pos] = piece

    def update_board(self, piece):
        if(piece.pos in self.pos_map):
            self.pos_map[piece.pos] = piece
            self.board_history.append(self.pos_map)

            
