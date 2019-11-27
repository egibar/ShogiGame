import unittest
import Shogi
from Shogi.Constants import *


class BoardTestCase(unittest.TestCase):
    def test_start_positions(self):
        board = Shogi.Board()
        self.assertEqual(board.turn,1)
        self.assertEqual(board.piece_at(56).piece_type, PAWN)  # G7
        self.assertEqual(board.piece_at(64).piece_type, BISHOP)  # H8
        self.assertEqual(board.piece_at(70).piece_type, ROOK)  # H2
        self.assertEqual(board.piece_at(72).piece_type, LANCE)  # I9
        self.assertEqual(board.piece_at(73).piece_type, KNIGHT)  # I8
        self.assertEqual(board.piece_at(74).piece_type, SILVER)  # I7
        self.assertEqual(board.piece_at(75).piece_type, GOLD)  # I6
        self.assertEqual(board.piece_at(76).piece_type, KING)  # I5
        self.assertEqual(board.piece_at(77).piece_type, GOLD)  # I4
        self.assertEqual(board.piece_at(78).piece_type, SILVER)  # I3
        self.assertEqual(board.piece_at(79).piece_type, KNIGHT)  # I2
        self.assertEqual(board.piece_at(80).piece_type, LANCE)  # I1

