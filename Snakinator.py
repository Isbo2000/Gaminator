#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Snakinator 1

import pygame, sys, time, random
from pygame.locals import *

blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
redcolour = pygame.Color(255, 0, 0)
blackcolour = pygame.Color(100, 100, 255)
whitecolour = pygame.Color(150, 255, 255)
greycolour = pygame.Color(150, 0, 150)
purple = pygame.Color(50, 50, 50)
hi = black
bi = black
hb = 0

green = pygame.Color(108,122,14)
green2 = pygame.Color(90,152,4)

ww = 900
wh = 900
cs = 20
assert ww % cs == 0, "Window width must be a multiple of cell size."
assert wh % cs == 0, "Window height must be a multiple of cell size."
cw = int(ww / cs)
ch = int(wh / cs)

def main():
    global fpsclock, playsurface, HighScore, speed, ISpeed, IS, hi, bi, hitself, hi1, hi2, hi3, hi4
    HighScore = 0
    hitself = 0
    speed = 10
    ISpeed = 0.25
    IS = 1
    hi = black
    bi = black
    hi1 = 'left'
    hi2 = 'right'
    hi3 = 'down'
    hi4 = 'up'
    
    pygame.init()
    fpsclock = pygame.time.Clock()
    playsurface = pygame.display.set_mode((900, 700))
    pygame.display.set_caption('Snakinator')
    StartScreen()
    while True:
        rungame()
        gameover()
        StartScreen()


def DrawGrid():
    for x in range(0, ww, cs): # draw vertical lines
        pygame.draw.line(playsurface, purple, (x, 0), (x, wh))
    for y in range(0, wh, cs): # draw horizontal lines
        pygame.draw.line(playsurface, purple, (0, y), (wh, y))

def score():
    rspfont = pygame.font.Font('freesansbold.ttf', 20)
    rspsurf = rspfont.render('Score: %s' % (rsp), True, black)
    rsprect = rspsurf.get_rect()
    rsprect.midtop = (100, 55)
    playsurface.blit(rspsurf, rsprect)
    
def highscore():
    rshsfont = pygame.font.Font('freesansbold.ttf', 20)
    rshssurf = rshsfont.render('High Score: %s' % (HighScore), True, black)
    rshsrect = rshssurf.get_rect()
    rshsrect.midtop = (100, 30)
    playsurface.blit(rshssurf, rshsrect)
    
def Speed():
    sfont = pygame.font.Font('freesansbold.ttf', 20)
    ssurf = sfont.render('Speed: %s' % (speed), True, black)
    srect = ssurf.get_rect()
    srect.midtop = (100, 80)
    playsurface.blit(ssurf, srect)
    

