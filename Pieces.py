from random import randint
import sys
import numpy as np


class Piece:
	def __init__(self, pieceNum):
	
		self.piece = tetraminos[pieceNum]
		self.piece = [np.array(p) for p in self.piece]
		self.leftMost = [4, 4, 4, 4]
		self.rightMost = [0, 0, 0, 0]
		self.bottom = [2]*4
		self.top = [2]*4
		
		for j in range(4):
			i = 0
			for row in self.piece[j]:
				if 1 in row:
					self.bottom[j] = i
					if i < self.top[j]:
						self.top[j] = i
				i += 1 
		
		for j in range(4):
			i = 0
			for column in self.piece[j].T:
				if 1 in column:
					self.rightMost[j] = i
					if i < self.leftMost[j]:
						self.leftMost[j] = i
				i += 1
		
	def __str__(self):
		return str(self.piece[0])
	
	def getLeftSide(self, rotation = 0):
		'''takes in an int from 0-3, returns the first row with a block (0-4)'''
		return self.leftMost[rotation]
	
	def getBottom(self, rot):
		return self.bottom[rot]
	
	def getTop(self, rot):
		return self.top[rot]
	
	def getRightSide(self, rotation = 0):
		return self.rightMost[rotation]
	
	def getPieceArray(self, rotation = 0):
		try:
			return self.piece[rotation]
		except:
			print (rotation, "is not a valid rotation value. Returning default")  
			return self.piece[0]
  
		
		
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
				[0,0,1,0,0],
				[0,1,2,0,0],
				[0,1,0,0,0],
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