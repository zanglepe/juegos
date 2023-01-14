import pygame
 

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)
 

LARGO  = 20
ALTO = 20
 

MARGEN = 5
 


grid = []
for fila in range(10):
   
    grid.append([])
    for columna in range(10):
        grid[fila].append(0) # Añade una celda
 

grid[1][5] = 1
 

pygame.init()
  

DIMENSION_VENTANA = [255, 255]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
 

pygame.display.set_caption("Retículas y Matrices")
 
hecho = False
 

reloj = pygame.time.Clock()
 

while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            
            pos = pygame.mouse.get_pos()
            
            columna = pos[0] // (LARGO + MARGEN)
            fila = pos[1] // (ALTO + MARGEN)
           
            grid[fila][columna] = 1
            print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)
 
    
    pantalla.fill(NEGRO)
 
    
    for fila in range(10):
        for columna in range(10):
            color = BLANCO
            if grid[fila][columna] == 1:
                color = VERDE
            pygame.draw.rect(pantalla,
                             color,
                             [(MARGEN+LARGO) * columna + MARGEN,
                              (MARGEN+ALTO) * fila + MARGEN,
                              LARGO,
                              ALTO])
     
    
    reloj.tick(60)
 
    
    pygame.display.flip()
     

pygame.quit()