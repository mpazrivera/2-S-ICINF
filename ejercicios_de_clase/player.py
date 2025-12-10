import pygame as pg
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED

class Player(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		#atrivutos de la nave
		self.image = pg.Surface((50,50),pg.SRCALPHA|)
		self.rect = self.image.get_rect()
		self.rect.centerx = SCREEN_WIDTH //2 #APARECERA AL MEDIO DE LA PANTALLA
		self.rect.bottom = SCREEN_HEIGHT -10
	
		#dibujar el triangulo
		pg.draw.polygon(self.image, (0,0,250), [(25,0),(0,50),(50,50)])

	def update(self):
		keys = pg.key.get_pressed()

		#teclas ocupadas
		if keys[pg.K_LEFT]:
			self.rect.x -= PLAYER_SPEED
		if keys[pg.K_RIGHT]:
			self.rect.x += PLAYER_SPEED

		#mantener la nave dentrro de los limites de la pantalla
		if self.rect.left = 0