from time import sleep

moves = ['e2e4', 'f7f5', 'a2a3', 'g7g5', 'd1h5']

for move in moves:
    for i in range(3):
        with open('input_moves.txt', 'w') as f:
            f.write(move)
            sleep(1)