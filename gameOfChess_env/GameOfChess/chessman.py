from constants import constants

# This class defines the creation of various Chess pieces
class chessman:
    def __init__(self, name, color, pos):
        self.name = name
        self.color = color
        self.pos = pos
        self.state = constants.ALIVE
        self.listOfPos = [self.pos]

    def move(self, next_pos):
        if(self.validate_move(next_pos)):
            self.pos = next_pos
            self.listOfPos.append(next_pos)
        return

    def validate_move(self, next_pos, board):
        l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        l2 = ['1', '2', '3', '4', '5', '6', '7', '8']
        if(next_pos[0] not in l1 or next_pos[1] not in l2):
            return False
        if(next_pos == self.pos):
            return False
        piece = board[next_pos]
        if(piece.color == self.color):
            return False
        return True

class rook(chessman):
    def validate_rook_move(self, next_pos, board):
        if(not self.validate_move(next_pos, board)):
            return False
        if(self.pos[0] == next_pos[0] or self.pos[1] == next_pos[1]):
            return True
        return False

class bishop(chessman):
    def validate_bishop_move(self, next_pos):
        if(not self.validate_move(next_pos, board)):
            return False
        if(abs(ord(next_pos[0]) - ord(self.pos[0])) == abs(int(next_pos[1]) - int(self.pos[0]))):
            return True
        return False

class pawn(chessman):
    def validate_pawn_move(self, next_pos, board):
        if(not self.validate_move(next_pos, board)):
            return False
        if(board[next_pos] == None and ((int(next_pos[1]) - int(self.pos[1]) == 1) and (next_pos[0] == self.pos[0]))):   
            return True 
        piece = board[next_pos]
        if(board[next_pos].color != self.color and ((int(next_pos[1]) - int(self.pos[1]) == 1) and (ord(next_pos[0]) - ord(self.pos[0]) == 1))):
            return True
        return False

class king(chessman):
    def validate_king_move(self, next_pos, board):
        if(not self.validate_move(next_pos, board)):
            return False
        if((int(next_pos[1]) - int(self.pos[1]) == 1) or (ord(next_pos[0]) - ord(self.pos[0]) == 1)):
            return True
        return False

class queen(chessman):
    def validate_queen_move(self, next_pos, board):
        if(not self.validate_move(next_pos, board)):
            return False
        if((self.pos[0] == next_pos[0] or self.pos[1] == next_pos[1]) and self.pos != next_pos):
            return True
        if(abs(ord(next_pos[0]) - ord(self.pos[0])) == abs(int(next_pos[1]) - int(self.pos[0]))):
            return True
        return False

class knight(chessman):
    def validate_knight_move(self, next_pos, board):
        if(not self.validate_move(next_pos, board)):
            return False
        if((abs(ord(next_pos[0]) - ord(self.pos[0])) == 2 and abs(int(next_pos[1]) - int(self.pos[0])) == 1)
         or (abs(ord(next_pos[0]) - ord(self.pos[0])) == 2 and abs(int(next_pos[1]) - int(self.pos[0])) == 1)):
            return True
        return False
        



            


    
