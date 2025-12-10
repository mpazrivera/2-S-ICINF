import pygame as pg 

pg.init()

#color de fondo 
blackground = (255,255,255)#blanco

#seteo de la ventana
window = pg.display.set_mode((800,600))
pg.display.set_caption("Conceptos básicos") #titulo de la ventana

velocidad = 0.25
x, y = 400, 300

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    window.fill(blackground)

    #dibujando figuras
    pg.draw.circle(window, (131, 218, 222), (x, y), 60, width=0) 

    teclas = pg.key.get_pressed()
    if teclas[pg.K_UP]:
        y -= velocidad
    
    if teclas[pg.K_DOWN]:
        y += velocidad
    
    if teclas[pg.K_LEFT]:
        x -= velocidad

    if teclas[pg.K_RIGHT]:
        x += velocidad


    pg.display.update()
pg.quit()

clase 


#a llamamos a la biblioteca
import pygame as pg

class Circulo:
    def __init__ (self, x, y, radio, color = (255,255,255), velocidad = 1):
        self.x =x
        self.y = y
        self.radio = radio
        self.color = color 
        self.velocidad = velocidad

    #metodos
    def mover (self):
        teclas = teclas.pg.key.get_pressed()
        if teclas[pg.K_UP]:
            y -= self.velocidad
    
        if teclas[pg.K_DOWN]:
            y += self.velocidad
    
        if teclas[pg.K_LEFT]:
            x -= self.velocidad

        if teclas[pg.K_RIGHT]:
            x += self.velocidad  
        
    def dibujar (self, pantalla):
        pg.draw.circle