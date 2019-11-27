from Shogi.Constants import *

class Piece(object):
    def __init__(self, piece_type, color):
        self.piece_type = piece_type
        self.color = color

    def symbol(self):
        if self.color == BLACK:
            direction = '^'
            return PIECE_SYMBOLS[self.piece_type].upper() + direction
        else:
            direction = 'v'
            return PIECE_SYMBOLS[self.piece_type] + direction