def Menu():
    global speed, ISpeed, IS, hitself
    menu = True
    while menu:
        if hitself == 0:
            lol = 'yes'
        if hitself == 1:
            lol = 'no'
        if hitself > 1:
            hitself = 0
        if hitself < 0:
            hitself = 1
        if speed > 100:
            speed = 100
        if speed < 1:
            speed = 1
        if IS > 4:
            IS = 0
        if IS < 0:
            IS = 4
        if IS == 0:
            ISpeed = 0
        if IS == 1:
            ISpeed = 0.25
        if IS == 2:
            ISpeed = 0.5
        if IS == 3:
            ISpeed = 0.75
        if IS == 4:
            ISpeed = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exec(open('Gaminator.py').read())
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    speed += 1
                if event.key == pygame.K_DOWN:
                    speed -= 1
                if event.key == pygame.K_m:
                    menu = False
                if event.key == pygame.K_RIGHT:
                    IS += 1
                if event.key == pygame.K_LEFT:
                    IS -= 1
                if event.key == pygame.K_a:
                    hitself += 1
                elif event.key == pygame.K_q:
                    playsurface.fill(blue)
                    font = pygame.font.Font('freesansbold.ttf', 75)
                    text = font.render("Thanks for playing! :)", True, black)
                    rect = text.get_rect()
                    rect.midtop = (450, 275)
                    playsurface.blit(text, rect)
                    pygame.display.flip()
                    time.sleep(1)
                    exec(open('Gaminator.py').read())
                    pygame.quit()
                    sys.exit()
        playsurface.fill(black)
        font = pygame.font.Font('freesansbold.ttf', 140)
        text = font.render("Menu", True, white)
        rect = text.get_rect()
        rect.midtop = (450, 25)
        playsurface.blit(text, rect)
        sfont = pygame.font.Font('freesansbold.ttf', 60)
        ssurf = sfont.render('Speed: %s' % (speed), True, white)
        srect = ssurf.get_rect()
        srect.midtop = (450, 200)
        playsurface.blit(ssurf, srect)
        font2 = pygame.font.Font('freesansbold.ttf', 25)
        text2 = font2.render("Use the up and down arrows to change the speed.", True, white)
        rect2 = text2.get_rect()
        rect2.midtop = (450, 275)
        playsurface.blit(text2, rect2)
        font3 = pygame.font.Font('freesansbold.ttf', 45)
        text3 = font3.render('Increase Speed Interval: %s' % (ISpeed), True, white)
        rect3 = text3.get_rect()
        rect3.midtop = (450, 350)
        playsurface.blit(text3, rect3)
        font4 = pygame.font.Font('freesansbold.ttf', 20)
        text4 = font4.render("Use the right and left arrows to change the increase speed interval", True, white)
        rect4 = text4.get_rect()
        rect4.midtop = (450, 410)
        playsurface.blit(text4, rect4)
        font3 = pygame.font.Font('freesansbold.ttf', 45)
        text3 = font3.render('Self collisions?: %s' % (lol), True, white)
        rect3 = text3.get_rect()
        rect3.midtop = (450, 450)
        playsurface.blit(text3, rect3)
        font4 = pygame.font.Font('freesansbold.ttf', 20)
        text4 = font4.render("Use the 'a' key to change yes or no", True, white)
        rect4 = text4.get_rect()
        rect4.midtop = (450, 510)
        playsurface.blit(text4, rect4)
        pygame.display.update()
        fpsclock.tick(5)
def StartScreen():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    Menu()
                if event.key == pygame.K_SPACE:
                    start = False
                elif event.key == pygame.K_q:
                    playsurface.fill(blue)
                    font = pygame.font.Font('freesansbold.ttf', 75)
                    text = font.render("Thanks for playing! :)", True, black)
                    rect = text.get_rect()
                    rect.midtop = (450, 275)
                    playsurface.blit(text, rect)
                    pygame.display.flip()
                    time.sleep(1)
                    exec(open('Gaminator.py').read())
                    pygame.quit()
                    sys.exit()
        playsurface.fill(blackcolour)
        font = pygame.font.Font('freesansbold.ttf', 35)
        text = font.render("Use the arrow keys or 'w', 's', 'a', or 'd' to move.", True, black)
        rect = text.get_rect()
        rect.midtop = (450, 275)
        playsurface.blit(text, rect)
        font2 = pygame.font.Font('freesansbold.ttf', 35)
        text2 = font2.render("Press 'p' to pause.", True, black)
        rect2 = text2.get_rect()
        rect2.midtop = (450, 325)
        playsurface.blit(text2, rect2)
        font3 = pygame.font.Font('freesansbold.ttf', 35)
        text3 = font3.render("Press the space key to start playing.", True, black)
        rect3 = text3.get_rect()
        rect3.midtop = (450, 550)
        playsurface.blit(text3, rect3)
