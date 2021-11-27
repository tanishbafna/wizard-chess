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