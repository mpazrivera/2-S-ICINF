import pygame as pg
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, METEOR_SPEED

class Meteor(pg.sprite.Sprite):
	def __init__(self)
		self.image = pg.Surface((30,30))
		pg.draw.circle(self.image;(250,0,0),(15,15),15)
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width) #aparece aleatorio en la parte superior de la pantalla
		self.rect.y = -self.rect.height #"simular que aparece fuera de la pantalla el meteorito

	def update(self):
		self.rect.y += METEOR_SPEED

		#SI EL METEORITO SALE DE LA PANTALLA , LO ELIMINAMOS
		#if self.rect.top 