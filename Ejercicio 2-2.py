import pygame #Importo la librería "pygame"

pygame.init() #Inicio "pygame"
ventana = pygame.display.set_mode((600,500)) #Establece el tamaño de la ventana
pygame.display.set_caption("Kripto War") #Establece el nombre de la ventana

ball = pygame.image.load("dogecoin-logo2.png") # Creo el objeto pelota
ballrect = ball.get_rect() #Obtengo el rectángulo que determina la colisión de la pelota con otros elementos (bordes, bate, ladrillos)
speed = [5,5] #Establezco la velocidad inicial de la pelota
ballrect.move_ip(300,100) #Coloco la pelota en la posición inicial

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("fuet.png")
baterect = bate.get_rect()

# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(240,400)

jugando = True #Establezco variable en verdadero
while jugando: #Establezco el bucle
    for event in pygame.event.get(): #Establezco la variable a la que afecta la condición
        if event.type == pygame.QUIT: #Establezco la condicion
            jugando = False #Establezco variable en falso

    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed() #Establezco una variable con la función detectar la tecla pulsada
    if keys[pygame.K_LEFT]: # Establezco la condición para mover el bate a la izquierda
        baterect = baterect.move(-6,0) #Muevo el bate a la izquierda
    if keys[pygame.K_RIGHT]: #Establezco la condición para mover el bate a la derecha
        baterect = baterect.move(6,0) #Muevo el bate a la derecha

    # Compruebo si hay colisión
    if baterect.colliderect(ballrect): #Establezco la condición para cambiar la dirección de la pelota
        speed[1] = -speed[1] #Cambio la dirección de la pelota
    ballrect = ballrect.move(speed) # Establezco una variable con la función detectar el movimiento de la pelota
    if ballrect.left < 0 or ballrect.right > ventana.get_width(): #Establezco las condiciones para cambiar la dirección de la pelota en el borde izquierdo y derecho
        speed[0] = -speed[0] #Cambio la dirección de la pelota
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height(): #Establezco las condiciones para cambiar la dirección de la pelota en el borde superior e inferior
        speed[1] = -speed[1] #Cambio la dirección de la pelota
    ventana.fill((119, 158, 203)) #Establezco el color de fondo de la pantalla
    ventana.blit(ball, ballrect)

    # Dibujo el bate
    ventana.blit(bate, baterect) #Obtengo el rectángulo que determina la colisión del bate con otros elementos (pelota, bordes)
    pygame.display.flip() # Todos los elementos del juego se vuelven a dibujar
    pygame.time.Clock().tick(60) #Establezco la tasa de refresco del programa

pygame.quit() #Cierro el juego
