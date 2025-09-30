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
    azul     = (0, 0, 255)
    branco   = (255, 255, 255)
    vermelho = (255, 0, 0)

    vertice_azul     = [(0,0),   (100,0),  (100,200), (0,200)]
    vertice_branco   = [(100,0), (200,0),  (200,200), (100,200)]
    vertice_vermelho = [(200,0), (300,0),  (300,200), (200,200)]

    pygame.draw.polygon(window, azul, vertice_azul)
    pygame.draw.polygon(window, branco, vertice_branco)
    pygame.draw.polygon(window, vermelho, vertice_vermelho) 

    pygame.display.update() 
    
def game_loop(window):

    while True:
        if recebe_eventos() == False:
            break
        desenha(window)