# import pygame
# import sys
# from pygame.locals import *
# from config import Configuracoes
# import som
# import os

# pygame.init()
# info = pygame.display.Info()  # Obtém informações do monitor
# screen_width, screen_height = info.current_w, info.current_h
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
# screen_width, screen_height = screen.get_size()

# def captacao_numeros(n, df, caminho_diretorio, titulo):
#     'função que mostra o teclado e devolve a lista de n respostas'
    
#     pygame.mouse.set_visible(True)   
#     pygame.mouse.set_pos([screen_width // 4, screen_height // 2])
         
#     lista = []

#     class botao(pygame.sprite.Sprite):

#         def __init__(self, palavra, width, height, x, y, funcao=None):
#             pygame.sprite.Sprite.__init__(self)
            
#             if palavra.isdigit():
#                 self.entrada = int(palavra)
#             else:
#                 self.entrada = ''    
            
#             self.cor_fundo = Configuracoes().gray
#             self.font = pygame.font.Font(Configuracoes().fonte, 100)
#             self.textSurf = self.font.render(palavra, True,
#                              Configuracoes().black, self.cor_fundo)
#             self.image = pygame.Surface((width, height))
#             self.image.fill(self.cor_fundo)
#             self.rect = self.image.get_rect()
#             self.rect.x = x
#             self.rect.y = y
#             W = self.textSurf.get_width()
#             H = self.textSurf.get_height()
#             self.image.blit(self.textSurf, [width / 2 - W / 2, height / 2 - H / 2])
#             self.funcao = funcao
        
#         def update(self):
#             mouse = pygame.mouse.get_pos()
#             if self.rect.collidepoint(mouse):
#                 for event in pygame.event.get():
#                     if event.type == pygame.MOUSEBUTTONDOWN:
#                         som.play_curto()
#                         pygame.time.delay(100)
#                         if self.funcao:
#                             self.funcao()  
#                         else:
#                             lista.append(self.entrada)  

#     def mostrar_mensagem(mensagem, tamanho_fonte, cor_texto, x, y):
#         fonte = pygame.font.Font(Configuracoes().fonte, tamanho_fonte)
#         texto = fonte.render(mensagem, True, cor_texto)
#         screen.blit(texto, (x, y))

#     def encerrar_programa():
#         # Salvar os dados no excel
#         if not os.path.exists(caminho_diretorio):
#             os.makedirs(caminho_diretorio)

#         df.to_excel(f"{caminho_diretorio}/{titulo}.xlsx")  
#         # Exibe a mensagem antes de encerrar
#         mostrar_mensagem("Programa sendo encerrado...", 50, Configuracoes().white, screen_width // 2 - 200, screen_height // 2 - 50)
#         pygame.display.flip()
#         pygame.time.delay(2000)  # Exibe a mensagem por 2 segundos
#         pygame.quit()
#         sys.exit()

#     xx = 305
#     yy = 220
#     b_0 = botao('0', 100, 100, 400+xx, 0+yy)
#     b_1 = botao('1', 100, 100, 600+xx, 0+yy)
#     b_2 = botao('2', 100, 100, 800+xx, 0+yy)
#     b_3 = botao('3', 100, 100, 400+xx, 200+yy)
#     b_4 = botao('4', 100, 100, 600+xx, 200+yy)
#     b_5 = botao('5', 100, 100, 800+xx, 200+yy)
#     b_6 = botao('6', 100, 100, 400+xx, 400+yy)
#     b_7 = botao('7', 100, 100, 600+xx, 400+yy)
#     b_8 = botao('8', 100, 100, 800+xx, 400+yy)
#     b_9 = botao('9', 100, 100, 400+xx, 600+yy)
#     b_int = botao('?', 100, 100, 600+xx, 600+yy)
#     b_encerrar = botao('X', 100, 100, 800+xx, 600+yy, funcao=encerrar_programa)

#     all_sprites_list = pygame.sprite.Group()

#     all_sprites_list.add(b_0)
#     all_sprites_list.add(b_1) 
#     all_sprites_list.add(b_2) 
#     all_sprites_list.add(b_3) 
#     all_sprites_list.add(b_4)
#     all_sprites_list.add(b_5)
#     all_sprites_list.add(b_6)
#     all_sprites_list.add(b_7)
#     all_sprites_list.add(b_8)
#     all_sprites_list.add(b_9) 
#     all_sprites_list.add(b_int)
#     all_sprites_list.add(b_encerrar)  # Adiciona o botão de encerrar

#     while len(lista) < n:
#         screen.fill(Configuracoes().black)
#         all_sprites_list.update()
#         all_sprites_list.draw(screen)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         pygame.display.flip()

#     return lista



