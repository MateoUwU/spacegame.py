import pygame
import sys
import random
import os

from configuracion import *

pygame.init()

PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego del Espacio")

ruta_imagen_fondo = os.path.join(os.getcwd(), "recursos", "imagenes", "fondo.png")
imagen_fondo = pygame.image.load(ruta_imagen_fondo).convert_alpha()

from extras import *
from sonidos import Sonidos

from menu import *
from menu_opciones import *
from actualizar import *
from menu_pausa import *
from menu_derrota import *

from objetos.nave import Nave
from objetos.proyectil import Proyectil
from objetos.asteroide import Asteroide

class Juego:
    def __init__(self):
        self.PANTALLA = PANTALLA
        self.estado = "menu"

        self.imagen_fondo = imagen_fondo

        self.sonidos = Sonidos()

        self.EJECUTAR = True
        self.pausa = False
        self.finalizado = False

        self.reloj = pygame.time.Clock()

        self.nave = Nave(self.PANTALLA)

        self.proyectiles = pygame.sprite.Group()
        self.asteroides = pygame.sprite.Group()

        self.cooldown_puntos = 120
        self.puntos = 0
        self.cooldown_nivel = 120
        self.nivel = 1
        self.transicion_nivel = False

        self.control_w = False
        self.control_s = False
        self.control_a = False
        self.control_d = False

        self.enfriar_disparo = False
        self.cooldown_disparo = 40

        self.mouse_encima = False

    def iniciar(self):
        while self.EJECUTAR:
            if self.estado == "menu":
                menu_principal(self)

            if self.estado == "opciones":
                menu_opciones(self)

            if self.estado == "juego":
                actualizar(self)

            if self.estado == "pausa":
                menu_pausa(self)

            if self.estado == "derrota":
                menu_derrota(self)

            self.reloj.tick(FPS)

    def cerrar(self):
        self.EJECUTAR = False
        pygame.quit()
        sys.exit()

    def mostrar_puntos(self):
        mostrar_texto(self.PANTALLA, "Puntos: " + str(self.puntos), ANCHO - 80, 30, 30, "Rajdhani-SemiBold", (255, 255, 255))

    def mostrar_nivel(self):
        if self.nivel == 1:
            color = COLOR_BLANCO
        if self.nivel == 2:
            color = COLOR_AMARILLO
        if self.nivel >= 3:
            color = COLOR_ROJO

        mostrar_texto(self.PANTALLA, "Nivel: " + str(self.nivel), 60, 30, 30, "Rajdhani-SemiBold", color)

    def dibujar_linea(self, x1, y1, x2, y2, color):
        pygame.draw.line(self.PANTALLA, color, (x1, y1), (x2, y2), 2)

    def pintar(self):
        self.PANTALLA.blit(self.imagen_fondo, (0, 0))
        self.dibujar_linea(ANCHO + 2, 0, ANCHO + 2, ALTO + 3, COLOR_LINEA)
        self.dibujar_linea(0, ALTO + 2, ANCHO + 2, ALTO + 2, COLOR_LINEA)

    def reiniciar(self):
        self.nave = Nave(self.PANTALLA)
        self.proyectiles = pygame.sprite.Group()
        self.asteroides = pygame.sprite.Group()

        self.puntos = 0
        self.nivel = 1
        self.enfriar_disparo = False

        self.sonidos.cargar_musica(f"tema{self.nivel}", 0.1)

    def disparar(self):
        if self.enfriar_disparo == False:
            proyectil = Proyectil(self.PANTALLA, self.nave.rect.centerx, self.nave.rect.centery)
            self.proyectiles.add(proyectil)
            self.sonidos.reproducir("disparo")
            self.enfriar_disparo = True

    def corregir_direccion(self):
        if self.control_w:
            self.nave.cambiar_direccion("arriba")
        elif self.control_s:
            self.nave.cambiar_direccion("abajo")
        elif self.control_a:
            self.nave.cambiar_direccion("izquierda")
        elif self.control_d:
            self.nave.cambiar_direccion("derecha")
        else:
            self.nave.cambiar_direccion("")

    def actualizar_proyectiles(self):
        for proyectil in self.proyectiles:
            proyectil.trayectoria()

            if pygame.sprite.spritecollide(proyectil, self.asteroides, True, pygame.sprite.collide_circle):
                proyectil.eliminar()
                self.puntos += 1

        self.proyectiles.draw(self.PANTALLA)

    def disparo_cooldown(self):
            if self.enfriar_disparo == True:
                self.cooldown_disparo -= 1
                mostrar_texto(self.PANTALLA, "Cargando Láser: " + str(self.cooldown_disparo), ANCHO - 130, ALTO - 25, 30, "Rajdhani-SemiBold", COLOR_ROJO)
                if self.cooldown_disparo == 0:
                    self.enfriar_disparo = False
                    self.cooldown_disparo = 40
            else:
                mostrar_texto(self.PANTALLA, "Láser Cargado", ANCHO - 100, ALTO - 25, 30, "Rajdhani-SemiBold", COLOR_VERDE)

    def actualizar_nave(self):
        self.nave.actualizar()

        if pygame.sprite.spritecollide(self.nave, self.asteroides, True, pygame.sprite.collide_circle):
            self.sonidos.reproducir("crash")
            self.estado = "derrota"
            self.reiniciar()

    def actualizar_asteroides(self):
        if random.randint(1, 20) == 1 and len(self.asteroides) <= 10 * self.nivel:
            nuevo_asteroide = Asteroide(self)
            self.asteroides.add(nuevo_asteroide)

        for asteroide in self.asteroides:
            asteroide.actualizar()

        self.asteroides.draw(self.PANTALLA)