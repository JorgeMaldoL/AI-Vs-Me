import pygame
from pygame.locals import *
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Robot Jump")
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load('game/assets/environment/background_wall.png').convert()

    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    screen.blit(background, (0,0))
    pygame.display.flip()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.blit(background, (0,0))
        pygame.display.flip()

    
if __name__ == "__main__":
    main()