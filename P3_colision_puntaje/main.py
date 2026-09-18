"""
PARTE 3: Colisiones, puntaje y game over
Esta es la última parte: ¡ahora depende más de ti!
Lee los TODO con atención, pero esta vez no incluyen pistas de código.
"""
import pygame
import random
import sys

pygame.init()

ANCHO, ALTO = 800, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquiva los Meteoritos")
reloj = pygame.time.Clock()
FPS = 60

COLOR_FONDO = (20, 20, 40)
COLOR_JUGADOR = (0, 200, 255)
COLOR_METEORITO = (255, 100, 60)
COLOR_TEXTO = (255, 255, 255)

fuente = pygame.font.SysFont(None, 36)
fuente_grande = pygame.font.SysFont(None, 64)

sprite_jugador = pygame.image.load("MEDIA/infinityguante.png").convert_alpha()
sprite_meteorito = pygame.image.load("MEDIA/Av.png").convert_alpha()
sprite_jugador = pygame.transform.scale(sprite_jugador, (50, 50))
sprite_meteorito = pygame.transform.scale(sprite_meteorito, (50, 50))


JUGADOR_ANCHO, JUGADOR_ALTO = 50, 20
jugador_x = ANCHO // 2 - JUGADOR_ANCHO // 2
jugador_y = ALTO - 50
VELOCIDAD_JUGADOR = 6

meteoritos = []
METEORITO_TAM = 30
VELOCIDAD_METEORITO = 4
INTERVALO_APARICION = 800
ultimo_spawn = pygame.time.get_ticks()

# TODO 1: Crea una variable para llevar el puntaje del jugador, inicializada en 0.

# TODO 2: Crea una variable booleana `juego_terminado` inicializada en False.

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()

    # TODO 3: Haz que el jugador solo pueda moverse mientras `juego_terminado` sea False.
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        jugador_x -= VELOCIDAD_JUGADOR
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        jugador_x += VELOCIDAD_JUGADOR
    jugador_x = max(0, min(jugador_x, ANCHO - JUGADOR_ANCHO))

    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_spawn >= INTERVALO_APARICION:
        x = random.randint(0, ANCHO - METEORITO_TAM)
        meteoritos.append(pygame.Rect(x, 0, METEORITO_TAM, METEORITO_TAM))
        ultimo_spawn = tiempo_actual

    for meteorito in meteoritos:
        meteorito.y += VELOCIDAD_METEORITO
    meteoritos = [m for m in meteoritos if m.y < ALTO]

    jugador_rect = pygame.Rect(jugador_x, jugador_y, JUGADOR_ANCHO, JUGADOR_ALTO)

    # TODO 4: Detecta si el jugador choca con algún meteorito.
    # Si choca, marca `juego_terminado = True`.
    # Pista de concepto (sin código): pygame.Rect tiene un método para saber si
    # colisiona con otro Rect. Revisa la documentación de pygame.Rect si no lo recuerdas.

    # TODO 5: Mientras el juego NO haya terminado, aumenta el puntaje con el paso
    # del tiempo (por ejemplo, sumando 1 cada cuadro, o usando el tiempo transcurrido).

    # TODO 6: Dibuja el puntaje en pantalla usando la fuente ya creada (`fuente`).
    # Pista de concepto: fuente.render(texto, True, color) crea una "superficie"
    # de texto que luego se dibuja con pantalla.blit(superficie, (x, y)).

    # TODO 7: Si `juego_terminado` es True, muestra un mensaje de "Game Over"
    # en el centro de la pantalla en vez de (o además de) seguir el juego normal.

    pantalla.fill(COLOR_FONDO)
    pantalla.blit(sprite_jugador, (jugador_x,jugador_y))
    for meteoritos in meteoritos:
        pantalla.blit(sprite_meteorito, (meteorito.x, meteorito.y))
    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()
