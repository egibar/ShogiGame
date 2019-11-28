from Shogi.Move import *
from Shogi.Piece import *
from Shogi.Board import *

class Main:
    if __name__ == "__main__":
        board=Board()
        i=0
        TURN = ['BLACK', 'WHITE']

        while (not board.is_check_mate()):
            print(board)
            print('Turn #'+str(i)+":    "+str(TURN[i%2]))
            #print(board.turn)
            from_square = input('FROM (row col):  ')
            to_square = input('TO (row col):  ')
            move_success=board.move(from_square,to_square)
            if (move_success):
                i = i + 1
            else:
                print("The movement was not valid. Repeat please.")
            #TODO: User board.turn to count the turn, and created the number of moves