##        font4 = pygame.font.Font('freesansbold.ttf', 40)
##        text4 = font4.render("Hi.", True, black)
##        rect4 = text4.get_rect()
##        rect4.midtop = (450, 30)
##        playsurface.blit(text4, rect4)
        font5 = pygame.font.Font('freesansbold.ttf', 70)
        text5 = font5.render("Snakinator.", True, black)
        rect5 = text5.get_rect()
        rect5.midtop = (450, 60)
        playsurface.blit(text5, rect5)
        font6 = pygame.font.Font('freesansbold.ttf', 35)
        text6 = font6.render("Press 'q' to Quit.", True, black)
        rect6 = text6.get_rect()
        rect6.midtop = (450, 375)
        playsurface.blit(text6, rect6)
        font7 = pygame.font.Font('freesansbold.ttf', 30)
        text7 = font7.render("Press 'm' for the Menu", True, black)
        rect7 = text7.get_rect()
        rect7.midtop = (450, 425)
        playsurface.blit(text7, rect7)
        font8 = pygame.font.Font('freesansbold.ttf', 25)
        text8 = font8.render("Your goal is to eat the red blocks to gain points", True, black)
        rect8 = text8.get_rect()
        rect8.midtop = (450, 175)
        playsurface.blit(text8, rect8)
                
        
        pygame.display.update()
        fpsclock.tick(5)
        


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exec(open('Gaminator.py').read())
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                if event.key == pygame.K_m:
                    Menu()
                elif event.key == pygame.K_q:
                    playsurface.fill(blue)
                    font = pygame.font.Font('freesansbold.ttf', 75)
                    text = font.render("Thanks for playing! :)", True, black)
                    rect = text.get_rect()
                    rect.midtop = (450, 275)
                    playsurface.blit(text, rect)
                    pygame.display.flip()
                    time.sleep(1)
                    exec(open('Gaminator.py').read())
                    pygame.quit()
                    sys.exit()
        playsurface.fill(white)
        font = pygame.font.Font('freesansbold.ttf', 175)
        font2 = pygame.font.Font('freesansbold.ttf', 45)
        text = font.render("Paused", True, black)
        text2 = font2.render("Press P to continue or Q to quit.", True, black)
        rect = text.get_rect()
        rect.midtop = (450, 200)
        rect2 = text2.get_rect()
        rect2.midtop = (450, 400)
        playsurface.blit(text, rect)
        playsurface.blit(text2, rect2)
        score()
        highscore()
        Speed()
        pygame.display.update()
        fpsclock.tick(5)
def gameover():
    for event in pygame.event.get():
        if event.key == pygame.K_q:
            playsurface.fill(blue)
            font = pygame.font.Font('freesansbold.ttf', 75)
            text = font.render("Thanks for playing! :)", True, black)
            rect = text.get_rect()
            rect.midtop = (450, 275)
            playsurface.blit(text, rect)
            pygame.display.flip()
            time.sleep(2)
            exec(open('Gaminator.py').read())
            pygame.quit()
            sys.exit()
    DrawGrid()
    score()
    highscore()
    Speed()
    gameoverfont = pygame.font.Font('freesansbold.ttf', 165)
    gameoversurf = gameoverfont.render('Game Over', True, greycolour)
    gameoverrect = gameoversurf.get_rect()
    gameoverrect.midtop = (450, 225)
    playsurface.blit(gameoversurf, gameoverrect)
    pygame.display.flip()
    time.sleep(1.5)
    return
def IncreaseSpeed():
    global ISpeed, speed
    if ISpeed == 0:
        speed += 0
    elif ISpeed == 0.25:
        speed += 0.25
    elif ISpeed == 0.5:
        speed += 0.5
    elif ISpeed == 0.75:
        speed += 0.75
    elif ISpeed == 1:
        speed += 1

