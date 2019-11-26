COLORS = [BLACK, WHITE] = range(2)

PIECE_TYPES = [
           PAWN,      LANCE,      KNIGHT,      SILVER,
           GOLD,
         BISHOP,       ROOK,
           KING,
]= range(8)

PIECE_SYMBOLS = ['p',  'l',  'n',  's', 'g',  'b',  'r', 'k']

class Piece(object):
    def __init__(self, piece_type, color):
        self.piece_type = piece_type
        self.color = color

    def symbol(self):
        if self.color == BLACK:
            return PIECE_SYMBOLS[self.piece_type].upper()
        else:
            return PIECE_SYMBOLS[self.piece_type]