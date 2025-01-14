import pygame
from pygame.locals import *
import random
from config import Configuracoes
# import math
import time

pygame.init()
info = pygame.display.Info()  # Obtém informações do monitor
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
# screen_width, screen_height = screen.get_size()
l = min(screen_width//40, screen_height//20)
def simbolo(x, tempo1, tempo2, tamanho, quina=False, mouse=False):
    '''Exibe o símbolo x na tela durante tempo tempo1
     depois uma tela preta por um tempo tempo2. Se 
     quina=True, desenha um quadradinho no canto direito
     inferior da tela.'''
    
    pygame.mouse.set_visible(mouse)
    palavra = str(x) if isinstance(x, int) else x
    screen.fill(Configuracoes().black)
    font = pygame.font.Font('freesansbold.ttf', tamanho)
    text = font.render(palavra, True, Configuracoes().white, Configuracoes().black)
    textRect = text.get_rect()
    textRect.center = (screen_width // 2, screen_height // 2)
    screen.blit(text, textRect)

    if quina:
        lado = Configuracoes().lado_quadradinho
        pygame.draw.rect(screen, Configuracoes().white,
                         pygame.Rect(screen_width - lado, screen_height - lado, lado, lado))
    pygame.display.flip()

    # Controle do tempo com loop
    start_time = time.time()
    while time.time() - start_time < tempo1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    if tempo2 > 0:
        screen.fill(Configuracoes().black)
        pygame.display.flip()

        start_time = time.time()
        while time.time() - start_time < tempo2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return


def simbolo_3_linhas(x, y, z, tempo1, tempo2, tamanho, quina=False, mouse=False):
    '''Exibe os símbolos x, y, z na tela durante tempo tempo1
     depois uma tela preta por um tempo tempo2. Se 
     quina=True, desenha um quadradinho no canto direito
     inferior da tela.'''
    
    pygame.mouse.set_visible(mouse)
    palavras = [str(i) if isinstance(i, int) else i for i in (x, y, z)]
    screen.fill(Configuracoes().black)
    font = pygame.font.Font('freesansbold.ttf', tamanho)
    L = screen_height // 7

    for i, palavra in enumerate(palavras):
        text = font.render(palavra, True, Configuracoes().white, Configuracoes().black)
        textRect = text.get_rect()
        textRect.center = (screen_width // 2, screen_height // 2 + (i - 1) * L)
        screen.blit(text, textRect)

    if quina:
        lado = Configuracoes().lado_quadradinho
        pygame.draw.rect(screen, Configuracoes().white,
                         pygame.Rect(screen_width - lado, screen_height - lado, lado, lado))
    pygame.display.flip()

    # Controle do tempo com loop
    start_time = time.time()
    while time.time() - start_time < tempo1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    if tempo2 > 0:
        screen.fill(Configuracoes().black)
        pygame.display.flip()

        start_time = time.time()
        while time.time() - start_time < tempo2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return


def geracao_dados(n):
    '''Gera n números na tela e devolve a lista com os números exibidos'''
    lista = []
    for i in range(n):
        x = random.randint(0, 9)
        simbolo(x, 1, 0.1, 380, quina=True)
        lista.append(x)
    return lista


def simbolo_count(bolas_brancas, distr_brancos, distr_azuis, tempo1, tempo2, quina=False):
    '''Exibe bolas brancas, quadrados brancos e bolas azuis 
    durante tempo tempo1, depois uma tela preta por tempo2.
    Se quina=True, desenha um quadradinho no canto.'''  
    
    pygame.mouse.set_visible(False)
    screen.fill(Configuracoes().black)
    pontos = [(x * (screen_width // 10) + screen_width // 20 + random.randint(-screen_width // 40, screen_width // 40),
               y * (screen_height // 5) + screen_height // 10 + random.randint(-screen_height // 20, screen_height // 20))
              for x in range(9) for y in range(5)]
    total = bolas_brancas + distr_brancos + distr_azuis
    pontos_escolhidos = random.sample(pontos, total)

    for i in range(bolas_brancas):
        pygame.draw.circle(screen, Configuracoes().white, pontos_escolhidos[i], l)
    for i in range(bolas_brancas, bolas_brancas + distr_azuis):
        pygame.draw.circle(screen, Configuracoes().blue, pontos_escolhidos[i], l)
    for i in range(bolas_brancas + distr_azuis, total):
        (a, b) = pontos_escolhidos[i]
        pygame.draw.rect(screen, Configuracoes().white, pygame.Rect(a - l, b - l, 2 * l, 2 * l))

    if quina:
        lado = Configuracoes().lado_quadradinho
        pygame.draw.rect(screen, Configuracoes().white,
                         pygame.Rect(screen_width - lado, screen_height - lado, lado, lado))
    pygame.display.flip()

    # Controle do tempo com loop
    start_time = time.time()
    while time.time() - start_time < tempo1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    if tempo2 > 0:
        screen.fill(Configuracoes().black)
        pygame.display.flip()

        start_time = time.time()
        while time.time() - start_time < tempo2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

    
    #return [bolas_brancas, distratores]  