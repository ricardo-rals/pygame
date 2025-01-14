import pygame
import sys
from pygame.locals import *
import random
from config import Configuracoes
import geracao
import math


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
l = min(screen_width//40, screen_height//20)

def simbolo(x, tempo1, tempo2, tamanho, quina = False, mouse = False):
    '''imprime o símbolo x na tela durante tempo tempo1
     depois uma tela preta por um tempo tempo2 e se 
     quina = True, imprime um quadradinho no canto direito
     embaixo da tela (para sincronizacao)'''
    
    pygame.mouse.set_visible(mouse)
    if isinstance(x, int):
        palavra = str(x)
    elif isinstance(x, str):
        palavra = x
    screen.fill(Configuracoes().black)
    font = pygame.font.Font('freesansbold.ttf', tamanho)
    text = font.render(palavra, True, Configuracoes().white,
                       Configuracoes().black)
    textRect = text.get_rect()
    textRect.center = (screen_width//2, screen_height//2)
    screen.blit(text, textRect)
    if quina == True:
        lado = Configuracoes().lado_quadradinho
        pygame.draw.rect(screen, Configuracoes().white, 
                        pygame.Rect(0, screen_height-lado,
                       lado, screen_height))
    pygame.display.flip()
    pygame.time.delay(math.floor(tempo1*10))
    if tempo2 > 0:
        screen.fill(Configuracoes().black)
        pygame.display.flip()
        pygame.time.delay(math.floor(tempo2*10))
        
        
        
def simbolo_3_linhas(x, y, z, tempo1, tempo2, tamanho, quina = False, mouse = False):
    '''imprime os símbolos x, y, z na tela durante tempo tempo1
     depois uma tela preta por um tempo tempo2 e se 
     quina = True, imprime um quadradinho no canto direito
     embaixo da tela (para sincronizacao)'''
    
    pygame.mouse.set_visible(mouse)
    if isinstance(x, int):
        palavra_1 = str(x)
    elif isinstance(x, str):
        palavra_1 = x
    if isinstance(y, int):
        palavra_2 = str(y)
    elif isinstance(y, str):
        palavra_2 = y
    if isinstance(z, int):
        palavra_3 = str(z)
    elif isinstance(z, str):
        palavra_3 = z
    screen.fill(Configuracoes().black)
    font = pygame.font.Font('freesansbold.ttf', tamanho)
    L = screen_height//7
    
    text = font.render(palavra_1, True, Configuracoes().white,
                       Configuracoes().black)
    textRect = text.get_rect()
    textRect.center = (screen_width//2, screen_height//2 - L)
    screen.blit(text, textRect)
        
    text = font.render(palavra_2, True, Configuracoes().white,
                       Configuracoes().black)
    textRect = text.get_rect()
    textRect.center = (screen_width//2, screen_height//2)
    screen.blit(text, textRect)
    
    text = font.render(palavra_3, True, Configuracoes().white,
                       Configuracoes().black)
    textRect = text.get_rect()
    textRect.center = (screen_width//2, screen_height//2 + L)
    screen.blit(text, textRect)
    
    
    
    if quina == True:
        lado = Configuracoes().lado_quadradinho
        pygame.draw.rect(screen, Configuracoes().white, 
                        pygame.Rect(screen_width-lado, screen_height-lado,
                        screen_width, screen_height))
    pygame.display.flip()
    pygame.time.delay(math.floor(tempo1*10))
    if tempo2 > 0:
        screen.fill(Configuracoes().black)
        pygame.display.flip()
        pygame.time.delay(math.floor(tempo2*10))        


def geracao_dados(n):
    'gera n números na tela e devolve a lista com que eles apareceram'
    
    lista = []
    for i in range(n):
        x = random.randint(0, 9)
        simbolo(x, 1, 0.1, 380, quina = True)
        lista.append(x)
    
    return lista
    
    
def simbolo_count(bolas_brancas, distr_brancos, distr_azuis, tempo1, tempo2, quina = False):
    '''imprime bolas brancas, quadrados brancos bolas azuis 
    durante um tempo1 e depois uma tela preta  por um tempo2.
    Se quina == True, imprime também um quadradinho no canto.'''  
    
    #para tornar o mouse invisível
    pygame.mouse.set_visible(False)
    
    screen.fill(Configuracoes().black)
    pontos = [(x*(screen_width//10)+screen_width//20+random.randint(-screen_width//40,screen_width//40),
              y*(screen_height//5)+(screen_height//10)+random.randint(-(screen_height//20), (screen_height//20)))
              for x in range(9) for y in range(5)]  
    total = bolas_brancas + distr_brancos + distr_azuis
    pontos_escolhidos = random.sample(pontos, total)
    for i in range(bolas_brancas):
        pygame.draw.circle(screen, Configuracoes().white, pontos_escolhidos[i], l)
    for i in range(bolas_brancas, bolas_brancas + distr_azuis):
        pygame.draw.circle(screen, Configuracoes().blue, pontos_escolhidos[i], l)
    for i in range(bolas_brancas + distr_azuis, total):    
        (a,b) = pontos_escolhidos[i]
        coordenadas = [(a-l, b-l), (2*l, 2*l)]
        pygame.draw.rect(screen, Configuracoes().white, coordenadas, l)
    if quina == True:
        lado = Configuracoes().lado_quadradinho
        pygame.draw.rect(screen, Configuracoes().white, 
                        pygame.Rect(screen_width-lado, screen_height-lado,
                        screen_width, screen_height))
    pygame.display.flip()
    pygame.time.delay(math.floor(tempo1*10))
    if tempo2 > 0:
        screen.fill(Configuracoes().black)
        pygame.display.flip()
        pygame.time.delay(math.floor(tempo2*10)) 
    
    #return [bolas_brancas, distratores]  