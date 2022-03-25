COLOR_NEGRO = (0, 0, 0)
COLOR_ROJO = (255, 0, 0)
COLOR_BLANCO = (255, 255, 255)
COLOR_VERDE = (0, 255, 0)
COLOR_AMARILLO = (255, 255, 0)
COLOR_GRIS_CLARO = (200, 200, 200)
COLOR_GRIS = (100, 100, 100)
COLOR_GRIS_OSCURO = (50, 50, 50)

import pygame
import os

ruta_fuentes = os.getcwd() + "\\recursos\\fuentes\\"

def mostrar_texto(PANTALLA, mensaje, x, y, tamano, fuente = ruta_fuentes + "Rajdhani-Regular", color = (255, 255, 255), flip = False, alias = True):
    fuente = pygame.font.Font(ruta_fuentes + fuente + ".ttf", tamano)
    mensaje = fuente.render(mensaje, alias, color)

    rectangulo = mensaje.get_rect()
    rectangulo.center = (x, y)
    PANTALLA.blit(mensaje, rectangulo)

    if flip:
        pygame.display.flip()

def crear_boton(x, y, ancho, alto):
    superficie = pygame.Surface((ancho, alto))
    superficie.fill(COLOR_AMARILLO)
    rect = superficie.get_rect(x = x, y = y)

    return superficie, rect

def dibujar_boton(pantalla, color_fondo, boton, boton_rect, texto):
    boton.fill(color_fondo)
    boton.set_alpha(200)
    pantalla.blit(boton, boton_rect) # Rajdhani-Bold
    mostrar_texto(pantalla, texto, boton_rect.x + boton_rect.width/2, boton_rect.y + boton_rect.height/2, 35, "Rajdhani-Bold", COLOR_BLANCO)