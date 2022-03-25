import pygame

from controles import *

def actualizar(juego):
    eventos(juego)
    juego.pintar()

    juego.actualizar_nave()
    juego.actualizar_proyectiles()
    juego.actualizar_asteroides()

    juego.cooldown_puntos -= 1
    if juego.cooldown_puntos == 0:
        juego.puntos += 1
        juego.cooldown_puntos = 120

    if juego.puntos % 100 == 0 and juego.puntos != 0:
        juego.transicion_nivel = True

    if juego.transicion_nivel == True:
        juego.cooldown_nivel -= 1

        if juego.cooldown_nivel == 100:
            juego.sonidos.parar_musica()
            juego.sonidos.reproducir("nivel")

        if juego.cooldown_nivel == 0:
            juego.nivel = juego.puntos // 100 + 1

            if juego.nivel > 3:
                juego.nivel = 3

            juego.sonidos.cargar_musica(f"tema{juego.nivel}", 0.1)
            juego.sonidos.reproducir_musica()

            juego.transicion_nivel = False
            juego.cooldown_nivel = 120

    juego.mostrar_puntos()
    juego.disparo_cooldown()
    juego.mostrar_nivel()

    pygame.display.flip()

    if juego.finalizado:
        juego.reiniciar()

    if juego.sonidos.posicion_musica() == -1:
        juego.sonidos.reproducir_musica()

def eventos(juego):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego.cerrar()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                juego.estado = "pausa"

            if evento.key == pygame.K_RETURN:
                if juego.pausa:
                    juego.reanudar()
                else:
                    juego.pausar()

            if juego.pausa == False:
                if evento.key == pygame.K_SPACE:
                    juego.disparar()

                tecla_movimiento = obtenerTeclaMovimiento(evento.key)

                if tecla_movimiento == "arriba":
                    juego.nave.cambiar_direccion("arriba")
                    juego.control_w = True
                if tecla_movimiento == "abajo":
                    juego.nave.cambiar_direccion("abajo")
                    juego.control_s = True
                if tecla_movimiento == "izquierda":
                    juego.nave.cambiar_direccion("izquierda")
                    juego.control_a = True
                if tecla_movimiento == "derecha":
                    juego.nave.cambiar_direccion("derecha")
                    juego.control_d = True
        
        if juego.pausa == False:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                juego.disparar()

        if evento.type == pygame.KEYUP:
            tecla_movimiento = obtenerTeclaMovimiento(evento.key)

            if tecla_movimiento == "arriba":
                juego.control_w = False
            if tecla_movimiento == "abajo":
                juego.control_s = False
            if tecla_movimiento == "izquierda":
                juego.control_a = False
            if tecla_movimiento == "derecha":
                juego.control_d = False
            
            juego.corregir_direccion()