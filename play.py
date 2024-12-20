from time import *
from math import *

import os
import pygame

tile=64
LONG,LARG=tile*12,tile*12

pygame.init()
fenetre = pygame.display.set_mode((LONG, LARG))
pygame.display.set_caption("Jeu de dames")
font = pygame.font.Font('freesansbold.ttf', 20)
frequence = pygame.time.Clock()

fond=pygame.image.load('textures/damier.png')

pion_blanc=pygame.image.load('textures/blanc-pion.png')
dame_blanc=pygame.image.load('textures/blanc-dame.png')
pion_noir =pygame.image.load('textures/noir-pion.png')
dame_noir =pygame.image.load('textures/noir-dame.png')

pos=pygame.image.load('textures/possibility.png')
superpos=pygame.image.load('textures/superpos.png')

data_file='dames_table.csv'

lst = {1:pion_blanc,2:dame_blanc,
       5:pion_noir, 6:dame_noir,
       21:pos,25:superpos}

table = [
    1,0,1,0,1,0,1,0,1,0,
    0,1,0,1,0,1,0,1,0,1,
    1,0,1,0,1,0,1,0,1,0,
    0,1,0,1,0,1,0,1,0,1,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    5,0,5,0,5,0,5,0,5,0,
    0,5,0,5,0,5,0,5,0,5,
    5,0,5,0,5,0,5,0,5,0,
    0,5,0,5,0,5,0,5,0,5,
]

# """
def map():
    fenetre.blit(fond,(tile,tile))
    for y in range(10):
        for x in range(10):
            if table[y*10+x] != 0 and table[y*10+x] < 10:
                fenetre.blit(lst[table[y*10+x]],((x+1)*tile,(y+1)*tile))
            elif table[y*10+x] > 10 and table[y*10+x] != 21:
                fenetre.blit(lst[table[y*10+x]-10],((x+1)*tile,(y+1)*tile))
                fenetre.blit(lst[25],((x+1)*tile,(y+1)*tile))
            elif table[y*10+x] == 21:
                fenetre.blit(lst[21],((x+1)*tile,(y+1)*tile))
# """

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

"""
class Pion:
    def __init__(self,nb:int,color:str,pos_x:int,pos_y:int):
        self.nb = nb
        self.color = color
        self.dame = False
        self.x = pos_x
        self.y = pos_y
        if self.color == 'black' and self.x == 0: self.dame = True; self.nb = 2
        elif self.color == 'white' and self.y == 9: self.dame = True; self.nb = 6
    
    def canMove(self):
        can = [(self.x,self.y)]
        mov = [(1,1),(-1,1)]
        if self.color == 'black':
            for i in mov:
                (x,y)=i
                if 0 <= self.x+x < 10:
                    can.append((self.x-x,self.y+y))
        elif self.color == 'white':
            for i in mov:
                (x,y)=i
                if 0 <= self.x+x < 10:
                    can.append((self.x+x,self.y+y))
        return can
    
    def draw(self,moves):
        for i in moves:
            (x,y)=i
            if x == self.x and y == self.y: nb=self.nb
            else: nb=10
            fenetre.blit(lst[nb],((x+1*tile),(y+1)*tile))
# """

def whereCanMove(x:int,y:int,nb:int):
    possibility=[]
    if nb == 1: 
        if Btw(x-1,y+1):
            possibility.append(x-1,y+1)
        if Btw(x+1,y+1):
            possibility.append(x+1,y+1)
    elif nb == 5: possibility=[(x-1,y-1),(x+1,y-1)]
    return possibility 

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
        pos_x1,pos_y1=pygame.mouse.get_pos()
        pos_x,pos_y=(pos_x1-tile)//tile,(pos_y1-tile)//tile
        """
        Logic's game
        """
        if pygame.mouse.get_pressed()[0]:
            if pion == 0:
                pion=table[pos_x+pos_y*10]
                table[pos_x+pos_y*10]=0
                lzt=whereCanMove(pos_x,pos_y,pion)
                for i in lzt:
                    (x,y)=i
                    if table[x+y*10] == 0: table[x+y*10]=21
                    elif pion < 5 and table[x+y*10] >= 5: table[x+y*10]+=10
                    elif pion >= 5 and table[x+y*10] < 5: table[x+y*10]+=10
            else: print(f'Try again')
        if pygame.mouse.get_pressed()[2]:
            if pos_x % 2 == pos_y % 2 and pion != 0 and table[pos_x+pos_y*10] >= 10:
                table[pos_y*10+pos_x]=pion
                pion=0
                qt_pion+=1
            else: print(f'Try again')
        if qt_pion % 2 == 0: texte = font.render(f'Au tour des Noirs', True, (255, 255, 255))
        else: texte = font.render(f'Au tour des Blancs', True, (255, 255, 255))
        pygame.draw.rect(fenetre, (0,0,0), (0,0,10*tile,tile),0)
        fenetre.blit(texte,(10,10))
        
        map()

    # Actualisation de l'affichage
    frequence.tick(60)
    pygame.display.update()
pygame.quit()