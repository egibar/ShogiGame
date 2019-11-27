import Shogi
import collections
from Shogi.Move import *
from Shogi.Piece import *
from Shogi.Constants import *

class Board(object):

    def __init__(self):
        self.start()

    def start(self):
        self.piece_b = [
            B_VOID,                     #NONE
            B_ROW_C | B_ROW_G,          # PAWN
            B_A1 | B_I1 | B_A9 | B_I9,  # LANCE
            B_A2 | B_A8 | B_I2 | B_I8,  # KNIGHT
            B_A3 | B_A7 | B_I3 | B_I7,  # SILVER
            B_A4 | B_A6 | B_I4 | B_I6,  # GOLD
            B_B2 | B_H8,                # BISHOP
            B_B8 | B_H2,                # ROOK
            B_A5 | B_I5,                # KING
            B_VOID,                     # PROM_PAWN
            B_VOID,                     # PROM_LANCE
            B_VOID,                     # PROM_KNIGHT
            B_VOID,                     # PROM_SILVER
            B_VOID,                     # PROM_BISHOP
            B_VOID,                     # PROM_ROOK
        ]

        self.turn = WHITE

        self.pieces_in_hand = [collections.Counter(), collections.Counter()]

        self.occupied = Occupied(B_ROW_G | B_H2 | B_H8 | B_ROW_I, B_ROW_A | B_B2 | B_B8 | B_ROW_C)

        self.pieces = [0 for i in SQUARES]  # CREATE THE EMPTY BOARD

        for i in SQUARES:
            mask = B_SQUARES[i]
            for piece_type in PIECE_TYPES:
                if mask & self.piece_b[piece_type]:
                    self.pieces[i] = piece_type

    def is_check_mate(self):
        #TODO: Look if it is a check mate
        return False

    def is_check(self):
        #TODO: Look if it is a check
        pass

    def piece_at(self, square):
        mask = B_SQUARES[square]
        color = int(bool(self.occupied[WHITE] & mask))

        piece_type = self.piece_type_at(square)
        if piece_type:
            return Piece(piece_type, color)

    def piece_type_at(self, square):
        return self.pieces[square]


    def remove_piece_at(self, square):
        piece_type = self.piece_type_at(square)

        if piece_type == NONE:
            return

        mask = B_SQUARES[square]

        self.piece_b[piece_type] ^= mask

        color = int(bool(self.occupied[WHITE] & mask))

        self.pieces[square] = NONE
        self.occupied.update(mask, color)

    def set_piece_at(self, square, piece):
        self.remove_piece_at(square)

        self.pieces[square] = piece.piece_type

        mask = B_SQUARES[square]

        piece_type = piece.piece_type

        self.piece_b[piece_type] |= mask

        self.occupied.update(mask, piece.color)

    def add_piece_to_hand(self,piece_type,color):
        pass

    def remove_piece_off_hand(self,piece_type,color):
        pass

    def is_piece_in_hand(self,piece_type,color):
        pass

    def move(self,from_square, to_square):
        #TODO: Improve the reason why the move is invalid.
        move = Shogi.Move.get_squares(from_square, to_square)
        piece = self.piece_at(move.from_square)
        piece_to_go=self.piece_at(move.to_square)
        if (piece_to_go !=None):
            if (piece_to_go.color!=self.turn & Shogi.Move.is_a_valid_attack(self,piece,move.from_square,move.to_square)):
                self.add_piece_to_hand(piece_to_go.piece_type,self.turn)
                self.remove_piece_at(move.from_square)
                self.set_piece_at(move.to_square, Piece(piece.piece_type, self.turn))
                self.turn ^= 1
                return True
            else:
                return False
        elif(piece.piece_type!=0):
            if (piece.color==self.turn & Shogi.Move.is_a_valid_move(self,piece,move.from_square,move.to_square)):
                self.remove_piece_at(move.from_square)
                self.set_piece_at(move.to_square, Piece(piece.piece_type, self.turn))
                self.turn ^= 1
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        builder = []
        builder.append("--------WHITE-------------\n")
        builder.append("Captured:    \n")
        builder.append("9:  \n")
        builder.append("    9   8   7   6   5   4   3   2   1\n")
        builder.append("  --------------------------------------\n")
        i=0
        for square in SQUARES:
            piece = self.piece_at(square)
            if B_SQUARES[square] & B_COLUM_9:
                builder.append(ROW_NAMES[i])
                builder.append(' |')
                i = i + 1

            if piece:
                builder.append(' '+piece.symbol())
            else:
                builder.append(' - ')
            if B_SQUARES[square] & B_COLUM_1:
                builder.append('  |')
                if square != I1:
                    builder.append('\n')
            else:
                builder.append(' ')
        builder.append('\n')
        builder.append("  --------------------------------------\n")
        builder.append("Captured:    \n")
        builder.append("9:  \n")
        builder.append("---------BLACK------------\n")
        return ''.join(builder)


class Occupied(object):
    def __init__(self, occupied_by_black, occupied_by_white):
        self.by_color = [occupied_by_black, occupied_by_white]
        self.bits = occupied_by_black | occupied_by_white

    def __getitem__(self, key):
        if key in COLORS:
            return self.by_color[key]


    def update(self, mask, color):
        self.bits ^= mask
        self.by_color[color] ^= mask
