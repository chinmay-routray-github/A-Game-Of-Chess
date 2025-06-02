import chessman as chm 
from constants import constants


class helper:
    def initialize_pawns(player):
        if(player.color.lower() == constants.WHITE):
            for idx, x_pos in enumerate("abcdefgh", start = 1):
                pawn = chm.pawn(constants.PAWN, player.color, f'{x_pos}2')
                setattr(player, f'pawn{idx}', pawn)
        else:
            for idx, x_pos in enumerate("hgfedcba", start = 1):
                pawn = chm.pawn(constants.PAWN, player.color, f'{x_pos}7')
                setattr(player, f'pawn{idx}', pawn)

    # def initialize_pieces(player, color):
    #     if(color.lower() == constants.WHITE):
    #         sequence = "abcdefgh"
    #         p1, p2 = 0, len(sequence) -1 
    #         while(p1 < p2):
    #             if(sequence[p1] == "a"):
    #                 setattr(player, f"rook{p1}")
