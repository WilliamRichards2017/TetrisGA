import graphics as gs
from Board import *
from Pieces import *
import random


def isValid(position):
	'''returns 1, 2, 3, or 4 if valid, else 0'''
	if position == None or position.getX() < 700:
		return 0
	if position.getY() < 200: 
		return 1
	elif position.getY() < 400:
		return 2
	elif position.getY() < 600:
		return 3
	return 4

def isValidCol(position):
	'''returns 0 if not valid col, else returns colNum'''
	if position == None or position.getX() < 80 or position.getX() > 520:
		return 0
	else:
		return position.getX() // 40
value = 1
lines = 0
board = Board(10, 22)
window = gs.GraphWin("tetris",  (15*40) + 300, 880)
scoreTXT = gs.Text(gs.Point(700, 850), "Your Score is 0")
scoreTXT.draw(window)
redraw = False

things = []

for i in range(len(board.board)):
		for j in range(len(board.board[i])):
			r = gs.Rectangle(gs.Point(j * 40, i * 40), gs.Point((j+1) * 40, (i+1) * 40) )
			r.draw(window)
			things.append(r)
prevVals = [0]*len(things)


PiecesToShow = []
for i in range(20):
	for j in range(5):
		r = gs.Rectangle(gs.Point((700 + j * 40),i * 40), gs.Point(700 + ((j+1) * 40), (i+1) * 40 ))
		r.draw(window)
		PiecesToShow.append(r)

while value != -1:
	index = 0
	for i in range(len(board.board)):
		for j in range(len(board.board[i])):
			if board.board[i][j] != prevVals[index] or redraw:
				r = things[index]
			
				if board.board[i][j] == 1:
					r.setFill("red")
					prevVals[index] = 1	
				else:
					r.setFill("white")
					prevVals[index] = 0
			
			index += 1
			
				


	pieceNum = random.randint(0, 6)
	piece = Piece(pieceNum)
	#print(board)
	output = [piece.getPieceArray(i) for i in range(4)]
	index = 0
	for k in range(len(output)):
		p = output[k]
		for i in range(5):
			for j in range(5):
				if p[i][j] == 1:
					PiecesToShow[index].setFill("blue")
				elif p[i][j] == 2:
					PiecesToShow[index].setFill("green")
				else:
					PiecesToShow[index].setFill("white")
				index +=1
					
							
		
		
		
	#rotation = int(raw_input("Which rotation do you want the piece (0-3)?: "))
	txt = gs.Text(gs.Point(700, 820), "click on a piece")
	txt.draw(window)
	position = None
	while not isValid(position):
		position = window.getMouse()
	txt.undraw()
	rotation = isValid(position) - 1
	txt = gs.Text(gs.Point(700, 820), "click on a column")
	txt.draw(window)
	position = None
	while not isValidCol(position):
		position = window.getMouse()
	txt.undraw()
	col = isValidCol(position)
	value = board.addPiece(piece, rotation, col)
	cleared = board.clearRows()
	redraw = False
	if cleared > 0:
		lines = lines + cleared
		redraw = True
	scoreTXT.setText("Your score is " + str(lines))
#print("game over")
gs.Text(gs.Point(420, 420), "GAME OVER. YOUR FINAL SCORE IS " + str(lines)).draw(window)
window.getMouse()
