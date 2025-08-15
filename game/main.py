import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Robot Jump")
    clock = pygame.time.Clock()
    running = True
    dt = 0 

    player_position = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("blue")

        pygame.display.flip()

        dt = clock.tick(FPS)/1000

    pygame.quit()
    
if __name__ == "__main__":
    main()