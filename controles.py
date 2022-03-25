import pygame

def obtenerTeclaMovimiento(key):
    tecla_movimiento_arriba = key == pygame.K_w or key == pygame.K_UP
    tecla_movimiento_abajo = key == pygame.K_s or key == pygame.K_DOWN
    tecla_movimiento_izquierda = key == pygame.K_a or key == pygame.K_LEFT
    tecla_movimiento_derecha = key == pygame.K_d or key == pygame.K_RIGHT

    if tecla_movimiento_arriba:
        return "arriba"
    elif tecla_movimiento_abajo:
        return "abajo"
    elif tecla_movimiento_izquierda:
        return "izquierda"
    elif tecla_movimiento_derecha:
        return "derecha"
    else:
        return None