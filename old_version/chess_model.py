import chess
import chess.pgn
import chess.svg
import chess.engine

import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
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

            self.node.set_eval(score=info['score'])
            try:
                self.node.comment += f" [%prob(n) {self.node.eval().white().wdl(model='lichess').expectation()}]"
                self.node.comment += f" [%prob(c) {2*self.node.eval().white().wdl(model='lichess').expectation() - 1}]"
            except AttributeError:
                pass
            
            self.drawBoard()

            return True
        
        else:
            return False
    
    def getProb_c(self, node) -> float:
        prob_regex = re.compile(r'\[%prob\(c\) (.*?)]')
        match = prob_regex.search(node.comment)
        return float(match.group(1))
    
    def getProb_n(self, node) -> float:
        prob_regex = re.compile(r'\[%prob\(n\) (.*?)]')
        match = prob_regex.search(node.comment)
        return float(match.group(1))
    
    # def undoMove()
          
    def drawBoard(self, lastmove=True, size=640) -> None:

        if lastmove:
            svg_board = chess.svg.board(self.board, size=size, lastmove=self.node.move)
        else:
            svg_board = chess.svg.board(self.board, size=size)
        
        svg2png(bytestring=svg_board, write_to='img/'+self.img_name)
    
    def drawProbability(self, fresh=False) -> None:

        if not fresh:
            prob = self.getProb_n(self.node)
        else:
            prob = 0.50

        df = pd.DataFrame(columns=['color','probability'], data=[['white', prob], ['black', 1 - prob]])

        df = df.set_index('color').reindex(df.set_index('color').sum().sort_values().index, axis=1)
        ax = df.T.plot(kind='bar', stacked=True, colormap=ListedColormap(sns.color_palette('Greys', 10)), figsize=(1.5,8.3), legend = None)
        
        plt.xticks([])
        plt.yticks([])
        plt.box(False)
        plt.margins(0,0)
        plt.axis('off')

        for i,c in enumerate(ax.containers):
            labels = ['%.2f' % v.get_height() if v.get_height() > 0 else '' for v in c]
            if i == 0:
                labels[0] = '+'+labels[0]
                ax.bar_label(c, labels=labels, label_type='center')
            else:
                labels[0] = '-'+labels[0]
                ax.bar_label(c, labels=labels, label_type='center', color='w')

        plt.savefig('img/'+'current_probability.png', bbox_inches='tight', pad_inches=0, transparent=True)
    
    def saveGame(self, save_dir) -> None:

        save_name = f"{self.game.headers['Event']} [{self.game.headers['Date']}]"
        pgn_file = open(f'{save_dir}/{save_name}', 'w', encoding='utf-8')
        self.game.accept(chess.pgn.FileExporter(pgn_file))
    
    def postAnalysis(self):
        
        probArr = [[i+1, self.getProb_c(node)] for i,node in enumerate(self.game.mainline()) if node.eval()]
        df = pd.DataFrame(columns=['move','probability'], data=[[0,0.00]] + probArr)

        sns.set(style='darkgrid')
        sns.relplot(data=df, x='move', y='probability', kind='line', height=5, aspect=2, color='black', markers="o").set(title='Post-Game Analysis')
        sns.despine()
        
        plt.axhline(y=0.00, color='r', linestyle='-')
        plt.ylim(-1.2, 1.2)
        plt.xticks([])
        #plt.show()

        plt.savefig('img/'+'post_analysis.png')

        return None

#---------------------

def quitEngine():

    global engine
    engine.quit()
    return True

#---------------------
