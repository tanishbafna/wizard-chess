import chess
import chess.pgn
import chess.svg
import chess.engine

import re
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from cairosvg import svg2png

#---------------------

STOCKFISH_PATH = '/usr/local/Cellar/stockfish/14/bin/stockfish'
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

starting_positions = {
    'default': 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
}

#---------------------

class chessGame():

    def __init__(self, file_name, img_name='current_board.png', position='default', White='White', Black='Black', clock='10+0'):
        
        self.img_name = img_name
        self.file_name = file_name
        
        self.board = chess.Board(fen=starting_positions[position])
        self.game = chess.pgn.Game()
        self.game.setup(self.board)

        self.game.headers['White'] = White
        self.game.headers['Black'] = Black
        self.game.headers['Event'] = f'{White} v. {Black}'
        self.game.headers['Date'] = datetime.today().strftime('%Y.%m.%d')

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
            
            info = engine.analyse(self.board, chess.engine.Limit(time=0.2))

            self.node.set_eval(score=info["score"])
            try:
                self.node.comment += f" [%prob {2*self.node.eval().white().wdl(model='lichess').expectation() - 1}]"
            except AttributeError:
                pass
            
            self.drawBoard()

            return True
        
        else:
            return False
    
    def getProb(self, node) -> float:
        prob_regex = re.compile(r'\[%prob (.*?)]')
        match = prob_regex.search(node.comment)
        return float(match.group(1))
    
    # def undoMove()
          
    def drawBoard(self, lastmove=True, size=900) -> None:

        if lastmove:
            svg_board = chess.svg.board(self.board, size=size, lastmove=self.node.move)
        else:
            svg_board = chess.svg.board(self.board, size=size)
        
        svg2png(bytestring=svg_board, write_to=self.img_name)
    
    def saveGame(self, save_dir) -> None:

        save_name = f'{self.game.headers["Event"]} [{self.game.headers["Date"]}]'
        pgn_file = open(f'{save_dir}/{save_name}', 'w', encoding='utf-8')
        self.game.accept(chess.pgn.FileExporter(pgn_file))
    
    def postAnalysis(self):
        
        probArr = [self.getProb(node) for node in self.game.mainline() if node.eval()]
        fig, ax = plt.subplots()
        fig.set_size_inches(15, 15 / 3)
        g = sns.lineplot(data=probArr, ax = ax, color = 'blue');   
        g.axhline(y=0.00, color='r', linestyle='-');
        plt.ylim(-1.2, 1.2);
        sns.despine()
        plt.show()

        return probArr

#---------------------

def quitEngine():

    global engine
    engine.quit()
    return True

#---------------------
