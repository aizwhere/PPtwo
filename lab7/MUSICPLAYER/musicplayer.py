import pygame

pygame.init()

clock = pygame.time.Clock()


W = 40*9
H = 40*16

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Aiz's music player")

background = pygame.transform.scale(pygame.image.load('MUSICPLAYER/bg.png'), (W, H))
icon_img = pygame.image.load('MUSICPLAYER/icon.png')
pygame.display.set_icon(icon_img) 



pos = 0 
songs = ('MUSICPLAYER/song1.mp3',
         'MUSICPLAYER/song2.mp3',
         'MUSICPLAYER/song3.mp3',
         'MUSICPLAYER/song4.mp3',
         'MUSICPLAYER/song5.mp3',
)
covers_seq = ('MUSICPLAYER/1.jpeg',
          'MUSICPLAYER/2.jpeg', 
          'MUSICPLAYER/3.jpg',
          'MUSICPLAYER/4.jpg',
          'MUSICPLAYER/5.webp'   
)

pygame.mixer.music.load(songs[pos])
pygame.mixer.music.play()

size_cover = 280
covers = pygame.transform.scale(pygame.image.load(covers_seq[pos]), (size_cover, size_cover))

play_button = pygame.transform.scale(pygame.image.load('play.png'), (60, 60))
pause_button = pygame.transform.scale(pygame.image.load('pause.png'), (60, 60))

record = True
x = 0 


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

             
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_RIGHT]:
        x = 0
        pos = (pos + 1) % len(songs)
        pygame.mixer.music.load(songs[pos])
        pygame.mixer.music.play()
        covers = pygame.transform.scale(pygame.image.load(covers_seq[pos]), (size_cover, size_cover))

    if pressed[pygame.K_LEFT]:
        x = 0
        pos = (pos - 1) % len(songs)
        pygame.mixer.music.load(songs[pos])
        pygame.mixer.music.play()
        covers = pygame.transform.scale(pygame.image.load(covers_seq[pos]), (size_cover, size_cover))

    if pressed[pygame.K_SPACE]:
        record = not record
        if record:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
       
    screen.blit(background, (0, 0))

    screen.blit(covers, (W/2 - size_cover/2, H/8)) 

    pygame.draw.rect(screen, (192,192,192), (W/2 - size_cover/2, 400, size_cover, 20))
    if record:
        x += 0.1
        if x > size_cover:
            x = 0

    pygame.draw.rect(screen, (0,0,51), (W/2 - size_cover/2, 400, x, 20))
    
    if record:
        screen.blit(pause_button, (W/2 - 30 , 450))
    else:
        screen.blit(play_button, (W/2 - 30, 450))         

         


    
    
    

    pygame.display.update()       
    clock.tick(10) 