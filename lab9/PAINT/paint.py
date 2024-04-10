import pygame
import random

pygame.init()

#collars
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (150, 75, 0)
YELLOW = (255, 255, 102)
GRAY = (125, 125, 125)
LIGHT_BLUE = (0, 191, 255)
PINK = (255, 0, 128)
PURPLE = (128, 0, 128)
HUNTER_GREEN = (0, 100, 0)
ORANGE = (255, 165, 0)
L_GREEN = (48, 213, 200)
H_PURPLE = (66, 49, 137)

#draw collars
def colorss(screen):
    pygame.draw.rect(screen, H_PURPLE, (300, 50, 100, 50))
    h_purple = pygame.Rect(300, 50, 100, 50)

    pygame.draw.rect(screen, L_GREEN, (400, 50, 100, 50))
    l_green = pygame.Rect(400, 50, 100, 50)

    pygame.draw.rect(screen, RED, (400, 0, 100, 50))
    red = pygame.Rect(400, 0, 100, 50)

    pygame.draw.rect(screen, ORANGE, (700, 0, 100, 50))
    orange = pygame.Rect(700, 0, 100, 50)

    pygame.draw.rect(screen, HUNTER_GREEN, (600, 50, 100, 50))
    h_green = pygame.Rect(600, 50, 100, 50)

    pygame.draw.rect(screen, GREEN, (800, 0, 100, 50))
    green = pygame.Rect(800, 0, 100, 50)

    pygame.draw.rect(screen, BLUE, (600, 0, 100, 50))
    blue = pygame.Rect(600, 0, 100, 50)

    pygame.draw.rect(screen, BROWN, (500, 50, 100, 50))
    brown = pygame.Rect(500, 50, 100, 50)

    pygame.draw.rect(screen, YELLOW, (900, 0, 100, 50))
    yellow = pygame.Rect(900, 0, 100, 50)

    pygame.draw.rect(screen, BLACK, (300, 0, 100, 50))
    black = pygame.Rect(300, 0, 100, 50)

    pygame.draw.rect(screen, GRAY, (800, 50, 100, 50))
    gray = pygame.Rect(800, 50, 100, 50)

    pygame.draw.rect(screen, LIGHT_BLUE, (900, 50, 100, 50))
    li_blue = pygame.Rect(900, 50, 100, 50)

    pygame.draw.rect(screen, PINK, (700, 50, 100, 50))
    pink = pygame.Rect(700, 50, 100, 50)

    pygame.draw.rect(screen, PURPLE, (500, 0, 100, 50))
    purple = pygame.Rect(500, 0, 100, 50)

    globals().update(locals()) #for update global varible

def drawLine(screen, start, end, width, mode):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, mode, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, mode, (x, y), width)

def drawCircle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    x=(x1+x2)/2
    y=(y1+y2)/2
    radius = abs(x1-x2)/2
    pygame.draw.circle(screen, pygame.Color(color),(x,y),radius, width)

def drawRectangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    widthr=abs(x1-x2)
    height=abs(y1-y2)
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)

