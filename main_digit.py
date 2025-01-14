import pygame
import sys
from pygame.locals import *
import random
from config import Configuracoes
import geracao
import pandas as pd
import teclado
import abertura
import os

nome = input('nome: ')
data = input('data: ')
assert data.isdigit() == True

seq = int(input('digite 1 ou 2 para escolher a sequência: '))
assert seq in {1, 2}

# Initialize Pygame
pygame.init()
info = pygame.display.Info()  # Obtém informações do monitor
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Limit to 60 frames per second
clock.tick(60)

abertura.abertura()

# Data frame inicial (vazio)
df = pd.DataFrame(index=[f'visualizacao', 'resposta'])


seq_trials_1 = [5, 7, 5, 7, 7, 7, 7, 7, 7, 3, 5, 5, 5, 7, 5, 3, 7, 7, 7, 3, 7, 3, 7, 
                7, 5, 5, 3, 7, 7, 7, 5, 3, 3, 5, 3, 7, 7, 5, 5, 5, 3, 7, 5, 3, 3, 3, 3, 3, 5, 5]
seq_trials_2 = [7, 3, 3, 3, 7, 7, 7, 5, 7, 5, 5, 3, 7, 3, 7, 5, 5, 7, 3, 7, 5, 3, 7,
                 3, 7, 5, 3, 3, 5, 7, 5, 5, 7, 3, 5, 5, 7, 7, 7, 5, 5, 5, 7, 3, 7, 7, 5, 3, 3, 7]

if seq == 1:  
    sequencia = enumerate(seq_trials_1)
if seq == 2:
    sequencia = enumerate(seq_trials_2)

caminho_diretorio = "excel_digit_span"
titulo = nome + ' ' + data + ' seq ' + str(seq)

for i in sequencia:
    geracao.simbolo('+', 120, 0.01, 350)
    # Gerar a lista de dados
    lista_mostrada = geracao.geracao_dados(i[1])
    a = lista_mostrada
    # Pedir os dados do usuário
    lista_resultados = teclado.captacao_numeros(i[1], df, caminho_diretorio, titulo)
    
    if i[1] == 3:
        colunas = [f'item {i[0]} {i[1]} i {a[0]}', f'item {i[0]} {i[1]} ii {a[1]}', f'item {i[0]} {i[1]} iii {a[2]}']
    elif i[1] == 5:
        colunas = [f'item {i[0]} {i[1]} i {a[0]}', f'item {i[0]} {i[1]} ii {a[1]}', f'item {i[0]} {i[1]} iii {a[2]}',
                   f'item {i[0]} {i[1]} iv {a[3]}', f'item {i[0]} {i[1]} v {a[4]}']
    elif i[1] == 7:
        colunas = [f'item {i[0]} {i[1]} i {a[0]}', f'item {i[0]} {i[1]} ii {a[1]}', f'item {i[0]} {i[1]} iii {a[2]}',
                   f'item {i[0]} {i[1]} iv {a[3]}', f'item {i[0]} {i[1]} v {a[4]}', f'item {i[0]} {i[1]} vi {a[5]}',
                   f'item {i[0]} {i[1]} vii {a[6]}']
    elif i[1] == 8:
        colunas = [f'item {i[0]} {i[1]} i {a[0]}', f'item {i[0]} {i[1]} ii {a[1]}', f'item {i[0]} {i[1]} iii {a[2]}',
                   f'item {i[0]} {i[1]} iv {a[3]}', f'item {i[0]} {i[1]} v {a[4]}', f'item {i[0]} {i[1]} vi {a[5]}',
                   f'item {i[0]} {i[1]} vii {a[6]}', f'item {i[0]} {i[1]} viii {a[7]}']
    
    df_gerado = pd.DataFrame([lista_mostrada, lista_resultados],
                             index=[f'visualizacao', 'resposta'],
                             columns=colunas)
    df = df.join(df_gerado)
    geracao.simbolo('', random.choice([2.5, 3.5, 4.5]), 0.1, 40)

# Salvar os dados no excel
if not os.path.exists(caminho_diretorio):
    os.makedirs(caminho_diretorio)

df.to_excel(f"{caminho_diretorio}/{titulo}.xlsx")  

screen.fill(Configuracoes().black)
pygame.display.flip()
pygame.time.delay(1000)
pygame.quit()
sys.exit()