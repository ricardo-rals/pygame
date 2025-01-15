import pygame
import sys
from pygame.locals import *
import random
from config import Configuracoes
import geracao
import pandas as pd
import openpyxl
import som
import teclado
import abertura
import os


nome = input('nome: ')
data = input('data: ')

seq = int(input('digite 1 ou 2 para escolher a sequência: '))
assert seq in {1, 2}


# Initialize Pygame
pygame.init()
# Set the height and width of the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Limit to 60 frames per second
clock.tick(60)




abertura.abertura()





# data frame inicial (vazio)
df =  pd.DataFrame(index=[f'visualizacao', 'resposta'])


seq_trials_1 = [[(8, 5, 5), (6, 1, 9), (4, 3, 9), (6, 4, 1)]]

seq_trials_2 = [[(5, 4, 7), (3, 2, 3), (5, 4, 9)], [(5, 2, 9), (8, 2, 9), (6, 3, 9)], [(7, 4, 3), (6, 2, 1), (8, 1, 9), (3, 1, 7)], [(3, 5, 9), (6, 1, 7), (5, 1, 3), (9, 3, 5)], [(7, 1, 7), (8, 3, 1), (9, 3, 7), (5, 1, 7), (8, 2, 3)], [(6, 4, 3), (3, 4, 3), (6, 1, 9), (6, 3, 5), (4, 4, 9)], [(9, 4, 5), (5, 1, 5), (3, 3, 5), (4, 2, 7), (9, 4, 9)], [(3, 3, 7), (3, 2, 7), (6, 3, 1), (3, 2, 1), (6, 1, 3)], [(7, 2, 9), (6, 2, 3), (8, 5, 5), (8, 4, 7), (8, 2, 1)], [(4, 1, 7), (6, 1, 5), (8, 2, 5), (8, 4, 9), (4, 5, 5)], [(4, 5, 3), (3, 2, 5), (9, 5, 1), (5, 2, 5)], [(3, 2, 9), (9, 5, 7), (4, 3, 7), (7, 2, 1), (3, 3, 9)], [(7, 4, 9), (7, 5, 9), (4, 4, 7), (7, 1, 9)], [(5, 2, 1), (5, 5, 5), (4, 1, 3), (6, 4, 9)], [(7, 3, 1), (7, 1, 3), (5, 3, 9), (9, 2, 1), (8, 2, 7)], [(6, 5, 9), (5, 4, 1), (8, 1, 5)], [(4, 3, 3), (4, 5, 1), (4, 2, 3)], [(7, 4, 5), (5, 2, 3), (4, 4, 1), (9, 5, 5)], [(4, 2, 9), (8, 5, 3), (7, 2, 5)], [(6, 5, 1), (8, 3, 5), (4, 4, 5), (4, 2, 1)], [(5, 4, 3), (9, 1, 9), (6, 3, 7)], [(4, 4, 3), (6, 4, 5), (7, 2, 3), (6, 2, 5), (6, 4, 1)], [(3, 1, 5), (3, 4, 5), (9, 1, 3), (7, 4, 1)], [(5, 2, 7), (9, 3, 1), (4, 2, 5), (7, 3, 7), (6, 2, 9)], [(9, 1, 5), (4, 5, 9), (3, 3, 1), (3, 4, 9), (8, 3, 9)], [(4, 1, 9), (8, 5, 7), (3, 5, 1), (9, 5, 9)], [(6, 5, 7), (4, 5, 7), (3, 1, 3), (8, 5, 1), (3, 5, 3)], [(3, 1, 9), (7, 3, 5), (8, 1, 7)], [(7, 3, 9), (9, 3, 3), (9, 3, 9), (6, 3, 3), (6, 2, 7)], [(7, 5, 7), (4, 3, 5), (9, 2, 5)], [(4, 3, 9), (4, 1, 5), (4, 3, 1)], [(3, 3, 3), (3, 5, 7), (7, 5, 1)], [(3, 5, 5), (9, 2, 3), (7, 4, 7), (3, 4, 1)], [(9, 4, 7), (9, 4, 3), (9, 5, 3), (9, 1, 7)], [(9, 2, 7), (5, 5, 3), (5, 5, 9), (5, 3, 5), (8, 4, 1)], [(8, 4, 5), (5, 1, 9), (7, 5, 5), (7, 3, 3)], [(5, 4, 5), (9, 4, 1), (8, 3, 3), (8, 4, 3), (7, 5, 3)], [(6, 5, 5), (8, 5, 9), (5, 3, 1)], [(6, 4, 7), (5, 3, 3), (8, 1, 3), (5, 5, 7)], [(7, 1, 5), (9, 2, 9), (5, 3, 7)], [(8, 3, 7), (3, 4, 7), (6, 5, 3), (7, 2, 7), (5, 5, 1)]]



