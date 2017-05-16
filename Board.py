import numpy as np
import scipy as sc

class Board:
	def __init__(self, width,height):
		self.width = width
		self.height = height
		self.board = np.array([[0]*width]*height)
	
	def __str__(self):
		return str(self.board)
	
	def getBoard(self):
		return self.board
	
	def addPiece(self, piece, rotation, column):
		'''takes in piece of type Piece, its rotation, and a column number.
		Updates the board with the piece where the 2 block is in that column.
		If successful, return 1, if impossible placement return 0, if gameOver, return -1'''
		left = column - (2 - piece.getLeftSide(rotation))
		right = column + piece.getRightSide(rotation) - 2
		if left < 0 or right >= self.width:
			return 0
		
		pieceArray = piece.getPieceArray(rotation)
		pieceArray[2,2] = 1
		pieceArray = pieceArray[piece.getTop(rotation):piece.getBottom(rotation)+1, 0:5]
		pHeight = piece.getBottom(rotation) - piece.getTop(rotation) + 1
		bestRow = self.height - pHeight
		for row in range(self.height-pHeight):
			smallBoard = self.board[row:row+pHeight, column-2:column+3]
			#print smallBoard
			#print pieceArray
			newBoard = smallBoard + pieceArray
			#print newBoard
			
			if row + piece.getBottom(rotation) >= self.height: #bottom collision
				bestRow = row - 1
				break

			
			if np.amax(newBoard) > 1:
				bestRow = row - 1
				break
		if bestRow < 0:
			return -1
		#print self.board[bestRow:bestRow+pHeight, column-2:column+3]
		#print 
		self.board[bestRow:bestRow+pHeight, column-2:column+3] = pieceArray + self.board[bestRow:bestRow+pHeight, column-2:column+3]
		return 1 
		
		
		
		
'''		
from Board import *
from Pieces import *
b = Board(10, 10)
p = Piece(3)
b.addPiece(p, 0, 5)
b.addPiece(Piece(4), 0, 3)
print(b)
b.addPiece(Piece(4), 0, 3)
print(b)
'''
		