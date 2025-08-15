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
        pygame.draw.circle(screen, 'red', player_position, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player_position.y -= 300 * dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player_position.y += 300 * dt
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_position.x -= 300 * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_position.x += 300 * dt

        pygame.display.flip()

        dt = clock.tick(FPS)/1000

    pygame.quit()
    
if __name__ == "__main__":
    main()