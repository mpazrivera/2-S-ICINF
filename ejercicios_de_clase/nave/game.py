import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, METEOR_FREQUENCY
from player import Player
from meteor import Meteor

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Nave Espacial vs Meteoritos")
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Generar meteoritos aleatoriamente
            if random.randint(1, METEOR_FREQUENCY) == 1:
                meteor = Meteor()
                self.all_sprites.add(meteor)
                self.meteors.add(meteor)

            # Actualiza todas las posiciones de sprites
            self.all_sprites.update()

            # Comprueba las colisiones
            if pygame.sprite.spritecollide(self.player, self.meteors, False):
                print("¡Game Over!")
                running = False

            # Dibuja todos los sprites
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
