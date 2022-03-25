import pygame
import os

ruta_imagen = os.getcwd() + "\\recursos\\imagenes\\mira.png"
imagen_mira = pygame.image.load(ruta_imagen).convert_alpha()

class Mira(pygame.sprite.Sprite):
    def __init__(self, PANTALLA):
        super().__init__()
        self.PANTALLA = PANTALLA

        self.image = imagen_mira
        self.rect = self.image.get_rect()

        self.grupo = pygame.sprite.Group()
        self.grupo.add(self)

    def pintar(self):
        self.grupo.draw(self.PANTALLA)

    def mover(self):
        self.rect.center = pygame.mouse.get_pos()

    def actualizar(self):
        self.mover()
        self.pintar()
    
    def update(self) -> None:
        self.actualizar()