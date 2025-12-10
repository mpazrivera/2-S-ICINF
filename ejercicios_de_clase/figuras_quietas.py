import pygame as pg

pg.init()

#color de fondo 
blackground = (0,0,0)#negro

#seteo de la ventana
window = pg.display.set_mode((800,600))
pg.display.set_caption("Conceptos básicos") #titulo de la ventana


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    window.fill(blackground)

    #dibujando figuras
    pg.draw.circle(window, (131, 218, 222), (400, 300), 60, width=0)
    pg.draw.rect(window, (196, 138, 230), (100, 200, 200, 100), width=0)
    pg.draw.rect(window, (255, 163, 230), (200, 400, 100, 100), width=0)
    pg.draw.line(window, (255, 163, 163), (600, 500), (600,100), width=3)

    pg.display.update()

pg.quit()