def rungame():
    global rsp, HighScore, speed, ISpeed, hitself, hi1, hi2, hi3, hi4
    hi = black
    bi = black
    rsp = 0
    speed = 10

    snakeposition = [100,100]
    snakesegments= [[100,100],[80,100],[60,100]]
    raspberryposition = [300,300]
    raspberryspawned = 1
    direction = 'right'
    changedirection = direction
    while True:
        hi = black
        bi = black
        if hitself == 0:
            hi1 = 'left'
            hi2 = 'right'
            hi3 = 'down'
            hi4 = 'up'
        else:
            hi1 = 'left1'
            hi2 = 'right1'
            hi3 = 'down1'
            hi4 = 'up1'
        for event in pygame.event.get():
            if event.type == QUIT:
                exec(open('Gaminator.py').read())
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == ord('d'):
                    changedirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changedirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changedirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changedirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_m:
                    Menu()
                if event.key == pygame.K_r:
                    return
                elif event.key == pygame.K_q:
                    playsurface.fill(blue)
                    font = pygame.font.Font('freesansbold.ttf', 75)
                    text = font.render("Thanks for playing! :)", True, black)
                    rect = text.get_rect()
                    rect.midtop = (450, 275)
                    playsurface.blit(text, rect)
                    pygame.display.flip()
                    time.sleep(1)
                    exec(open('Gaminator.py').read())
                    pygame.quit()
                    sys.exit()
        if changedirection == 'right' and not direction == hi1:
            direction = changedirection
        if changedirection == 'left' and not direction == hi2:
            direction = changedirection  
        if changedirection == 'up' and not direction == hi3:
            direction = changedirection
        if changedirection == 'down' and not direction == hi4:
            direction = changedirection
        if direction == 'right':
            snakeposition[0] += 20
        if direction == 'left':
            snakeposition[0] -= 20
        if direction == 'up':
            snakeposition[1] -= 20
        if direction == 'down':
            snakeposition[1] += 20
        snakesegments.insert(0,list(snakeposition))
        if snakeposition[0] == raspberryposition[0]:
            bi = redcolour
        if snakeposition[1] == raspberryposition[1]:
            bi = redcolour
        if snakeposition[0] == raspberryposition[0] and snakeposition[1] == raspberryposition[1]:
            raspberryspawned = 0
            rsp += 1
            IncreaseSpeed()
            hi = redcolour
            
        else:
            snakesegments.pop()
            #hi = black
        if HighScore < rsp:
            HighScore = rsp

        if raspberryspawned == 0:
            hi = redcolour
            x = random.randrange(1,32)
            y = random.randrange(1,24)
            raspberryposition = [int(x*20),int(y*20)]
        raspberryspawned = 1
        playsurface.fill(blackcolour)
        for position in snakesegments:
            pygame.draw.rect(playsurface,bi,Rect(snakeposition[0], snakeposition[1], 20,5))
            pygame.draw.rect(playsurface,whitecolour,Rect(snakeposition[0], snakeposition[1], 16,15))
            pygame.draw.rect(playsurface,hi,Rect(snakeposition[0], snakeposition[1], 16,15))
            pygame.draw.rect(playsurface,whitecolour,Rect(snakeposition[0], snakeposition[1], 16,9))
            pygame.draw.rect(playsurface,whitecolour,Rect(snakeposition[0], snakeposition[1], 5,20))
            pygame.draw.rect(playsurface,bi,Rect(snakeposition[0], snakeposition[1], 5,5))
            pygame.draw.rect(playsurface,whitecolour,Rect(position[0], position[1], 20,20))
            pygame.draw.rect(playsurface,redcolour,Rect(raspberryposition[0], raspberryposition[1], 20,20))
            #pygame.display.flip()

          #can hit walls
##        if snakeposition[0] > 900:
##            snakeposition[0] = 0
##            changedirection = 'right'
##        if snakeposition[0] < 0:
##            snakeposition[0] = 900
##            changedirection = 'left'
##        if snakeposition[1] > 700:
##            snakeposition[1] = 0
##            changedirection = 'down'
##        if snakeposition[1] < 0:
##            snakeposition[1] = 700
##            changedirection = 'up'

        #cant hit walls
        if snakeposition[0] > 900 or snakeposition[0] < 0:
            return
        if snakeposition[1] > 700 or snakeposition[1] < 0:
            return
            
        if hitself == 0:
            for snakebody in snakesegments[1:]:
                if snakeposition[0] == snakebody[0] and snakeposition[1] == snakebody[1]:
                    return
        
        DrawGrid()
       
        Speed()
      
        score()
    
        highscore()
        pygame.display.update()
        fpsclock.tick(speed)
if __name__ == '__main__':
    main()
