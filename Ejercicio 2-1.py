import pygame #Importo la librería "pygame"

pygame.init() #Inicio "pygame"
ventana = pygame.display.set_mode((600,500)) #Establece el tamaño de la ventana
pygame.display.set_caption("Kripto War") #Establece el nombre de la ventana

# Crea el objeto pelota
ball = pygame.image.load("dogecoin-logo2.png")

# Obtengo el rectángulo del objeto anterior
ballrect = ball.get_rect()

# Inicializo los valores con los que se van a mover la pelota
speed = [5,5]

# Pongo la pelota en el origen de coordenadas
ballrect.move_ip(300,100)

jugando = True #Establezco variable en verdadero
while jugando: #Establezco el bucle
    for event in pygame.event.get(): #Establezco la variable a la que afecta la condición
        if event.type == pygame.QUIT: #Establezco la condicion
            jugando = False #Establezco variable en falso

    # Muevo la pelota
    ballrect = ballrect.move(speed)

    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width(): #Establezco las condiciones para cambiar la dirección de la pelota en el borde izquierdo y derecho
        speed[0] = -speed[0] #Cambio la dirección de la pelota
            
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height(): #Establezco las condiciones para cambiar la dirección de la pelota en el borde superior e inferior
        speed[1] = -speed[1] #Cambio la dirección de la pelota
    
    ventana.fill((119, 158, 203)) #Establezco el color de fondo de la pantalla

    # Dibujo la pelota
    ventana.blit(ball, ballrect) #Obtengo el rectángulo que determina la colisión de la pelota con otros elementos (bordes, bate, ladrillos)
    pygame.display.flip() # Todos los elementos del juego se vuelven a dibujar
    pygame.time.Clock().tick(60) #Establezco la tasa de refresco del programa

pygame.quit() #Cierro el juego
