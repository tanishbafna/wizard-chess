from time import sleep

moves = {1:['d2d4', 'g8f6'], 2:['c2c4', 'e7e5'], 3:['d4e5', 'f6g4'], 4:['c1f4', 'b8c6'], 5:['g1f3', 'f8b4'], 6:['b1d2', 'd8e7'], 7:['a2a3', 'g4e5'], 8:['a3b4', 'e5d3']} 
print('')

for n, moveSet in moves.items():

    for move in moveSet:
        print(f'{n}. {move}')
        
        for i in range(3):
            with open('input_moves.txt', 'w') as f:
                f.write(move)
            sleep(2)
    
    print('')