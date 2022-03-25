import pygame
import os 

from configuracion import *

ruta_imagenes_nave = os.getcwd() + "\\recursos\\imagenes\\nave\\"

imagen1 = pygame.image.load(ruta_imagenes_nave + "nave_01.png").convert_alpha()
imagen2 = pygame.image.load(ruta_imagenes_nave + "nave_02.png").convert_alpha()
imagen3 = pygame.image.load(ruta_imagenes_nave + "nave_03.png").convert_alpha()
imagen4 = pygame.image.load(ruta_imagenes_nave + "nave_04.png").convert_alpha()
imagen5 = pygame.image.load(ruta_imagenes_nave + "nave_05.png").convert_alpha()
imagen6 = pygame.image.load(ruta_imagenes_nave + "nave_06.png").convert_alpha()


frames = [imagen1, imagen2, imagen3, imagen4, imagen5, imagen6]

class Nave(pygame.sprite.Sprite):
    def __init__(self, PANTALLA) -> None:
        super().__init__()
        self.PANTALLA = PANTALLA

        self.image = imagen1
        self.rect = self.image.get_rect()

        self.ancho = self.image.get_width()
        self.alto = self.image.get_height()

        self.radius = self.ancho / 3
        # pygame.draw.circle(self.image, (255, 255, 255), self.rect.center, self.radius)

        self.x = ANCHO / 2
        self.y = ALTO - 20

        self.velocidad = 10
        self.estado = "quieto"
        self.direccion = ""

        self.nave = pygame.sprite.GroupSingle()
        self.nave.add(self)

        self.contador_animacion = 60

    def pintar(self):
        self.nave.draw(self.PANTALLA)

    def cambiar_direccion(self, direccion):
        self.direccion = direccion

    def mover(self):
        if self.direccion == "arriba":
            self.y -= self.velocidad
        elif self.direccion == "abajo":
            self.y += self.velocidad
        elif self.direccion == "izquierda":
            self.x -= self.velocidad
        elif self.direccion == "derecha":
            self.x += self.velocidad

        if self.x < self.ancho / 2:
            self.x = self.ancho / 2
        elif self.x > ANCHO - self.ancho / 2:
            self.x = ANCHO - self.ancho / 2
        elif self.y < self.alto / 2:
            self.y = self.alto / 2
        elif self.y > ALTO - self.alto / 2:
            self.y = ALTO - self.alto / 2

        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.cambiar_estado()

    def cambiar_estado(self):
        if self.direccion == "":
            self.estado = "quieto"
        else:
            self.estado = "moviendose"

    def animar(self):
        if self.contador_animacion <= 60:
            self.image = frames[0]
        if self.contador_animacion <= 55:
            self.image = frames[5]
        if self.contador_animacion <= 50:
            self.image = frames[1]
        if self.contador_animacion <= 45:
            self.image = frames[4]
        if self.contador_animacion <= 40:
            self.image = frames[2]
        if self.contador_animacion <= 35:
            self.image = frames[3]
        if self.contador_animacion <= 30:
            self.image = frames[3]
        if self.contador_animacion <= 25:
            self.image = frames[2]
        if self.contador_animacion <= 20:
            self.image = frames[4]
        if self.contador_animacion <= 15:
            self.image = frames[1]
        if self.contador_animacion <= 10:
            self.image = frames[5]
        if self.contador_animacion <= 5:
            self.image = frames[0]

        if self.contador_animacion <= 0:
            self.contador_animacion = 60
        self.contador_animacion -= 1

    def actualizar(self):
        self.animar()
        self.mover()
        self.pintar()