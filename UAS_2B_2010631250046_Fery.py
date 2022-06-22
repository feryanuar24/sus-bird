#1. mengimpor library
import pygame, random, time, sys

#2. menginisialisasi permainan
pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((700,700))
print("Flappy Sus")
pygame.display.set_caption('Flappy Sus')
font, font2, font3 = pygame.font.SysFont('Helvetica', 70), pygame.font.SysFont('Helvetica', 35), pygame.font.SysFont('Helvetica', 15)
title = font.render('Flappy Sus', True, (0,0,255))
caption = font2.render('Tekan Spasi Untuk Mulai dan Bergerak', True, (0,255,0))
wm = font3.render('Oleh: Fery  Anuar', True, (0,0,0))

#3. memuat aset game
#3.1. memuat gambar
pygame.display.set_icon(pygame.image.load("image/trashcan.jpg"))
bg = pygame.image.load("image/bg.jfif")
nobird = pygame.image.load("image/start.png")
bird = pygame.image.load("image/sus.png")
bird_dead = pygame.image.load("image/end.png")
#3.2. memuat audio
bgm = pygame.mixer.Sound("sound/bgm.mp3")
bgm.set_volume(0.5)

#4. loop permainan
global start, vel, ypos, hscore, p1, p2, tscore, died
start = False
vel = 0
ypos = 300
hscore = 0
pipe = [700,random.randint(0,350)]
tscore = 0
died = False
while True:

    #5. memberi warna layar
    window.fill((252,182,193))

    #6. menggambar objek permainan
    window.blit(nobird, (100, 500))
    window.blit(wm,(600,680))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start == False:
                    ypos = 300
                    start = True
                vel = 7.
    if start:
        window.blit(bg,(0,0))
        window.blit(bird,(50,ypos))
        bgm.play()
        ypos = ypos - vel
        vel = vel - 0.5
        pygame.draw.rect(window,(0,0,0),(pipe[0],0,50,pipe[1]))
        pygame.draw.rect(window,(0,0,0),(pipe[0],pipe[1]+300,50,720))
        window.blit(font2.render('Score: ' + str(tscore), True, (255,255,255)),(10,10))
        pipe[0] = pipe[0] - 5
        if pipe[0] < -50:
            pipe[0] = 720
            pipe[1] = random.randint(0,380)
            tscore = tscore + 1
            if tscore > hscore:
                hscore = tscore
    else:
        if died:
            window.blit(bird_dead,(100,500))
        window.blit(title,(100,100))
        window.blit(caption,(100,300))
        window.blit(font2.render('Skor Tertinggi= ' + str(hscore), True, (255,0,0), None),(100,400))
    if (pipe[0] < 164 and pipe[0] > 14) and (ypos+192 > pipe[1]+300 or ypos < pipe[1]):
        ypos = 528
    if ypos >= 528:
        ypos = 528
        caption = font2.render('Kamu Kalah', True, (0,255,0), None)
        start = False
        tscore = 0
        pipe[0] = 720
        died = True
    elif ypos < 0:
        ypos = 0
        vel = -abs(vel)
    clock.tick(60)
    if time.time() - int(time.time()) < 0.02 and int(time.time()) % 5 == 0:
        print("FPS: " + str(int(clock.get_fps())))

    #7. memperbaharui layar
    pygame.display.flip()

    #8. event loop
    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)