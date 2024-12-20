from time import *
from math import *

import os
import pygame

tile=64
LONG,LARG=tile*10,tile*10

pygame.init()
fenetre = pygame.display.set_mode((LONG, LARG))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)
frequence = pygame.time.Clock()

fond=pygame.image.load('')


data_file=''

lst = {}

table = []

def map():
    fenetre.blit(fond,(tile,tile))
    for y in range(10):
        for x in range(10):
            if table[y*10+x] != 0 and table[y*10+x] < 50:
                fenetre.blit(lst[table[y*10+x]],((x+1)*tile,(y+1)*tile))
            elif table[y*8+x] > 50:
                fenetre.blit(lst[table[y*10+x]-50],((x+1)*tile,(y+1)*tile))
                fenetre.blit(lst[25],((x+1)*tile,(y+1)*tile))

def get_data(filename):
    file=open(filename)
    content=file.read()
    file.close()
    return content

def set_data(filename,string=''):
    file=open(filename,'w')
    file.write(str(string))
    file.close()
    return get_data(filename)

def thisIsATable(filename=data_file):
    content=get_data(filename)
    table=[]; ctr=''
    for i in content:
        if i == ',': table.append(int(ctr)); ctr=''
        elif i == '\n': pass
        else: ctr+=i
    return table

def txt():
    data=''
    for y in range(10):
        for x in range(10):
            data+=str(table[y*10+x])+','
        data+='\n'
    return data

def Btw(n,m):
    if 0 <= n < 10 and 0 <= m < 10: return True
    else: return False

set_data(data_file,txt())

loop=True
pion=0
qt_pion=1
memx,memy=0,0
oldx,oldy=0,0

while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        pos_x,pos_y=pygame.mouse.get_pos()
        pos_x,pos_y=pos_x-tile,pos_y-tile
        """
        Logic's game
        """
        map()

    # Actualisation de l'affichage
    frequence.tick(60)
    pygame.display.update()
pygame.quit()