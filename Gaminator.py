#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, time, random
from pygame.locals import *

grey = pygame.Color(35,35,35)
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
whitea = pygame.Color(45,45,45)
whiteb = pygame.Color(65,65,65)
whitec = pygame.Color(85,85,85)
whited = pygame.Color(105,105,105)
whitee = pygame.Color(125,125,125)
whitef = pygame.Color(145,145,145)
whiteg = pygame.Color(165,165,165)
whiteh = pygame.Color(185,185,185)
whitei = pygame.Color(205,205,205)
whitej = pygame.Color(225,225,225)
whitek = pygame.Color(245,245,245)


pygame.init()
fpsclock = pygame.time.Clock()
playsurface = pygame.display.set_mode((900, 700))
pygame.display.set_caption('Gaminator')



while True:
    playsurface.fill(grey)
    font = pygame.font.Font('freesansbold.ttf', 140)
    text = font.render("Games", True, white)
    rect = text.get_rect()
    rect.midtop = (450, 25)
    playsurface.blit(text, rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                while True:
                    playsurface.fill(whitea)
                    pygame.display.flip()
                    time.sleep(0.05)
                    playsurface.fill(whiteb)
                    pygame.display.flip()
                    time.sleep(0.05)
                    playsurface.fill(whitec)
                    pygame.display.flip()
                    time.sleep(0.05)
                    playsurface.fill(whited)
                    pygame.display.flip()
                    time.sleep(0.05)
                    playsurface.fill(whitee)
                    pygame.display.flip()
                    time.sleep(0.05)
                    playsurface.fill(whitef)
                    pygame.display.flip()
                    time.sleep(0.05)
                    playsurface.fill(whiteg)
                    pygame.display.flip()
                    time.sleep(0.05)
                    playsurface.fill(whiteh)
                    pygame.display.flip()
                    time.sleep(0.05)
                    playsurface.fill(whitei)
                    pygame.display.flip()
                    time.sleep(0.05)
                    playsurface.fill(whitej)
                    pygame.display.flip()
                    time.sleep(0.05)
                    playsurface.fill(whitek)
                    pygame.display.flip()
                    time.sleep(0.05)
                    playsurface.fill(white)
                    pygame.display.flip()
                    time.sleep(0.5)
                    pygame.quit()
                    sys.exit()
    image = pygame.image.load(r'C:\Gaminator\Snakinator1.png')
    image1 = pygame.image.load(r'C:\Gaminator\Snakinator1MO.png')
    tx = 150
    bx = 615
    ty = 200
    by = 323
    
    
    
    #pygame.draw.rect(playsurface, grey, Rect(150,200, 200, 123))
    playsurface.blit(image, (150,200))
    x, y = pygame.mouse.get_pos()
    if x > tx and x < bx and y > ty and y < by:
        font = pygame.font.Font('freesansbold.ttf', 45)
        text = font.render("Snakinator", True, white)
        rect = text.get_rect()
        rect.midtop = (515, 200)
        playsurface.blit(text, rect)
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Eat red dots, gain points", True, white)
        rect = text.get_rect()
        rect.midtop = (515, 250)
        playsurface.blit(text, rect)

        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("CLICK TO PLAY", True, white)
        rect = text.get_rect()
        rect.midtop = (515, 285)
        playsurface.blit(text, rect)
        
        playsurface.blit(image1, (140,190))
        #event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x > tx and x < bx and y > ty and y < by:
                if event.button == 1:
                    exec(open('Snakinator.py').read())
    else:
        font = pygame.font.Font('freesansbold.ttf', 45)
        text = font.render("Snakinator", True, white)
        rect = text.get_rect()
        rect.midtop = (485, 200)
        playsurface.blit(text, rect)

        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("CLICK TO PLAY", True, white)
        rect = text.get_rect()
        rect.midtop = (485, 285)
        playsurface.blit(text, rect)
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Eat red dots, gain points", True, white)
        rect = text.get_rect()
        rect.midtop = (485, 250)
        playsurface.blit(text, rect)


    mage = pygame.image.load(r'C:\Gaminator\Snakinator1.png')
    mage1 = pygame.image.load(r'C:\Gaminator\Snakinator1MO.png')
    qtx = 150
    qbx = 850
    qty = 350
    qby = 473
    
    
    
    #pygame.draw.rect(playsurface, grey, Rect(150,350, 200, 123))
    playsurface.blit(mage, (150,350))
    qx, qy = pygame.mouse.get_pos()
    if qx > qtx and qx < qbx and qy > qty and qy < qby:
        font = pygame.font.Font('freesansbold.ttf', 45)
        text = font.render("Snakinator 2 ~ Rottin", True, white)
        rect = text.get_rect()
        rect.midtop = (630, 350)
        playsurface.blit(text, rect)
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Eat red dots, gain points, avoid rotting squares", True, white)
        rect = text.get_rect()
        rect.midtop = (630, 400)
        playsurface.blit(text, rect)

        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("CLICK TO PLAY", True, white)
        rect = text.get_rect()
        rect.midtop = (630, 435)
        playsurface.blit(text, rect)
        
        playsurface.blit(mage1, (140,340))
        #event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if qx > qtx and qx < qbx and qy > qty and qy < qby:
                if event.button == 1:
                    exec(open('Snakinator2 - Rottin.py').read())
    else:
        font = pygame.font.Font('freesansbold.ttf', 45)
        text = font.render("Snakinator 2 ~ Rottin", True, white)
        rect = text.get_rect()
        rect.midtop = (600, 350)
        playsurface.blit(text, rect)

        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("CLICK TO PLAY", True, white)
        rect = text.get_rect()
        rect.midtop = (600, 435)
        playsurface.blit(text, rect)
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Eat red dots, gain points, avoid rotting squares", True, white)
        rect = text.get_rect()
        rect.midtop = (600, 400)
        playsurface.blit(text, rect)
        
    fpsclock.tick(10)
    pygame.display.flip()
