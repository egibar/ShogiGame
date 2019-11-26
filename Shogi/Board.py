from Shogi.Move import *
from Shogi.Piece import *


SQUARES = [
    A9, A8, A7, A6, A5, A4, A3, A2, A1,
    B9, B8, B7, B6, B5, B4, B3, B2, B1,
    C9, C8, C7, C6, C5, C4, C3, C2, C1,
    D9, D8, D7, D6, D5, D4, D3, D2, D1,
    E9, E8, E7, E6, E5, E4, E3, E2, E1,
    F9, F8, F7, F6, F5, F4, F3, F2, F1,
    G9, G8, G7, G6, G5, G4, G3, G2, G1,
    H9, H8, H7, H6, H5, H4, H3, H2, H1,
    I9, I8, I7, I6, I5, I4, I3, I2, I1,
] = range(81)

B_SQUARES = [
    B_A9, B_A8, B_A7, B_A6, B_A5, B_A4, B_A3, B_A2, B_A1,
    B_B9, B_B8, B_B7, B_B6, B_B5, B_B4, B_B3, B_B2, B_B1,
    B_C9, B_C8, B_C7, B_C6, B_C5, B_C4, B_C3, B_C2, B_C1,
    B_D9, B_D8, B_D7, B_D6, B_D5, B_D4, B_D3, B_D2, B_D1,
    B_E9, B_E8, B_E7, B_E6, B_E5, B_E4, B_E3, B_E2, B_E1,
    B_F9, B_F8, B_F7, B_F6, B_F5, B_F4, B_F3, B_F2, B_F1,
    B_G9, B_G8, B_G7, B_G6, B_G5, B_G4, B_G3, B_G2, B_G1,
    B_H9, B_H8, B_H7, B_H6, B_H5, B_H4, B_H3, B_H2, B_H1,
    B_I9, B_I8, B_I7, B_I6, B_I5, B_I4, B_I3, B_I2, B_I1,
] = [1 << i for i in SQUARES]

B_COLUMS = [
    B_COLUM_9,
    B_COLUM_8,
    B_COLUM_7,
    B_COLUM_6,
    B_COLUM_5,
    B_COLUM_4,
    B_COLUM_3,
    B_COLUM_2,
    B_COLUM_1,
] = [
    B_A9 | B_B9 | B_C9 | B_D9 | B_E9 | B_F9 | B_G9 | B_H9 | B_I9,
    B_A8 | B_B8 | B_C8 | B_D8 | B_E8 | B_F8 | B_G8 | B_H8 | B_I8,
    B_A7 | B_B7 | B_C7 | B_D7 | B_E7 | B_F7 | B_G7 | B_H7 | B_I7,
    B_A6 | B_B6 | B_C6 | B_D6 | B_E6 | B_F6 | B_G6 | B_H6 | B_I6,
    B_A5 | B_B5 | B_C5 | B_D5 | B_E5 | B_F5 | B_G5 | B_H5 | B_I5,
    B_A4 | B_B4 | B_C4 | B_D4 | B_E4 | B_F4 | B_G4 | B_H4 | B_I4,
    B_A3 | B_B3 | B_C3 | B_D3 | B_E3 | B_F3 | B_G3 | B_H3 | B_I3,
    B_A2 | B_B2 | B_C2 | B_D2 | B_E2 | B_F2 | B_G2 | B_H2 | B_I2,
    B_A1 | B_B1 | B_C1 | B_D1 | B_E1 | B_F1 | B_G1 | B_H1 | B_I1,
]

B_ROW = [
    B_ROW_A,
    B_ROW_B,
    B_ROW_C,
    B_ROW_D,
    B_ROW_E,
    B_ROW_F,
    B_ROW_G,
    B_ROW_H,
    B_ROW_I
] = [
    B_A1 | B_A2 | B_A3 | B_A4 | B_A5 | B_A6 | B_A7 | B_A8 | B_A9,
    B_B1 | B_B2 | B_B3 | B_B4 | B_B5 | B_B6 | B_B7 | B_B8 | B_B9,
    B_C1 | B_C2 | B_C3 | B_C4 | B_C5 | B_C6 | B_C7 | B_C8 | B_C9,
    B_D1 | B_D2 | B_D3 | B_D4 | B_D5 | B_D6 | B_D7 | B_D8 | B_D9,
    B_E1 | B_E2 | B_E3 | B_E4 | B_E5 | B_E6 | B_E7 | B_E8 | B_E9,
    B_F1 | B_F2 | B_F3 | B_F4 | B_F5 | B_F6 | B_F7 | B_F8 | B_F9,
    B_G1 | B_G2 | B_G3 | B_G4 | B_G5 | B_G6 | B_G7 | B_G8 | B_G9,
    B_H1 | B_H2 | B_H3 | B_H4 | B_H5 | B_H6 | B_H7 | B_H8 | B_H9,
    B_I1 | B_I2 | B_I3 | B_I4 | B_I5 | B_I6 | B_I7 | B_I8 | B_I9,
]

class Board(object):

    def __init__(self):
        self.start()

    def start(self):
        self.piece_b = [
            B_ROW_C | B_ROW_G,  # PAWN
            B_A1 | B_I1 | B_A9 | B_I9,  # LANCE
            B_A2 | B_A8 | B_I2 | B_I8,  # KNIGHT
            B_A3 | B_A7 | B_I3 | B_I7,  # SILVER
            B_A4 | B_A6 | B_I4 | B_I6,  # GOLD
            B_B2 | B_H8,  # BISHOP
            B_B8 | B_H2,  # ROOK
            B_A5 | B_I5,  # KING
        ]

        self.turn = BLACK

        self.pieces = [0 for i in SQUARES]  # CREATE THE EMPTY BOARD

        for i in SQUARES:
            mask = B_SQUARES[i]
            for piece_type in PIECE_TYPES:
                if mask & self.piece_b[piece_type]:
                    self.pieces[i] = piece_type