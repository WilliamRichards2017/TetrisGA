import numpy as np

class Board:
	def __init__(self, width,height):
		self.width = width + 4
		self.height = height
		self.board = np.array([[0]*self.width]*self.height)
		self.board[:,0:2] = np.array([[1]*2]*self.height)
		self.board[:,self.width-2:self.width] = np.array([[1]*2]*self.height)
		self.testArray = np.array([1]*self.width)
		self.replacementArray = np.concatenate(([1, 1], [0]*width, [1, 1]))
	
	def __str__(self):
		return str(np.vstack((self.board, np.array(range(self.width))))) #adding col nums

	
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
		for row in range(self.height-pHeight + 1):
			smallBoard = self.board[row:row+pHeight, column-2:column+3]
			#print smallBoard
			#print pieceArray
			try:
				newBoard = smallBoard + pieceArray
				print newBoard
			except:
				return -1
				
			
			if row + piece.getBottom(rotation) - piece.getTop(rotation) >= self.height: #bottom collision
				bestRow = row - 1
				print "hit bottom!"
				break

			print np.amax(newBoard)
			if np.amax(newBoard) > 1:
				bestRow = row - 1
				print "yup"
				break
		if bestRow < 0:
			return -1
		#print self.board[bestRow:bestRow+pHeight, column-2:column+3]
		#print 
		self.board[bestRow:bestRow+pHeight, column-2:column+3] = pieceArray + self.board[bestRow:bestRow+pHeight, column-2:column+3]
		return 1 

	def clearRows(self):
		'''returns number of rows cleared. Updates board'''
		count = 0
		for i in range(len(self.board)):
			row = self.board[i]
			if np.array_equal(row, self.testArray):
				self.board[0:i+1] = np.roll(self.board[0:i+1], self.width) 
				self.board[0] = self.replacementArray
				count += 1
		return count


		
		
		
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
		