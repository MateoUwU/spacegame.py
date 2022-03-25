import pygame

from configuracion import *
from extras import *

def menu_derrota(juego):
    pygame.mouse.set_visible(True)

    if juego.sonidos.hay_musica():
        juego.sonidos.parar_musica()

    pantalla = juego.PANTALLA
    pantalla.fill(COLOR_NEGRO)

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

    mostrar_texto(pantalla, "Has Perdido", ANCHO // 2, 80, 50, "Rajdhani-Regular", COLOR_BLANCO)
    mostrar_texto(pantalla, "Inténtalo una vez más", ANCHO // 2, 140, 50, "Rajdhani-Regular", COLOR_BLANCO)

    mx, my = pygame.mouse.get_pos()

    boton_reiniciar, boton_reiniciar_rect = crear_boton(ANCHO / 2 - 150, 220, 300, 65)
    boton_menu, boton_menu_rect = crear_boton(ANCHO / 2 - 150, 220 + 85, 300, 65)
    boton_salir, boton_salir_rect = crear_boton(ANCHO / 2 - 150, 220 + 85 * 2, 300, 65)

    if boton_reiniciar_rect.collidepoint(mx, my):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if juego.mouse_encima == False:
            juego.sonidos.reproducir("mouse_encima")
            juego.mouse_encima = True

        if click:
            pygame.mouse.set_visible(False)
            juego.sonidos.reproducir("click")
            juego.estado = "juego"
            juego.sonidos.reproducir_musica()

        dibujar_boton(pantalla, COLOR_GRIS_OSCURO, boton_reiniciar, boton_reiniciar_rect, "Reiniciar")
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

        dibujar_boton(pantalla, COLOR_GRIS, boton_reiniciar, boton_reiniciar_rect, "Reiniciar")
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

        dibujar_boton(pantalla, COLOR_GRIS, boton_reiniciar, boton_reiniciar_rect, "Reiniciar")
        dibujar_boton(pantalla, COLOR_GRIS, boton_menu, boton_menu_rect, "Menú Principal")
        dibujar_boton(pantalla, COLOR_GRIS_OSCURO, boton_salir, boton_salir_rect, "Salir")

    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        dibujar_boton(pantalla, COLOR_GRIS, boton_reiniciar, boton_reiniciar_rect, "Reiniciar")
        dibujar_boton(pantalla, COLOR_GRIS, boton_menu, boton_menu_rect, "Menú Principal")
        dibujar_boton(pantalla, COLOR_GRIS, boton_salir, boton_salir_rect, "Salir")

        juego.mouse_encima = False

    pygame.display.flip()