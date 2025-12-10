import pygame
import random
from settings import SCREEN_WIDTH, METEOR_SPEED, SCREEN_HEIGHT, RED

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        pygame.draw.circle(self.image, RED, (15, 15), 15)  # Dibuja un círculo rojo
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += METEOR_SPEED
        # Si el meteorito sale de la pantalla, se eliminan
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
