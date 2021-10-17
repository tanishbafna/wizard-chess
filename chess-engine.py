import chess
import chess.svg
import chess.engine
from PIL import Image
from cairosvg import svg2png
from stockfish import Stockfish

#---------------------

STOCKFISH_PATH = '/usr/local/Cellar/stockfish/14/bin/stockfish'
stockfish = Stockfish(STOCKFISH_PATH)
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

board = chess.Board()

#---------------------

def drawBoard(board, lastmove, size=900):

    svg_board = chess.svg.board(board, size=size, lastmove=lastmove)
    svg2png(bytestring=svg_board,write_to='current_board.png')

#---------------------

move_num = 0

while board.outcome() is None:

    first_attempt = True
    uci_move = None

    while first_attempt or not board.is_legal(uci_move):

        first_attempt = False

        if move_num % 2 == 0:
            move = input('White Move: ')
        else:
            move = input('Black Move: ')

        uci_move = chess.Move.from_uci(move)

    board.push(uci_move)
    move_num += 1

    drawBoard(board, uci_move)
    Image.open('current_board.png').show()

print('Game Over')