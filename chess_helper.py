import re

#---------------------

def getFirstMove(file_name):

    moveRegex = re.compile(r'[a-h][1-8][a-h][1-8]')

    with open(file_name, 'r') as f:
        moves_in = f.read().strip('\n').strip().lower()

    while not (len(moves_in) == 4 and re.match(moveRegex, moves_in)):
        with open(file_name, 'r') as f:
            moves_in = f.read().strip('\n').strip().lower()
    
    return moves_in

#---------------------

def getMove(lastmove, file_name):

    moves_in = lastmove
    moveRegex = re.compile(r'[a-h][1-8][a-h][1-8]')

    while moves_in in [lastmove, ''] or not (len(moves_in) == 4 and re.match(moveRegex, moves_in)):
        with open(file_name, 'r') as f:
            moves_in = f.read().strip('\n').strip().lower()
        
    return moves_in

#---------------------