# a square
def drawSquare(screen, start, end, width, color):
    radius = 15
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    widths=abs(x2-x1)
    height=abs(y2-y1)
    mn=min(abs(x2-x1), abs(y2-y1))

    # right down
    if x2>x1 and y2>y1:
        pygame.draw.line(screen, pygame.Color(color), (x1,y1-radius/2.3), (x1, y1+mn), width) # левого верха до левого низа
        pygame.draw.line(screen, pygame.Color(color), (x1,y1), (x1+mn, y1), width) # левого верха до правого верха
        pygame.draw.line(screen, pygame.Color(color), (x1+mn,y1-radius/2.3), (x1+mn, y1+mn), width)  # с правого верха до правого низа
        pygame.draw.line(screen, pygame.Color(color), (x1-radius/2.3,y1+mn), (x1+mn+radius/2, y1+mn), width)   # с левого низа до правого низа

    # right up
    if y2<y1 and x2>x1:
        pygame.draw.line(screen, pygame.Color(color), (x1,y1),(x1,y1-mn), width) # левого верха до левого верха
        pygame.draw.line(screen, pygame.Color(color), (x1-radius/2.3,y1),(x1+mn,y1), width)  # левого верха до правого верха
        pygame.draw.line(screen, pygame.Color(color), (x1-radius/2.3,y1-mn),(x1+mn,y1-mn), width)  # с правого верха до правого низа
        pygame.draw.line(screen, pygame.Color(color), (x1+mn,y1+radius/2),(x1+mn,y1-mn-radius/2.3), width)  # с правого низа до левого низа

    # left up
    if x1>x2 and y1>y2:
        pygame.draw.line(screen, pygame.Color(color), (x1,y1+radius/2),(x1,y1-mn), width)  #  с правого низа до правого верха
        pygame.draw.line(screen, pygame.Color(color), (x1,y1),(x1-mn-radius/2.3,y1), width)  # с правого верха до левого верха
        pygame.draw.line(screen, pygame.Color(color), (x1-mn,y1),(x1-mn,y1-mn-radius/2.3), width)   # с левого верха до левого низа
        pygame.draw.line(screen, pygame.Color(color), (x1-mn,y1-mn),(x1+radius/2,y1-mn), width)  # с левого низа до правого низа

    # left down
    if x1>x2 and y1<y2:
        pygame.draw.line(screen, pygame.Color(color), (x1,y1-radius/2.3), (x1,y1+mn+radius/2), width)  #   с правого верха до правого низа
        pygame.draw.line(screen, pygame.Color(color), (x1,y1+mn), (x1-mn-radius/2.3,y1+mn), width)  # с правого низа до левого низа
        pygame.draw.line(screen, pygame.Color(color), (x1-mn,y1+mn), (x1-mn,y1-radius/2.3), width)   # с левого низа до левого верха
        pygame.draw.line(screen, pygame.Color(color), (x1-mn,y1), (x1,y1), width)  # с левого верха до правого верха


# RightTriangle
def drawRightTriangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    if x2 > x1 and y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)), width)

#   EquilateralTriangle
def drawEquilateralTriangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    width_b = abs(x2 - x1)
    height = (3**0.5) * width_b / 2

    if y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width)
    else:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)), width)
    
# Rhombus
def drawRhombus(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width)

