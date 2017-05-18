#PlayTetris.py
from Board import *
from Pieces import *
import numpy as np
import random

value = 1
lines = 0
board = Board(10, 22)
while value != -1:
	pieceNum = random.randint(0, 6)
	piece = Piece(pieceNum)
	print(board)
	output = [piece.getPieceArray(i) for i in range(4)]
	for thing in output:
		print thing
	rotation = int(raw_input("Which rotation do you want the piece (0-3)?: "))
	col = int(raw_input("Which column do you want to place it in? "))
	value = board.addPiece(piece, rotation, col)

print("game over")