if seq == 1:  
    sequencia = enumerate(seq_trials_1)
if seq == 2:
    sequencia = enumerate(seq_trials_2)
            
               
S = 0
for i in sequencia:
    # mostrar as bolas e distratores
    geracao.simbolo('+', 6, 0.01, 350, quina=True)
    for j in i[1]:
        geracao.simbolo_count(j[0], j[1], j[2], 6, 0.5)

    if len(i[1]) == 2:
        colunas = [f'item {i[0]} {len(i[1])} i {i[1][0][0]} {i[1][0][1]} {i[1][0][2]}', 
                   f'item {i[0]} {len(i[1])} ii {i[1][1][0]} {i[1][1][1]} {i[1][1][2]}']   
        lista_mostrada = [i[1][0][0], i[1][1][0]]     
    elif len(i[1]) == 3:
        colunas = [f'item {i[0]} {len(i[1])} i {i[1][0][0]} {i[1][0][1]} {i[1][0][2]}', 
                   f'item {i[0]} {len(i[1])} ii {i[1][1][0]} {i[1][1][1]} {i[1][1][2]}', 
                   f'item {i[0]} {len(i[1])} iii {i[1][2][0]} {i[1][2][1]} {i[1][2][2]}']
        lista_mostrada = [i[1][0][0], i[1][1][0], i[1][2][0]]
    elif len(i[1]) == 4:
        colunas = [f'item {i[0]} {len(i[1])} i {i[1][0][0]} {i[1][0][1]} {i[1][0][2]}', 
                   f'item {i[0]} {len(i[1])} ii {i[1][1][0]} {i[1][1][1]} {i[1][1][2]}', 
                   f'item {i[0]} {len(i[1])} iii {i[1][2][0]} {i[1][2][1]} {i[1][2][2]}',
                   f'item {i[0]} {len(i[1])} iv {i[1][3][0]} {i[1][3][1]} {i[1][3][2]}']
        lista_mostrada = [i[1][0][0], i[1][1][0], i[1][2][0], i[1][3][0]]
    elif len(i[1]) == 5:
        colunas = [f'item {i[0]} {len(i[1])} i {i[1][0][0]} {i[1][0][1]} {i[1][0][2]}', 
                   f'item {i[0]} {len(i[1])} ii {i[1][1][0]} {i[1][1][1]} {i[1][1][2]}', 
                   f'item {i[0]} {len(i[1])} iii {i[1][2][0]} {i[1][2][1]} {i[1][2][2]}',
                   f'item {i[0]} {len(i[1])} iv {i[1][3][0]} {i[1][3][1]} {i[1][3][2]}',
                   f'item {i[0]} {len(i[1])} v {i[1][4][0]} {i[1][4][1]} {i[1][4][2]}',]
        lista_mostrada = [i[1][0][0], i[1][1][0], i[1][2][0], i[1][3][0], i[1][4][0]]
    elif len(i[1]) == 6:
        colunas = [f'item {i[0]} {len(i[1])} i {i[1][0][0]} {i[1][0][1]} {i[1][0][2]}', 
                   f'item {i[0]} {len(i[1])} ii {i[1][1][0]} {i[1][1][1]} {i[1][1][2]}', 
                   f'item {i[0]} {len(i[1])} iii {i[1][2][0]} {i[1][2][1]} {i[1][2][2]}',
                   f'item {i[0]} {len(i[1])} iv {i[1][3][0]} {i[1][3][1]} {i[1][3][2]}',
                   f'item {i[0]} {len(i[1])} v {i[1][4][0]} {i[1][4][1]} {i[1][4][2]}',
                   f'item {i[0]} {len(i[1])} vi {i[1][5][0]} {i[1][5][1]} {i[1][5][2]}']
        lista_mostrada = [i[1][0][0], i[1][1][0], i[1][2][0], i[1][3][0], 
                            i[1][4][0], i[1][5][0]]
    elif len(i[1]) == 7:
        colunas = [f'item {i[0]} {len(i[1])} i {i[1][0][0]} {i[1][0][1]} {i[1][0][2]}', 
                   f'item {i[0]} {len(i[1])} ii {i[1][1][0]} {i[1][1][1]} {i[1][1][2]}', 
                   f'item {i[0]} {len(i[1])} iii {i[1][2][0]} {i[1][2][1]} {i[1][2][2]}',
                   f'item {i[0]} {len(i[1])} iv {i[1][3][0]} {i[1][3][1]} {i[1][3][2]}',
                   f'item {i[0]} {len(i[1])} v {i[1][4][0]} {i[1][4][1]} {i[1][4][2]}',
                   f'item {i[0]} {len(i[1])} vi {i[1][5][0]} {i[1][5][1]} {i[1][5][2]}',
                   f'item {i[0]} {len(i[1])} vii {i[1][6][0]} {i[1][6][1]} {i[1][6][2]}']
        lista_mostrada = [i[1][0][0], i[1][1][0], i[1][2][0], i[1][3][0], 
                            i[1][4][0], i[1][5][0], i[1][6][0]]
    elif len(i[1]) == 8:
        colunas = [f'item {i[0]} {len(i[1])} i {i[1][0][0]} {i[1][0][1]} {i[1][0][2]}', 
                   f'item {i[0]} {len(i[1])} ii {i[1][1][0]} {i[1][1][1]} {i[1][1][2]}', 
                   f'item {i[0]} {len(i[1])} iii {i[1][2][0]} {i[1][2][1]} {i[1][2][2]}',
                   f'item {i[0]} {len(i[1])} iv {i[1][3][0]} {i[1][3][1]} {i[1][3][2]}',
                   f'item {i[0]} {len(i[1])} v {i[1][4][0]} {i[1][4][1]} {i[1][4][2]}',
                   f'item {i[0]} {len(i[1])} vi {i[1][5][0]} {i[1][5][1]} {i[1][5][2]}',
                   f'item {i[0]} {len(i[1])} vii {i[1][6][0]} {i[1][6][1]} {i[1][6][2]}',
                   f'item {i[0]} {len(i[1])} viii {i[1][7][0]} {i[1][7][1]}',]
        lista_mostrada = [i[1][0][0], i[1][1][0], i[1][2][0], i[1][3][0], 
                            i[1][4][0], i[1][5][0], i[1][6][0], i[1][7][0]]
                   
    lista_resultados = teclado.captacao_numeros_counting(len(i[1]))    
#    print(lista_resultados)
#    print(lista_mostrada)
#    print(colunas)
    
    df_gerado = pd.DataFrame([lista_mostrada, lista_resultados],
                   index=[f'visualizacao', 'resposta'],
                   columns=colunas)
    df = df.join(df_gerado)
    geracao.simbolo('', random.choice([2.5,3.5,4.5]), 0.1, 40)
    S += 1
    if S == 21:
        abertura.intervalo()    
         
    

    

caminho_diretorio = "excel_count_span"   
if not os.path.exists(caminho_diretorio):
    os.makedirs(caminho_diretorio) 
    
# salvar os dados no excel
titulo = nome + ' ' + data + ' seq '+ str(seq)
df.to_excel(f"excel_count_span/{titulo}.xlsx")  







screen.fill(Configuracoes().black)
pygame.display.flip()
pygame.time.delay(1000)

pygame.quit()
sys.exit() 
