from constants import constants
import chessman as chm
from helper import helper as hlp

# This class initializes players
class player:
    def __init__(self, name, color):
        self.name = name
        if(color.lower() == constants.WHITE):
            self.color = constants.WHITE
        else:
            self.color = constants.BLACK
        self.status = constants.IN_PROGRESS
        self.initialize()

    def initialize(self):
        if(self.color.lower() == constants.WHITE):
            self.rook1 = chm.rook(constants.ROOK, constants.WHITE, 'a1')
            self.knight1 = chm.knight(constants.KNIGHT, constants.WHITE, 'b1')
            self.bishop1 = chm.bishop(constants.BISHOP, constants.WHITE, 'c1')
            self.queen = chm.queen(constants.QUEEN, constants.WHITE, 'd1')
            self.king = chm.king(constants.KING, constants.WHITE, 'e1')
            self.bishop2 = chm.bishop(constants.BISHOP, constants.WHITE, 'f1')
            self.knight2 = chm.knight(constants.KNIGHT, constants.WHITE, 'g1')
            self.rook2 = chm.rook(constants.ROOK, constants.WHITE, 'h1')
        else:
            self.rook1 = chm.rook(constants.ROOK, constants.BLACK, 'h8')
            self.knight1 = chm.knight(constants.KNIGHT, constants.BLACK, 'g8')
            self.bishop1 = chm.bishop(constants.BISHOP, constants.BLACK, 'f8')
            self.queen = chm.queen(constants.QUEEN, constants.BLACK, 'd8')
            self.king = chm.king(constants.KING, constants.BLACK, 'e8')
            self.bishop2 = chm.bishop(constants.BISHOP, constants.BLACK, 'c8')
            self.knight2 = chm.knight(constants.KNIGHT, constants.BLACK, 'b8')
            self.rook2 = chm.rook(constants.ROOK, constants.BLACK, 'a8')
        hlp.initialize_pawns(self)
        



