import pygame

pygame.init()

W = 600
H = 600
v = 20#pixels
R = 25
screen = pygame.display.set_mode((W,H))

clock = pygame.time.Clock()

x = 300
y = 300
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()  

    if pressed[pygame.K_UP]:
        y = max(R, y - v)

    elif pressed[pygame.K_DOWN]:
        y = min(H - R, y + v)

    elif pressed[pygame.K_RIGHT]:
        x = min(W - R, x + v)

    elif pressed[pygame.K_LEFT]:
        x = max(R, x - v)  

    screen.fill((255,255,255))    

    pygame.draw.circle(screen, (255,0,0), (x,y), R)        
       
    clock.tick(60)
    
    pygame.display.update()