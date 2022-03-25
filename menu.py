import pygame
import sys
import os

from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN

from configuracion import *
from extras import *

ruta_imagenes_menu = os.getcwd() + "\\recursos\\imagenes\\menu\\"
fondo = pygame.image.load(ruta_imagenes_menu + "fondo.png").convert_alpha()

def menu_principal(juego):
    pantalla = juego.PANTALLA
    pantalla.fill(COLOR_NEGRO)
    fondo.set_alpha(220)
    pantalla.blit(fondo, (0, 0))

    click = False

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego.cerrar()

        if evento.type == KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                juego.cerrar()
        
        if evento.type == MOUSEBUTTONDOWN:
            if evento.button == 1:
                click = True

    if juego.sonidos.hay_musica() == False:
        juego.sonidos.cargar_musica("fondo1", 0.1)
        juego.sonidos.reproducir_musica()

    mx, my = pygame.mouse.get_pos()

    boton_jugar, boton_jugar_rect = crear_boton(80, 80, 300, 65)
    boton_opciones, boton_opciones_rect = crear_boton(80, 165, 300, 65)
    boton_salir, boton_salir_rect = crear_boton(80, 250, 300, 65)

    if boton_jugar_rect.collidepoint(mx, my):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if juego.mouse_encima == False:
            juego.sonidos.reproducir("mouse_encima")
            juego.mouse_encima = True

        if click:
            pygame.mouse.set_visible(False)
            juego.sonidos.reproducir("click")
            juego.estado = "juego"
            juego.sonidos.parar_musica()
            juego.sonidos.cargar_musica("tema1", 0.1)
            juego.sonidos.reproducir_musica()

        dibujar_boton(pantalla, COLOR_GRIS_OSCURO, boton_jugar, boton_jugar_rect, "Jugar")
        dibujar_boton(pantalla, COLOR_GRIS, boton_opciones, boton_opciones_rect, "Opciones")
        dibujar_boton(pantalla, COLOR_GRIS, boton_salir, boton_salir_rect, "Salir")

    elif boton_opciones_rect.collidepoint(mx, my):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if juego.mouse_encima == False:
            juego.sonidos.reproducir("mouse_encima")
            juego.mouse_encima = True

        if click:
            juego.sonidos.reproducir("click")
            juego.estado = "opciones"

        dibujar_boton(pantalla, COLOR_GRIS, boton_jugar, boton_jugar_rect, "Jugar")
        dibujar_boton(pantalla, COLOR_GRIS_OSCURO, boton_opciones, boton_opciones_rect, "Opciones")
        dibujar_boton(pantalla, COLOR_GRIS, boton_salir, boton_salir_rect, "Salir")

    elif boton_salir_rect.collidepoint(mx, my):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if juego.mouse_encima == False:
            juego.sonidos.reproducir("mouse_encima")
            juego.mouse_encima = True

        if click:
            juego.sonidos.reproducir("click")
            juego.cerrar()

        dibujar_boton(pantalla, COLOR_GRIS, boton_jugar, boton_jugar_rect, "Jugar")
        dibujar_boton(pantalla, COLOR_GRIS, boton_opciones, boton_opciones_rect, "Opciones")
        dibujar_boton(pantalla, COLOR_GRIS_OSCURO, boton_salir, boton_salir_rect, "Salir")

    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        dibujar_boton(pantalla, COLOR_GRIS, boton_jugar, boton_jugar_rect, "Jugar")
        dibujar_boton(pantalla, COLOR_GRIS, boton_opciones, boton_opciones_rect, "Opciones")
        dibujar_boton(pantalla, COLOR_GRIS, boton_salir, boton_salir_rect, "Salir")

        juego.mouse_encima = False

    mostrar_texto(pantalla, "0.1.0", 30, ALTO - 20, 20, "Rajdhani-Regular", COLOR_BLANCO)
    pygame.display.flip()