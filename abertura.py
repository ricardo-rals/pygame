import pygame
import sys
from pygame.locals import *
import geracao
import som


def abertura():
    '''mensagem para comecar o programa
    e testes iniciais'''
    
    estado = True
    while estado:
        geracao.simbolo_3_linhas ('Não mova a cabeça bruscamente', 'Não cruze pernas nem braços', 'Pisque quando pedido', 0, 0, 45)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                estado = False
            
    geracao.simbolo('+',120, 0, 350)
    for _ in range(3):
        geracao.simbolo('Pisque', 2, 0, 200, quina=True)
        geracao.simbolo('', 2, 0, 40)
    geracao.simbolo('Vamos começar', 2, 0, 120)
    geracao.simbolo('', 2, 0, 40)


def abertura_pratica():
    '''mensagem para comecar o programa
    e testes iniciais'''
    
    estado = True
    while estado:
        geracao.simbolo_3_linhas ('Não mova a cabeça bruscamente', 'Não cruze pernas nem braços', 'Pisque quando pedido', 0, 0, 90)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                estado = False
            
    geracao.simbolo('+',120, 0, 350)
    for _ in range(3):
        geracao.simbolo('Pisque', 2, 0, 200, quina=True)
        geracao.simbolo('', 2, 0, 40)
    geracao.simbolo('Vamos começar', 2, 0, 120)
    geracao.simbolo('', 2, 0, 40)
    
    
def intervalo():
    '''intervalo no meio do experimento'''
    
    estado = True
    while estado:
        geracao.simbolo('Pausa', 0, 0 , 120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                estado = False
    #geracao.simbolo_3_linhas ('Não mova a cabeça bruscamente', 'Não cruze pernas nem braços', 'Pisque quando pedido', 20, 0, 90)            
    geracao.simbolo('+', 120, 0, 350)
    for _ in range(3):
        geracao.simbolo('Pisque', 2, 0, 200, quina=True)
        geracao.simbolo('', 2, 0, 40)
    geracao.simbolo('Vamos começar', 2, 0, 120)
    geracao.simbolo('', 2, 0, 40)
