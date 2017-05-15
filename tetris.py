from random import randint
import sys

## Declare board size
row = 22
col = 10

## 4x4 array storing all possible tetrimino configurations
## Pieces are stored in 5x5 bit arrays so we can perform
## rotation operations only using lookup
tetraminos = [[[[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,2,1,0],
                [0,0,1,1,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,2,1,0],
                [0,0,1,1,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,2,1,0],
                [0,0,1,1,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,2,1,0],
                [0,0,1,1,0],
                [0,0,0,0,0]]],
              [[[0,0,0,0,0],
                [0,0,0,0,0],
                [0,1,2,1,1],
                [0,0,0,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,2,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0]],
               [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,1,2,1,1],
                [0,0,0,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,2,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0]]],
              [[[0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,2,0,0],
                [0,0,1,1,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,1,2,1,0],
                [0,1,0,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,1,1,0,0],
                [0,0,2,0,0],
                [0,0,1,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,0,1,0],
                [0,1,2,1,0],
                [0,0,0,0,0],
                [0,0,0,0,0]]],
              [[[0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,2,0,0],
                [0,1,1,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,1,0,0,0],
                [0,1,2,1,0],
                [0,0,0,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,1,1,0],
                [0,0,2,0,0],
                [0,0,1,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,1,2,1,0],
                [0,0,0,1,0],
                [0,0,0,0,0]]],
              [[[0,0,0,0,0],
                [0,0,0,1,0],
                [0,0,2,1,0],
                [0,0,1,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,1,2,0,0],
                [0,0,1,1,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,0,1,0],
                [0,0,1,2,0],
                [0,0,1,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,1,2,0,0],
                [0,0,1,1,0],
                [0,0,0,0,0]]],
              [[[0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,2,1,0],
                [0,0,0,1,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,2,1,0],
                [0,1,1,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,2,1,0],
                [0,0,0,1,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,2,1,0],
                [0,1,1,0,0],
                [0,0,0,0,0]]],
              [[[0,0,0,0,0],
                [0,0,0,0,0],
                [0,1,2,1,0],
                [0,0,1,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,1,0,0],
                [0,1,2,0,0],
                [0,0,1,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,1,0,0],
                [0,1,2,1,0],
                [0,0,0,0,0],
                [0,0,0,0,0]],
               [[0,0,0,0,0],
                [0,0,1,0,0],
                [0,0,2,1,0],
                [0,0,1,0,0],
                [0,0,0,0,0]]]]

## Generate random int corresponding to index storing a tetramino
def get_tetramino():
    return randint(0, 7)

## Returns int corresponding to index of rotated
## tetramino configuration
def rotate_tetramino(rotation):
    return rotation % 4

##Helper function to remove row
## Todo: shift board down after row break
def remove_row(r):
    for x in range(0,10):
        board[r][x] = 0



def get_final_piece(block, rotation):
    return tetraminos[block][rotation]

## Initilize a 22x10 boardstate with a bottom row of 1's
## and the rest 0 values with list comprehension.
def new_board():
	board = [ [ 0 for x in xrange(col) ]
			for y in xrange(row) ]
	board += [[ 1 for x in xrange(col)]]
	return board


## Input: piece to play, row to drop the piece from
## Output: updates boardstate to represent placed piece
def place_piece(final_piece, drop_row):

    height = get_collision_height(board, final_piece, drop_row)

    for x in range(0, 5):
        for y in range(0,5):
            board[height+y][drop_row+x] += final_piece[y][x]

## returns the highest row # at which a piece will collide
## with something given a piece to play and row to drop
## it from
def get_collision_height(piece, row):
        return 0

## returns how much space there is between a piece and the
## left and right edges of its corresponding 5x5 bitmatrix
def piece_buffer(piece):


board = new_board()

place_piece(get_final_piece(4,0),1)
place_piece(get_final_piece(6,1),4)

print board

def init_game(self):
		self.board = new_board()
		self.score = 0
		self.lines = 0






##print get_final_piece(get_tetramino(), rotate_tetramino(0))
