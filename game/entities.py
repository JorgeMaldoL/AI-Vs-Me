import pygame

def load_png(name):
    """Load image and return image object and rect."""
    image = pygame.image.load(name)
    image = image.convert_alpha()
    return image, image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('assets/characters/bot.png')