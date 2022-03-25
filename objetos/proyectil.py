import pygame
import os

from configuracion import *

ruta_imagenes = os.getcwd() + "\\recursos\\imagenes\\proyectil.png"
imagen_proyectil = pygame.image.load(ruta_imagenes).convert_alpha()

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, PANTALLA, posx, posy):
        super().__init__()

        self.PANTALLA = PANTALLA
        self.velocidad = 20
        
        self.image = imagen_proyectil

        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)

    def trayectoria(self):
        self.rect.y -= self.velocidad

        if self.rect.x > ANCHO or self.rect.x < 0 or self.rect.y > ALTO or self.rect.y < 0:
            self.eliminar()

    def eliminar(self):
        self.kill()