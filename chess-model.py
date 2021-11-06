import chess
import chess.pgn
import chess.svg
import chess.engine

import sys
import select
import time
from cairosvg import svg2png

#---------------------

STOCKFISH_PATH = '/usr/local/Cellar/stockfish/14/bin/stockfish'
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

starting_positions = {
    'default': 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
}

img_name = 'current_board.png'

#---------------------

class chessGame():

    def __init__(self, position='default', White='White', Black='Black', clock='10+0'):
        
        self.board = chess.Board(fen=starting_positions[position])
        self.game = chess.pgn.Game()
        self.game.setup(self.board)

        self.game.headers['White'] = White
        self.game.headers['Black'] = Black
        self.game.headers['Event'] = f'{White} v. {Black}'

        self.base_time, self.increament = [int(x) for x in clock.split('+')]
        self.game.set_clock((self.base_time*60) + self.increament)
        self.game.set_clock((self.base_time*60) + self.increament)

        self.node = self.game
        self.drawBoard(lastmove=False)
    
    def move(self, moveIn, timePassed) -> bool:

        uciMove = chess.Move.from_uci(moveIn)

        if self.board.is_legal(uciMove):
        
            self.node = self.node.add_main_variation(uciMove)
            updateTime = (self.node.parent.parent.clock() if self.node.parent.parent else self.node.parent.clock()) - timePassed
            self.node.set_clock(updateTime)
            self.board.push(uciMove)
            
            info = engine.analyse(self.board, chess.engine.Limit(time=0.15))

            self.node.set_eval(score=info["score"])
            # print(self.node.eval().white().wdl(model='lichess').expectation())
            self.drawBoard()
        
        else:
            return False
    
    # def undoMove()
          
    def drawBoard(self, lastmove=True, size=900) -> None:

        if lastmove:
            svg_board = chess.svg.board(self.board, size=size, lastmove=self.node.move)
        else:
            svg_board = chess.svg.board(self.board, size=size)
        
        svg2png(bytestring=svg_board, write_to=img_name)


newGame = chessGame()
timeLeft = newGame.game.clock()

while time.time() + timeLeft >= time.time():

    startClock = time.time()
    i, o, e = select.select([sys.stdin], [], [], timeLeft)
    while not newGame.move(i, int(time.time() - startClock)):
        pass

engine.quit()