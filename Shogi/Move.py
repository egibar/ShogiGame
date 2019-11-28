from Shogi.Piece import *
from Shogi.Board import *

class Move(object):
    def __init__(self,from_square, to_square):
        self.from_square = from_square
        self.to_square = to_square

    @classmethod
    def get_squares(cls,from_square, to_square):
        from_square=cls.normalize_squares(cls,from_square)
        to_square=cls.normalize_squares(cls,to_square)
        piece_from=SQUARE_NAMES.index(from_square.upper())
        piece_to=SQUARE_NAMES.index(to_square.upper())
        return cls(piece_from, piece_to)

    def normalize_squares(self,square):
        square=square.replace(' ','')
        if (square[0].isdigit()):
            aux = square[1]
            square=square.replace(square[1],square[0])
            square=square.replace(square[0], aux,1)
        return square

    def is_a_valid_move(self,piece,piece_from,piece_to):
        return True

    def is_a_valid_attack(self,piece,piece_from,piece_to):
        return True


    def can_promote(square, piece_type, color):
        if piece_type not in [PAWN, LANCE, KNIGHT, SILVER, BISHOP, ROOK]:
            return False
        elif color == BLACK:
            return square//9 <= 2
        else:
            return square//9 >= 6

