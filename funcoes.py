import pygame

def inicializa():

    pygame.init()

    window = pygame.display.set_mode((320, 240))

    pygame.display.set_caption('Jogo do Erick')

    return window 
 
def recebe_eventos():

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
    return True 
                               
def desenha (window):

    window.fill ((255,0,0)) 
    
    pygame.display.update() 
    
def game_loop(window):

    while True:
        if recebe_eventos() == False:
            break
        desenha(window)