def main():
    screen = pygame.display.set_mode((1000, 800))
    font = pygame.font.SysFont("Verdana", 20)

    directory = ""
    #my files
    pen = pygame.image.load(directory + "PAINT/pen.jpg")
    rubber = pygame.image.load(directory + "PAINT/rubber.jpg")

    up = pygame.image.load(directory + "PAINT/up.jpg")
    down = pygame.image.load(directory + "PAINT/down.jpg")

    save = pygame.image.load(directory + "PAINT/save.jpg")
    screen.fill(WHITE)
    mode = BLACK
    # mode = 'random'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 5

    recta = False
    cir = False
    squ = False
    rt = False
    equil = False
    rhomb = False

    f = ()
    s = ()

    while True:
        
        mx, my = pygame.mouse.get_pos()

        colorss(screen)
        #draw pen and rubber
        screen.blit(pen, (0, 0))
        screen.blit(rubber, (5, 50))
        #Rect of pen and rubber
        pe = pygame.Rect(0, 0, 50, 50)
        rub = pygame.Rect(0, 50, 50, 50)

        screen.blit(up, (50, 0))
        screen.blit(down, (50, 50))

        UP = pygame.Rect(50, 0, 50, 50)
        DOWN = pygame.Rect(50, 50, 50, 50)

        screen.blit(save, (160, 0))
        SAVE = pygame.Rect(160, 0, 100, 100)

        '''
        pygame.draw.rect(screen, BLACK, (110, 10, 40, 30), 3)
        pygame.draw.circle(screen, BLACK, (130, 75), 20, 3)

        
        REC = font.render('r', True, BLACK)
        CIR = font.render('c', True, BLACK)
        screen.blit(REC, (125, 7))
        screen.blit(CIR, (123, 57))
        '''
        com = font.render("circle-'C' rectangle-'R' square-'S' right.triangle-'Z' equilateral.triangle-'E' rhombus-'L'", True, BLACK)
        screen.blit(com, (0, 100))
        pygame.display.update()

        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return   
            #save desk
            if SAVE.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #pygame.draw.rect(screen, WHITE, (0, 0, 1000, 105))
                    pygame.image.save(screen, 'paint_new_file.png')
                    

            if h_purple.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = H_PURPLE
            if l_green.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = L_GREEN
            if orange.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = ORANGE
            if rub.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = WHITE
            if pe.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = BLACK
            if UP.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    radius += 1
            if DOWN.collidepoint((mx, my)) and radius > 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    radius -= 1
            if h_green.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = HUNTER_GREEN
            if red.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = RED
            if green.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = GREEN
            if blue.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = BLUE
            if brown.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = BROWN
            if yellow.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = YELLOW

            if black.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = BLACK
            if gray.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = GRAY
            if li_blue.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = LIGHT_BLUE
            if pink.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = PINK
            if li_blue.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = LIGHT_BLUE
            if purple.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mode = PURPLE
            #exit types
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    #pygame.draw.rect(screen, WHITE, (0, 0, 1000, 105))
                    pygame.image.save(screen, 'paint_new_file.png')
                    return
            
                if event.key == pygame.K_r:
                    recta = True
                if event.key == pygame.K_c:
                    cir = True
                if event.key == pygame.K_s:
                    squ = True
                if event.key == pygame.K_z:
                    rt = True
                if event.key == pygame.K_e:
                    equil = True
                if event.key == pygame.K_l:
                    rhomb = True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                f = pygame.mouse.get_pos()
                
                if cir == False and recta == False and squ == False and rt == False and equil == False and rhomb == False :
                    draw_on = True

            if event.type == pygame.MOUSEMOTION:
                #color = mode
                if cir == False and recta == False and squ == False and rt == False and equil == False and rhomb == False: 
                    if draw_on:
                        drawLine(screen, last_pos, event.pos, radius, mode)
                    last_pos = event.pos
                if cir == True or recta == True or squ == True or rt == True or equil == True or rhomb == True :
                    s = pygame.mouse.get_pos()
                    
            
            if event.type == pygame.MOUSEBUTTONUP:
                draw_on = False
                if recta == True:
                    drawRectangle(screen, f, s, 3, mode)
                    #pygame.draw.rect(screen, mode, (f[0], f[1], abs(f[0] - s[0]), abs(f[1] - s[1])), 3)
                    f = ()
                    s = ()
                    recta = False
                if cir == True:
                    drawCircle(screen, f, s, 3, mode)
                    #pygame.draw.circle(screen, mode, (f[0], f[1]), abs(f[0] - s[0]), 3)
                    cir = False
                    f = ()
                    s = ()
                if squ == True:
                    drawSquare(screen, f, s, 3, mode)
                    #pygame.draw.rect(screen, mode, (f[0], f[1], abs(f[0] - s[0]), abs(f[1] - s[1])), 3)
                    f = ()
                    s = ()
                    squ = False
                if rt == True:
                    drawRightTriangle(screen, f, s, 3, mode)
                    #pygame.draw.circle(screen, mode, (f[0], f[1]), abs(f[0] - s[0]), 3)
                    rt = False
                    f = ()
                    s = ()
                if equil == True:
                    drawEquilateralTriangle(screen, f, s, 3, mode)
                    #pygame.draw.rect(screen, mode, (f[0], f[1], abs(f[0] - s[0]), abs(f[1] - s[1])), 3)
                    f = ()
                    s = ()
                    equil = False
                if rhomb == True:
                    drawRhombus(screen, f, s, 3, mode)
                    #pygame.draw.circle(screen, mode, (f[0], f[1]), abs(f[0] - s[0]), 3)
                    rhomb = False
                    f = ()
                    s = ()
                

        pygame.display.flip()

    pygame.quit()

main()