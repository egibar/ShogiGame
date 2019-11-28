import unittest
import Shogi
from Shogi.Constants import *
from Shogi import *


class MoveTestCase(unittest.TestCase):
    def test_default(self):
        self.assertEqual(Board().turn,1)
        #self.assertEqual(board.piece_type_at,Shogi.PIECE_TYPES[7])

    def test_normalizer(self):
        board = Board()
        self.assertEqual(board.move('c 7','7 D'), True)

    def test_none_move(self):
        board = Board()
        self.assertEqual(board.move('F7','e7'), False)

    def  test_pawn_move(self):
        board = Board()
        self.assertEqual(board.move('G7','F7'),False) #White first
        self.assertEqual(board.move('C7','D7'),True)
        self.assertEqual(board.piece_at(20),None) #G7
        self.assertEqual(board.piece_at(29).piece_type, PAWN) #F7
        #self.assertEqual(board.move('G3','H3'),False) '''The move should be invalid'''


    def  test_lance_move(self):
        pass

    def  test_knight_move(self):
        pass

    def  test_silver_move(self):
        pass

    def  test_gold_move(self):
        pass

    def  test_bishop_move(self):
        pass

    def  test_rook_move(self):
        pass

    def  test_king_move(self):
        pass