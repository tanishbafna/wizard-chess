import time
from cairosvg import svg2png
from chess import Outcome

import chess_model 
import chess_helper

#---------------------

file_name = 'input_moves.txt'
img_name = 'current_board.png'

#---------------------

newGame = chess_model.chessGame(file_name, img_name)

with open(file_name, 'w') as f:
    f.write('')

startClock = time.time()
while not newGame.move(chess_helper.getFirstMove(file_name), int(time.time() - startClock)):
    pass

while not newGame.board.outcome():
    startClock = time.time()
    while not newGame.move(chess_helper.getMove(newGame.node.move, file_name), int(time.time() - startClock)):
        pass

outcome = newGame.board.outcome()
newGame.game.headers['Result'] = outcome.result()
print(newGame.game.headers)
chess_model.quitEngine()

#---------------------