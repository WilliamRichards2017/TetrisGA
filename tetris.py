from random import randint
import sys

x = 0
y = 0

row = 22
col = 10

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

def get_tetramino():
    return randint(0, )


def rotate_tetramino(rotation):
    return rotation % 4


def remove_row():
    return null

def get_final_piece(block, rotation):
    return tetraminos[block][rotation]

def new_board():
	board = [ [ 0 for x in xrange(col) ]
			for y in xrange(row) ]
	board += [[ 1 for x in xrange(col)]]
	return board

def init_game(self):
		self.board = new_board()
		self.score = 0
		self.lines = 0

def place_piece(final_piece, drop_row):

    height = get_collision_height(board, final_piece, drop_row)

    for x in range(0, 5):
        for y in range(0,5):
            board[height+y][drop_row+x] += final_piece[y][x]


def get_collision_height(board, piece, row):
        return 1


board = new_board()

place_piece(get_final_piece(4,0),2)

print board





##print get_final_piece(get_tetramino(), rotate_tetramino(0))
