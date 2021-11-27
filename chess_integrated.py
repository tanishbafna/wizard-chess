
import pygame
from cairosvg import svg2png

import os
import time

import chess_model_integrated as chess_model
import chess_helper_integrated as chess_helper

#---------------------

# Running Variables
file_name = 'input_moves.txt'
img_name = 'current_board.png'
save_dir = os.getcwd()

#---------------------

# Pygame Setup
pygame.init()
pygame.font.init()
pygame.display.set_caption('wizard-chess')

X = 1440
Y = 800
display_surface = pygame.display.set_mode((X, Y ))

#---------------------

# Pygame Variables
bg = (64, 77, 99)
offset_x = 30
offset_y = 20
font1 = pygame.font.SysFont('Cambria', 24)
font2 = pygame.font.SysFont('Cambria', 26)
font3 = pygame.font.SysFont('Cambria', 18)

board_img = 'img/' + img_name
prob_img = 'img/' + 'current_probability.png'
white_img = 'img/' + 'white.png'
black_img = 'img/' + 'black.png'

#---------------------

# Setup the Game
white_name = 'Tanish'
black_name = 'Sarvag'
clock_input = '10+0'
newGame = chess_model.chessGame(file_name, img_name, White=white_name, Black=black_name, clock=clock_input)

white_player = font1.render(white_name, True, (255, 255, 255))
black_player = font1.render(black_name, True, (255, 255, 255))

white_timeFloat = newGame.time_control
black_timeFloat = newGame.time_control

print('Game has started!')
startClock = time.time()
gameplay_arr = []
gameOver = 0
lastmove = ''

#---------------------

while not gameOver == 2:

    board = pygame.image.load(board_img)
    probability = pygame.image.load(prob_img)
    white_profile = pygame.image.load(white_img)
    black_profile = pygame.image.load(black_img)

    #---------------------

    display_surface.fill(bg)

    display_surface.blit(black_profile, (0+offset_x, 0+offset_y))
    display_surface.blit(white_profile, (0+offset_x, 720+offset_y))

    display_surface.blit(board, (0+offset_x, 60+offset_y))
    display_surface.blit(probability, (640+offset_x, 60+offset_y))

    display_surface.blit(black_player, (60+offset_x, 10+offset_y))
    display_surface.blit(white_player, (60+offset_x, 730+offset_y))

    for i,x in enumerate(gameplay_arr):
        display_surface.blit(font3.render(x, True, (255,255,255)), (800+offset_x, 60+offset_y+(25*i)))

    #---------------------

    white_timeStr = time.strftime(' %M:%S ', time.gmtime(int(white_timeFloat)))
    black_timeStr = time.strftime(' %M:%S ', time.gmtime(int(black_timeFloat)))

    white_timeLeft = font2.render(white_timeStr, True, (255, 255, 255), (214, 43, 60))
    black_timeLeft = font2.render(black_timeStr, True, (255, 255, 255), (214, 43, 60))

    display_surface.blit(black_timeLeft, (565+offset_x, 8+offset_y))
    display_surface.blit(white_timeLeft, (565+offset_x, 728+offset_y))

    #---------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update() 

    #---------------------

    if gameOver == 0 and not newGame.board.outcome() and not white_timeFloat == 0 and not black_timeFloat == 0:

        movePlayed = chess_helper.getMove_integrated(file_name, lastmove)

        if not movePlayed:
            if newGame.board.turn:
                white_timeFloat -= 1
            else:
                black_timeFloat -= 1
            time.sleep(1)
        else:
            newGame.move(movePlayed, int(time.time() - startClock))
            startClock = time.time()
            lastmove = movePlayed
        
        gameplay_arr = newGame.gamePlay()
    
    if newGame.board.outcome() or white_timeFloat == 0 or black_timeFloat == 0:
        gameOver += 1

    if gameOver == 2:
        input()

#---------------------

if newGame.board.outcome():
    outcome = newGame.board.outcome()
    newGame.game.headers['Result'] = outcome.result()
elif white_timeFloat == 0:
    newGame.game.headers['Result'] = '0-1'
elif black_timeFloat == 0:
    newGame.game.headers['Result'] = '1-0'

print(newGame.game.headers)
newGame.saveGame(save_dir)
newGame.postAnalysis()
chess_model.quitEngine()

#---------------------