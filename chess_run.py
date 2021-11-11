import os
import time
from cairosvg import svg2png

import chess_model 
import chess_helper

#---------------------

file_name = 'input_moves.txt'
img_name = 'current_board.png'
save_dir = os.getcwd()

#---------------------

newGame = chess_model.chessGame(file_name, img_name)

with open(file_name, 'w') as f:
    f.write('')

print('Game has started!')
newGame.drawStartProbability()

startClock = time.time()
while not newGame.move(chess_helper.getFirstMove(file_name), int(time.time() - startClock)):
    pass

while not newGame.board.outcome():
    newGame.drawProbability()
    startClock = time.time()
    while not newGame.move(chess_helper.getMove(newGame.node.move, file_name), int(time.time() - startClock)):
        pass

outcome = newGame.board.outcome()
newGame.game.headers['Result'] = outcome.result()
print(newGame.game.headers)
newGame.saveGame(save_dir)
newGame.postAnalysis()
chess_model.quitEngine()

#---------------------