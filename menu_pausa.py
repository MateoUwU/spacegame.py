import pygame
import os

from configuracion import *
from extras import *

ruta_imagenes_menu = os.getcwd() + "\\recursos\\imagenes\\menu\\"
fondo = pygame.image.load(ruta_imagenes_menu + "fondo.png").convert_alpha()

def menu_pausa(juego):
    pygame.mouse.set_visible(True)

    if juego.sonidos.hay_musica():
        juego.sonidos.pausar_musica()

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
                juego.estado = "juego"
                juego.sonidos.reanudar_musica()
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                click = True

    mx, my = pygame.mouse.get_pos()

    boton_continuar, boton_continuar_rect = crear_boton(80, 80, 300, 65)
    boton_menu, boton_menu_rect = crear_boton(80, 165, 300, 65)
    boton_salir, boton_salir_rect = crear_boton(80, 250, 300, 65)

    if boton_continuar_rect.collidepoint(mx, my):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if juego.mouse_encima == False:
            juego.sonidos.reproducir("mouse_encima")
            juego.mouse_encima = True

        if click:
            pygame.mouse.set_visible(False)
            juego.sonidos.reproducir("click")
            juego.estado = "juego"
            juego.sonidos.reanudar_musica()

        dibujar_boton(pantalla, COLOR_GRIS_OSCURO, boton_continuar, boton_continuar_rect, "Continuar")
        dibujar_boton(pantalla, COLOR_GRIS, boton_menu, boton_menu_rect, "Menú Principal")
        dibujar_boton(pantalla, COLOR_GRIS, boton_salir, boton_salir_rect, "Salir")
    
    elif boton_menu_rect.collidepoint(mx, my):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if juego.mouse_encima == False:
            juego.sonidos.reproducir("mouse_encima")
            juego.mouse_encima = True

        if click:
            juego.sonidos.reproducir("click")
            juego.estado = "menu"
            juego.reiniciar()
            juego.sonidos.parar_musica()

        dibujar_boton(pantalla, COLOR_GRIS, boton_continuar, boton_continuar_rect, "Continuar")
        dibujar_boton(pantalla, COLOR_GRIS_OSCURO, boton_menu, boton_menu_rect, "Menú Principal")
        dibujar_boton(pantalla, COLOR_GRIS, boton_salir, boton_salir_rect, "Salir")
    
    elif boton_salir_rect.collidepoint(mx, my):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if juego.mouse_encima == False:
            juego.sonidos.reproducir("mouse_encima")
            juego.mouse_encima = True

        if click:
            juego.sonidos.reproducir("click")
            juego.cerrar()

        dibujar_boton(pantalla, COLOR_GRIS, boton_continuar, boton_continuar_rect, "Continuar")
        dibujar_boton(pantalla, COLOR_GRIS, boton_menu, boton_menu_rect, "Menú Principal")
        dibujar_boton(pantalla, COLOR_GRIS_OSCURO, boton_salir, boton_salir_rect, "Salir")

    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        dibujar_boton(pantalla, COLOR_GRIS, boton_continuar, boton_continuar_rect, "Continuar")
        dibujar_boton(pantalla, COLOR_GRIS, boton_menu, boton_menu_rect, "Menú Principal")
        dibujar_boton(pantalla, COLOR_GRIS, boton_salir, boton_salir_rect, "Salir")

        juego.mouse_encima = False

    pygame.display.flip()