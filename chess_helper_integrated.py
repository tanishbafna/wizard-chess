import re

#---------------------

def getMove_integrated(file_name, lastmove):

    moveRegex = re.compile(r'[a-h][1-8][a-h][1-8]')

    with open(file_name, 'r') as f:
        moves_in = f.read().strip().lower()
    
    if moves_in in lastmove or not (len(moves_in) == 4 and re.match(moveRegex, moves_in)):
        return False
    else:
        return moves_in

#---------------------

pieces_mapping = {
    "b":"b_bishop",
    "k":"b_king",
    "n":"b_knight",
    "p":"b_pawn",
    "q":"b_queen",
    "r":"b_rook",
    "B":"w_bishop",
    "K":"w_king",
    "N":"w_knight",
    "P":"w_pawn",
    "Q":"w_queen",
    "R":"w_rook"
}

#---------------------