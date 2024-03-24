import pygame

pygame.init()


x = 300
y = 300

screen = pygame.display.set_mode((600,600))

clock = pygame.time.Clock()    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()  

    if pressed[pygame.K_UP]:
        y = max(25, y - 20)
    elif pressed[pygame.K_DOWN]:
        y = min(575, y + 20)
    elif pressed[pygame.K_RIGHT]:
        x = min(575, x + 20)
    elif pressed[pygame.K_LEFT]:
        x = max(25, x - 20)  

    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0), (x,y), 25)        
       
    clock.tick(60)
    pygame.display.flip()