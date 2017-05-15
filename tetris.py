from random import randint

x = 0
y = 0

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
    return randint(0, 7)


def rotate_tetramino(rotation):
    return rotation % 4


def remove_row():
    return null

def get_final_piece(block, rotation):
    return tetraminos[block][rotation]

get_tetramino()
rotate_tetramino()
rotate_tetramino()


print x
print y
