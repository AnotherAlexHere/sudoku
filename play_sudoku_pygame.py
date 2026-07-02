#Following tutorial from the following: https://www.youtube.com/watch?v=Xw0xxvyxFuE

import sys, pygame as pygame

pygame.init()
screen_size = 750, 750
screen = pygame.display.set_mode(screen_size)

def draw_background():
    """
    Creates the background of the sudoku.
    """

    screen.fill(pygame.Color("white"))
    pygame.draw.rect(screen, pygame.Color("black"), pygame.Rect(15,15, 720, 720), 10)
    i = 1
    while (i * 80) < 720:
        if i % 3  > 0:
            line_width = 5
        else:
            line_width = 10
        
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2((i * 80)+ 15, 15), pygame.Vector2((i * 80) + 15, 735), line_width)
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2(15, (i * 80)+ 15), pygame.Vector2(735, (i * 80)+ 15), line_width)

        i += 1

def game_loop():
    """
    Refreshes the game.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    draw_background()
    pygame.display.flip()


while True:
    game_loop()
