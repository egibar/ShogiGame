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

    def test_attack_move(self):
        board = Shogi.Board()
        self.assertEqual(board.move('C7','G7'),True)#It should be False once is_valid_attack is implemented

    def test_attack_same_color(self):
        board=Shogi.Board()
        self.assertEqual(board.move('A7','C7'), False)

    def test_remove_piece(self):
        board = Shogi.Board()
        self.assertEqual(board.piece_at(56).piece_type, PAWN)  # G7
        board.remove_piece_at(56)
        self.assertEqual(board.piece_at(56), None)  # G7


    def test_set_piece_at(self):
        board = Shogi.Board()
        piece = board.piece_at(56)
        board.set_piece_at(47,piece)
        self.assertEqual(board.piece_at(47).piece_type, PAWN)  # G7




