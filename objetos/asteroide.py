import pygame
import random
import os

from configuracion import *

ruta_imagenes = os.getcwd() + "\\recursos\\imagenes\\"

imagen1 = pygame.image.load(ruta_imagenes + "asteroide-01.png").convert_alpha()
imagen2 = pygame.image.load(ruta_imagenes + "asteroide-02.png").convert_alpha()
imagen3 = pygame.image.load(ruta_imagenes + "asteroide-03.png").convert_alpha()
imagen4 = pygame.image.load(ruta_imagenes + "asteroide4.png").convert_alpha()

imagen_explosion = pygame.image.load(ruta_imagenes + "explosion.png").convert_alpha()
imagenes = [imagen1, imagen2, imagen3]

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, juego):
        super().__init__()

        self.PANTALLA = juego.PANTALLA

        self.imagen_limpia = imagenes[random.randint(0, len(imagenes) - 1)]
        self.imagen_explosion = imagen_explosion

        self.ancho = self.imagen_limpia.get_width()
        self.alto = self.imagen_limpia.get_height()

        self.angulo_rotacion = random.randint(0, 360)
        self.direccion_rotacion = random.randint(1, 2)
        self.velocidad_rotacion = random.randint(1, 5)

        if juego.nivel == 1:
            self.velocidad = random.randint(4, 5)
            self.escala = random.randint(1, 2)
        if juego.nivel == 2:
            self.velocidad = random.randint(5, 6)
            self.escala = random.randint(1, 2)
        if juego.nivel >= 3:
            self.velocidad = random.randint(5, 7)
            self.escala = random.randint(1, 3)

        if self.escala == 1:
            self.escala = 0.7
            self.radius = self.ancho / 3
        elif self.escala == 2:
            self.escala = 0.9
            self.radius = self.ancho / 2 - 10
        elif self.escala == 3:
            self.escala = 1.1
            self.radius = self.ancho - 50

        posx = random.randint(self.ancho, ANCHO - self.ancho)
        posy = self.alto * -1

        self.image = pygame.transform.rotozoom(self.imagen_limpia, self.angulo_rotacion, self.escala)
        self.rect = self.image.get_rect()

        self.rect.center = (posx, posy)

        self.estado = ""
        self.tiempo_explosion = 60

    def trayectoria(self):
        self.rect.y += self.velocidad

        if self.rect.y > ALTO + self.alto:
            self.kill("fuera de pantalla")

    def rotar(self):
        center_viejo = self.rect.center

        if self.direccion_rotacion == 1:
            self.angulo_rotacion += self.velocidad_rotacion
        else:
            self.angulo_rotacion -= self.velocidad_rotacion

        self.image = pygame.transform.rotozoom(self.imagen_limpia, self.angulo_rotacion, self.escala)
        self.rect = self.image.get_rect()

        # pygame.draw.circle(self.image, (255, 255, 255), self.rect.center, self.radius)
        self.rect.center = center_viejo

    def kill(self, tipo = ""):
        if tipo == "destruir":
            return super().kill()

        self.destruir()

    def destruir(self):
        self.velocidad = 0
        self.radius = 0
        self.estado = "explosion"

    def animacion_destruccion(self):
        self.tiempo_explosion -= 1

        if self.tiempo_explosion < 60:
            self.image = pygame.transform.rotozoom(self.imagen_explosion, self.angulo_rotacion, self.escala)
            self.rect = self.image.get_rect(center = self.rect.center)

        if self.tiempo_explosion < 40:
            self.image = pygame.transform.rotozoom(self.imagen_explosion, self.angulo_rotacion, self.escala * 0.8)
            self.rect = self.image.get_rect(center = self.rect.center)

        if self.tiempo_explosion < 20:
            self.image = pygame.transform.rotozoom(self.imagen_explosion, self.angulo_rotacion, self.escala * 0.6)
            self.rect = self.image.get_rect(center = self.rect.center)

        if self.tiempo_explosion <= 0:
            self.kill("destruir")

    def actualizar(self):
        if self.estado == "explosion":
            self.animacion_destruccion()
            return
        
        self.trayectoria()
        self.rotar()