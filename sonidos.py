import pygame

pygame.mixer.init()

sonido_disparo = pygame.mixer.Sound("recursos/sonidos/disparo.mp3")
sonido_destruccion_asteroide = pygame.mixer.Sound("recursos/sonidos/destruccion_asteroide.mp3")
sonido_crash = pygame.mixer.Sound("recursos/sonidos/crash.mp3")
sonido_nivel = pygame.mixer.Sound("recursos/sonidos/sonido-nivel.mp3")
sonido_mouse_encima = pygame.mixer.Sound("recursos/sonidos/mouse_encima.mp3")
sonido_click = pygame.mixer.Sound("recursos/sonidos/click.mp3")

class Sonidos:
    def __init__(self) -> None:
        self.sonidos = {
            "disparo": sonido_disparo,
            "destruccion_asteroide": sonido_destruccion_asteroide,
            "crash": sonido_crash,
            "nivel": sonido_nivel,
            "mouse_encima": sonido_mouse_encima,
            "click": sonido_click
        }

    def reproducir(self, sonido: str) -> None:
        self.sonidos[sonido].set_volume(0.2)
        self.sonidos[sonido].play()

    def cargar_musica(self, musica: str, volumen: float) -> None:
        pygame.mixer.music.load("recursos/musica/" + musica + ".mp3")
        pygame.mixer.music.set_volume(volumen)

    def reproducir_musica(self) -> None:
        pygame.mixer.music.play()

    def parar_musica(self) -> None:
        volumen = pygame.mixer.music.get_volume()

        i = volumen
        while i > 0:
            pygame.mixer.music.set_volume(volumen - 0.1)
            i -= 1

        pygame.mixer.music.stop()

    def pausar_musica(self) -> None:
        pygame.mixer.music.pause()
    
    def reanudar_musica(self) -> None:
        pygame.mixer.music.unpause()

    def posicion_musica(self) -> int:
        return pygame.mixer.music.get_pos()

    def hay_musica(self) -> bool:
        return pygame.mixer.music.get_busy()

    def reiniciar_musica(self) -> None:
        pygame.mixer.music.rewind()