# def captacao_numeros_counting(n):
#     'funcao que mostra o teclado e devolve a lista de n respostas'
    
#     pygame.mouse.set_visible(True)   
#     pygame.mouse.set_pos([screen_width//4, screen_height//2])
         
#     lista = []

#     class botao(pygame.sprite.Sprite):

#         def __init__(self, palavra, width, height, x, y):
#             # Call the parent class (Sprite) constructor  
            
#             pygame.sprite.Sprite.__init__(self)
            
#             if palavra == "?":
#                 self.entrada = ' '
#             else:
#                 self.entrada = int(palavra)    
            
#             self.cor_fundo = Configuracoes().gray
#             self.font = pygame.font.Font(Configuracoes().fonte, 100)
#             self.textSurf = self.font.render(palavra, True,
#                              Configuracoes().black, self.cor_fundo)
#             self.image = pygame.Surface((width, height))
#             self.image.fill(self.cor_fundo)
#             self.rect = self.image.get_rect()
#             self.rect.x = x
#             self.rect.y = y
#             W = self.textSurf.get_width()
#             H = self.textSurf.get_height()
#             self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
        
#         def update(self):
#             """ Called each frame. """
            
#             mouse = pygame.mouse.get_pos()
#             if self.rect.collidepoint(mouse):
#                 #self.cor_fundo = Configuracoes().blue
#                 for event in pygame.event.get():
#                     if event.type == pygame.MOUSEBUTTONDOWN:
#                         som.play_curto()
#                         pygame.time.delay(100)
#                         lista.append(self.entrada)                        
#             #else:
#                 #self.cor_fundo = Configuracoes().gray
#     xx = 305
#     yy  = 220
#     b_0 = botao('0', 100, 100, 400+xx, 0+yy)
#     b_1 = botao('1', 100, 100, 600+xx, 0+yy)
#     b_2 = botao('2', 100, 100, 800+xx, 0+yy)
#     b_3 = botao('3', 100, 100, 400+xx, 200+yy)
#     b_4 = botao('4', 100, 100, 600+xx, 200+yy)
#     b_5 = botao('5', 100, 100, 800+xx, 200+yy)
#     b_6 = botao('6', 100, 100, 400+xx, 400+yy)
#     b_7 = botao('7', 100, 100, 600+xx, 400+yy)
#     b_8 = botao('8', 100, 100, 800+xx, 400+yy)
#     b_9 = botao('9', 100, 100, 400+xx, 600+yy)
#     b_int = botao('?', 100, 100, 600+xx, 600+yy)

#     all_sprites_list = pygame.sprite.Group()

#     all_sprites_list.add(b_0)
#     all_sprites_list.add(b_1) 
#     all_sprites_list.add(b_2) 
#     all_sprites_list.add(b_3) 
#     all_sprites_list.add(b_4)
#     all_sprites_list.add(b_5)
#     all_sprites_list.add(b_6)
#     all_sprites_list.add(b_7)
#     all_sprites_list.add(b_8)
#     all_sprites_list.add(b_9) 
#     all_sprites_list.add(b_int) 

#     while len(lista) < n:
#         screen.fill(Configuracoes().black)
#         all_sprites_list.update()
#         all_sprites_list.draw(screen)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         pygame.display.flip()

#     return lista

import pygame
import sys
from pygame.locals import *
from config import Configuracoes
import som
import os

pygame.init()
info = pygame.display.Info()  # Obtém informações do monitor
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

