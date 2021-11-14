import pygame
import time

#---------------------

pygame.init()
pygame.font.init()
pygame.display.set_caption('wizard-chess')

X = 1440
Y = 800
display_surface = pygame.display.set_mode((X, Y ))

#---------------------

bg = (64, 77, 99)
offset_x = 30
offset_y = 20
font1 = pygame.font.SysFont('Cambria', 24)
font2 = pygame.font.SysFont('Cambria', 26)

#---------------------

board = pygame.image.load('img/current_board.png')
probability = pygame.image.load('img/current_probability.png')
white_profile = pygame.image.load('img/white.png')
black_profile = pygame.image.load('img/black.png')

#---------------------

white_player = font1.render('Tanish', True, (255, 255, 255))
black_player = font1.render('Sarvag', True, (255, 255, 255))

white_timeFloat = 599.0
black_timeFloat = 599.0

#---------------------

while True:

    try:
        board = pygame.image.load('img/current_board.png')
        probability = pygame.image.load('img/current_probability.png')
    except:
        continue

    #---------------------

    white_profile = pygame.image.load('img/white.png')
    black_profile = pygame.image.load('img/black.png')

    #---------------------

    display_surface.fill(bg)

    display_surface.blit(black_profile, (0+offset_x, 0+offset_y))
    display_surface.blit(white_profile, (0+offset_x, 720+offset_y))

    display_surface.blit(board, (0+offset_x, 60+offset_y))
    display_surface.blit(probability, (640+offset_x, 60+offset_y))

    display_surface.blit(black_player, (60+offset_x, 10+offset_y))
    display_surface.blit(white_player, (60+offset_x, 730+offset_y))

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
    time.sleep(1)