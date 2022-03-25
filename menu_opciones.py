import pygame
import sys
import os

from configuracion import *
from extras import *

ruta_imagenes_menu = os.getcwd() + "\\recursos\\imagenes\\menu\\"
fondo = pygame.image.load(ruta_imagenes_menu + "fondo.png").convert_alpha()

def menu_opciones(juego):
    pantalla = juego.PANTALLA
    pantalla.fill(COLOR_NEGRO)
    fondo.set_alpha(220)
    pantalla.blit(fondo, (0, 0))

    click = False

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego.cerrar()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                juego.estado = "menu"

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                click = True

    if juego.sonidos.hay_musica() == False:
        juego.sonidos.cargar_musica("fondo1", 0.1)
        juego.sonidos.reproducir_musica()

    mx, my = pygame.mouse.get_pos()

    boton_atras, boton_atras_rect = crear_boton(80, 80, 300, 65)

    if boton_atras_rect.collidepoint(mx, my):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if juego.mouse_encima == False:
            juego.sonidos.reproducir("mouse_encima")
            juego.mouse_encima = True

        if click:
            juego.sonidos.reproducir("click")
            juego.estado = "menu"

        dibujar_boton(pantalla, COLOR_GRIS_OSCURO, boton_atras, boton_atras_rect, "Atrás")
    
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        dibujar_boton(pantalla, COLOR_GRIS, boton_atras, boton_atras_rect, "Atrás")
        juego.mouse_encima = False

    mostrar_texto(pantalla, "0.1.0", 30, ALTO - 20, 20, "Rajdhani-Regular", COLOR_BLANCO)
    pygame.display.flip()