def captacao_numeros(n, df, caminho_diretorio, titulo):
    'função que mostra o teclado e devolve a lista de n respostas'
    
    pygame.mouse.set_visible(True)   
    pygame.mouse.set_pos([screen_width // 4, screen_height // 2])
         
    lista = []

    class botao(pygame.sprite.Sprite):

        def __init__(self, palavra, width, height, x, y, funcao=None):
            pygame.sprite.Sprite.__init__(self)
            
            if palavra.isdigit():
                self.entrada = int(palavra)
            else:
                self.entrada = ''    
            
            self.cor_fundo = Configuracoes().gray
            self.font = pygame.font.Font(Configuracoes().fonte, 100)
            self.textSurf = self.font.render(palavra, True,
                             Configuracoes().black, self.cor_fundo)
            self.image = pygame.Surface((width, height))
            self.image.fill(self.cor_fundo)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            W = self.textSurf.get_width()
            H = self.textSurf.get_height()
            self.image.blit(self.textSurf, [width / 2 - W / 2, height / 2 - H / 2])
            self.funcao = funcao
        
        def update(self):
            mouse = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        som.play_curto()
                        pygame.time.delay(100)
                        if self.funcao:
                            self.funcao()  
                        else:
                            lista.append(self.entrada)  

    def mostrar_mensagem(mensagem, tamanho_fonte, cor_texto, x, y):
        fonte = pygame.font.Font(Configuracoes().fonte, tamanho_fonte)
        texto = fonte.render(mensagem, True, cor_texto)
        screen.blit(texto, (x, y))

    def encerrar_programa():
        # Salvar os dados no excel
        if not os.path.exists(caminho_diretorio):
            os.makedirs(caminho_diretorio)

        df.to_excel(f"{caminho_diretorio}/{titulo}.xlsx")  
        # Exibe a mensagem antes de encerrar
        mostrar_mensagem("Programa sendo encerrado...", 50, Configuracoes().white, screen_width // 2 - 200, screen_height // 2 - 50)
        pygame.display.flip()
        pygame.time.delay(2000)  # Exibe a mensagem por 2 segundos
        pygame.quit()
        sys.exit()

    # Calcula a posição inicial para centralizar o teclado
    teclado_largura = 3 * 100 + 2 * 200  # Largura total do teclado
    teclado_altura = 4 * 100 + 3 * 200  # Altura total do teclado
    x_inicio = (screen_width - teclado_largura) // 2
    y_inicio = (screen_height - teclado_altura) // 2

    # Adiciona os botões
    all_sprites_list = pygame.sprite.Group()
    botoes = [
        ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
        ('0', 4, 0), ('?', 4, 1), ('X', 4, 2)
    ]

    for palavra, linha, coluna in botoes:
        funcao = encerrar_programa if palavra == 'X' else None
        x = x_inicio + coluna * 200
        y = y_inicio + linha * 200
        all_sprites_list.add(botao(palavra, 100, 100, x, y, funcao))

    while len(lista) < n:
        screen.fill(Configuracoes().black)
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

    return lista

def captacao_numeros_counting(n, df, caminho_diretorio, titulo):
    'função que mostra o teclado e devolve a lista de n respostas'
    
    pygame.mouse.set_visible(True)   
    pygame.mouse.set_pos([screen_width // 4, screen_height // 2])
         
    lista = []

    class botao(pygame.sprite.Sprite):

        def __init__(self, palavra, width, height, x, y, funcao=None):
            pygame.sprite.Sprite.__init__(self)
            
            if palavra.isdigit():
                self.entrada = int(palavra)
            else:
                self.entrada = ''    
            
            self.cor_fundo = Configuracoes().gray
            self.font = pygame.font.Font(Configuracoes().fonte, 100)
            self.textSurf = self.font.render(palavra, True,
                             Configuracoes().black, self.cor_fundo)
            self.image = pygame.Surface((width, height))
            self.image.fill(self.cor_fundo)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            W = self.textSurf.get_width()
            H = self.textSurf.get_height()
            self.image.blit(self.textSurf, [width / 2 - W / 2, height / 2 - H / 2])
            self.funcao = funcao
        
        def update(self):
            mouse = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        som.play_curto()
                        pygame.time.delay(100)
                        if self.funcao:
                            self.funcao()  
                        else:
                            lista.append(self.entrada)  

    def mostrar_mensagem(mensagem, tamanho_fonte, cor_texto, x, y):
        fonte = pygame.font.Font(Configuracoes().fonte, tamanho_fonte)
        texto = fonte.render(mensagem, True, cor_texto)
        screen.blit(texto, (x, y))

    def encerrar_programa():
        # Salvar os dados no excel
        if not os.path.exists(caminho_diretorio):
            os.makedirs(caminho_diretorio)

        df.to_excel(f"{caminho_diretorio}/{titulo}.xlsx")  
        # Exibe a mensagem antes de encerrar
        mostrar_mensagem("Programa sendo encerrado...", 50, Configuracoes().white, screen_width // 2 - 200, screen_height // 2 - 50)
        pygame.display.flip()
        pygame.time.delay(2000)  # Exibe a mensagem por 2 segundos
        pygame.quit()
        sys.exit()

    # Calcula a posição inicial para centralizar o teclado
    teclado_largura = 3 * 100 + 2 * 200  # Largura total do teclado
    teclado_altura = 4 * 100 + 3 * 200  # Altura total do teclado
    x_inicio = (screen_width - teclado_largura) // 2
    y_inicio = (screen_height - teclado_altura) // 2

    # Adiciona os botões
    all_sprites_list = pygame.sprite.Group()
    botoes = [
        ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
        ('0', 4, 0), ('?', 4, 1), ('X', 4, 2)
    ]

    for palavra, linha, coluna in botoes:
        funcao = encerrar_programa if palavra == 'X' else None
        x = x_inicio + coluna * 200
        y = y_inicio + linha * 200
        all_sprites_list.add(botao(palavra, 100, 100, x, y, funcao))

    while len(lista) < n:
        screen.fill(Configuracoes().black)
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

    return lista