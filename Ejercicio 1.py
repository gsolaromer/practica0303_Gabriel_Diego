import pygame #Importo la librería "pygame"

# Inicialización de Pygame
pygame.init()

# Inicialización de la superficie de dibujo
ventana = pygame.display.set_mode((600,500)) #Establece el tamaño de la ventana
pygame.display.set_caption("Kripto War") #Establece el nombre de la ventana

# Bucle principal del juego
jugando = True #Establezco variable en verdadero
while jugando: #Establezco el bucle
    # Comprobamos los eventos
    #Comprobamos si se ha pulsado el botón de cierre de la ventana
    for event in pygame.event.get(): #Establezco la variable a la que afecta la condición del bucle
        if event.type == pygame.QUIT: #Establezco la condicion del bucle
            jugando = False

    # Se pinta la ventana con un color
    # Esto borra los posibles elementos que teníamos anteriormente
    ventana.fill((119, 158, 203))

    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()

    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)

pygame.quit() #Cierro el juego
