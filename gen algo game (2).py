#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Packages and dependancies

import sys
import random
import math
import pygame
pygame.init()


# In[2]:


# Basic Pygame attributes

size = width, height = 400, 600

black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


# In[3]:


# Useful functions for Walls class

def horizontalPoint(side):
    
    # Returns list of points on side
    
    tempList = []
    
    tempX = side[0][0]
    
    for i in range(side[0][0], side[1][0] + 1):
        
        tempList.insert(len(tempList), (tempX, side[0][1]))
        tempX += 1
    
    return tempList


def verticlePoint(side):
    
    # Returns list of points on side
    
    tempList = []
    
    tempY = side[0][1]
    
    for i in range(side[0][1], side[1][1] + 1):
        
        tempList.insert(len(tempList), (side[0][0], tempY))
        tempY += 1
    
    return tempList


# In[4]:


# Class for creating walls, obbjective and anything related

targetPos = ()

walls = []

class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 40, 40)
        
        self.xCent = pos[0]+19
        self.yCent = pos[1]+19
        
        self.UL_corner = (self.xCent-15, self.yCent+15)
        self.UR_corner = (self.xCent+15, self.yCent+15)
        self.BR_corner = (self.xCent+15, self.yCent-15)
        self.BL_corner = (self.xCent-15, self.yCent-15)

        self.top = (self.UL_corner, self.UR_corner)
        self.left = (self.BL_corner, self.UL_corner)
        self.bottom = (self.BL_corner, self.BR_corner)
        self.right = (self.BR_corner, self.UR_corner)
        
        self.topList = horizontalPoint(self.top)
        self.bottomList = horizontalPoint(self.bottom)
        self.leftList = verticlePoint(self.left)
        self.rightList = verticlePoint(self.right)

    def get_UL_corner(self):
        return self.UL_corner

    def get_UR_corner(self):
        return self.UR_corner

    def get_BR_corner(self):
        return self.BR_corner

    def get_BL_corner(self):
        return self.BL_corner

    def get_topList(self):
        return self.topList

    def get_bottomList(self):
        return self.bottomList

    def get_leftList(self):
        return self.leftList

    def get_rightList(self):
        return self.rightList
        
        
wallString = [
    'WWWWWWWWWW',
    'W   E    W',
    'W        W',
    'W  WW WW W',
    'W  W     W',
    'W        W',
    'W WW WWW W',
    'W      W W',
    'W        W',
    'W        W',
    'W        W',
    'W WW  WW W',
    'W        W',
    'W        W',
    'WWWWWWWWWW'
]

dx = dy = 0
for row in wallString:
    for col in row:
        if col == "W":
            Wall((dx, dy))
        if col == "E":
            end_rect = pygame.Rect(dx + 20, dy, 40, 40)
            targetPos = (dx + 20, dy)
        dx += 40
    dy += 40
    dx = 0


# In[5]:


# Functions for the "Player" class to fill in data
    

def midpoint(side):
    
    # Finds midpoint using midpoint formula and returns as (x, y)
    
    return (round((side[0][0] + side[1][0])/2), round((side[0][1] + side[1][1])/2))


'''Function for finding distance'''

def distLeft(middlePoint, walls):
    
    # Returns the distance to the nearest obstruction on a given side
    
    listOfCoords = []

    for i in walls:
        for n in i.rightList:
            if middlePoint[1]-20 < n[1] < middlePoint[1]+20 and n[0] < middlePoint[0]:
                listOfCoords.insert(len(listOfCoords), n)
    nearest = max(listOfCoords)
    
    return round(math.sqrt(((nearest[0] - middlePoint[0]) ** 2) + ((nearest[1] - middlePoint[1]) ** 2)))


def distFront(middlePoint, walls):
    
    # Returns the distance to the nearest obstruction on a given side
    
    listOfCoords = []
    for i in walls:
        for n in i.topList:

            if middlePoint[0]-20 < n[0] < middlePoint[0]+20 and n[1] < middlePoint[1]:
                listOfCoords.insert(len(listOfCoords), n)
    nearest = max(listOfCoords)
    
    return round(math.sqrt(((nearest[0] - middlePoint[0]) ** 2) + ((nearest[1] - middlePoint[1]) ** 2)))


def distRight(middlePoint, walls):
    
    # Returns the distance to the nearest obstruction on a given side
    
    listOfCoords = []

    for i in walls:
        for n in i.rightList:
            if middlePoint[1]-20 < n[1] < middlePoint[1]+20 and n[0] > middlePoint[0]:
                listOfCoords.insert(len(listOfCoords), n)
    nearest = min(listOfCoords)
    
    return round(math.sqrt(((nearest[0] - middlePoint[0]) ** 2) + ((nearest[1] - middlePoint[1]) ** 2)))


def distObj(selfCenter, targetCenter):
    
    # Returns distance between self and the middle of the target
    
    return round(math.sqrt(((targetCenter[0] - selfCenter[0]) ** 2) + ((targetCenter[1] - selfCenter[1]) ** 2)))


'''Functions for returning the output nodes'''

def outNodeLeft(chrom, inputs, bot):
    
    if len(chrom) > 0:
        n1 = inputs[0] * (chrom[0] / 1000)
        n2 = inputs[1] * (chrom[3] / 1000)
        n3 = inputs[2] * (chrom[6] / 1000)
        n4 = inputs[3] * (chrom[9] / 1000)
        #return n1+n2+n3+n4
        bot.outputList[0] = n1+n2+n3+n4
    else:
        pass


def outNodeFront(chrom, inputs, bot):
    
    if len(chrom) > 0:
        n1 = inputs[0] * (chrom[1] / 1000)
        n2 = inputs[1] * (chrom[4] / 1000)
        n3 = inputs[2] * (chrom[7] / 1000)
        n4 = inputs[3] * (chrom[10] / 1000)
        #return n1 + n2 + n3 + n4
        bot.outputList[1] = n1+n2+n3+n4
    else:
        pass


def outNodeRight(chrom, inputs, bot):
    
    if len(chrom) > 0:
        n1 = inputs[0] * (chrom[2] / 1000)
        n2 = inputs[1] * (chrom[5] / 1000)
        n3 = inputs[2] * (chrom[8] / 1000)
        n4 = inputs[3] * (chrom[11] / 1000)
        #return n1 + n2 + n3 + n4
        bot.outputList[2] = n1+n2+n3+n4
    else:
        pass


# In[6]:


# Creates a player class with useful data


class Player():
    
    model = pygame.image.load("spaceship.png")
    sprite = pygame.transform.scale(model, (30, 30))
    
    chromosome = []
    
    xChange = 0
    yChange = 0
    
    xPos = (width * .5) - 15
    yPos = (height * .8) + 15
    
    xCent = xPos + 15
    yCent = yPos + 15
    selfCenter = (xCent, yCent)
    
    UL_corner = (xCent-15, yCent+15)
    UR_corner = (xCent+15, yCent+15)
    BR_corner = (xCent+15, yCent-15)
    BL_corner = (xCent-15, yCent-15)
    
    top = (UL_corner, UR_corner)
    left = (BL_corner, UL_corner)
    bottom = (BL_corner, BR_corner)
    right = (BR_corner, UR_corner)
    
    lMid = midpoint(left)
    tMid = midpoint(top)
    rMid = midpoint(right)
    
    sensLeft = distLeft(lMid, walls)
    sensFront = distFront(tMid, walls)
    sensRight = distRight(rMid, walls)
    sensObj = distObj(selfCenter, targetPos)
    sensList = [sensLeft, sensFront, sensRight, sensObj]
    
    outputLeft = 0
    outputFront = 0
    outputRight = 0
    outputList = [outputLeft, outputFront, outputRight]
    
    fitness = 0

    canMove = True


# In[7]:


# Initialize bots and related criteria


bot1 = Player()

bot2 = Player()

bot3 = Player()

bot4 = Player()

bot5 = Player()

bot6 = Player()

bot7 = Player()

bot8 = Player()


botList = [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8]

for i in botList:
    
    bList = []
    
    for n in range(1,13):
        bList.insert(len(bList), random.choice(range(0, 1000)))
    i.chromosome = bList


# In[8]:


# Function for the game loop

def gameloop():
    
    #function containing the loop for the main processes
    
    inGame = True
    
    while inGame:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e: sys.exit()

        for i in botList:

            # Disables movement if bots are outside of boundaries
            if i.xPos > width-65 or i.xPos < 40:
                i.canMove = False
            if i.yPos > height-65 or i.yPos < 40:
                i.canMove = False

            # Disables movement if bots hit a wall
            for n in walls:

                # If bot hit bottom
                if n.get_BL_corner()[0] <= i.UL_corner[0] and i.UL_corner[0] <= n.get_BR_corner()[0]:
                    if n.get_UL_corner()[1] <= i.UL_corner[1] and n.get_BL_corner()[1] >= i.UL_corner[1]:
                        print('n')
                if n.get_BL_corner()[0] <= i.UR_corner[0] and i.UR_corner[0] <= n.get_BR_corner()[0]:
                    if n.get_UL_corner()[1] <= i.UR_corner[1] and n.get_BL_corner()[1] >= i.UR_corner[1]:
                        pass

            outNodeLeft(i.chromosome, i.sensList, i)
            outNodeFront(i.chromosome, i.sensList, i)
            outNodeRight(i.chromosome, i.sensList, i)

            if max(i.outputList) == i.outputList[0] and i.canMove:
                i.xPos += -5
            elif max(i.outputList) == i.outputList[1] and i.canMove:
                i.yPos += -5
            elif max(i.outputList) == i.outputList[2] and i.canMove:
                i.xPos += 5

            i.xCent = i.xPos + 15
            i.yCent = i.yPos + 15
            i.selfCenter = (i.xCent, i.yCent)

            i.UL_corner = (i.xCent - 15, i.yCent + 15)
            i.UR_corner = (i.xCent + 15, i.yCent + 15)
            i.BR_corner = (i.xCent + 15, i.yCent - 15)
            i.BL_corner = (i.xCent - 15, i.yCent - 15)

            i.top = (i.UL_corner, i.UR_corner)
            i.left = (i.BL_corner, i.UL_corner)
            i.bottom = (i.BL_corner, i.BR_corner)
            i.right = (i.BR_corner, i.UR_corner)

            i.lMid = midpoint(i.left)
            i.tMid = midpoint(i.top)
            i.rMid = midpoint(i.right)

            i.sensLeft = distLeft(i.lMid, walls)
            i.sensFront = distFront(i.tMid, walls)
            i.sensRight = distRight(i.rMid, walls)
            i.sensObj = distObj(i.selfCenter, targetPos)
            i.sensList = [i.sensLeft, i.sensFront, i.sensRight, i.sensObj]

        screen.fill(white)
        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        for i in botList:
            screen.blit(i.sprite, (i.xPos, i.yPos))
        for wall in walls:
            pygame.draw.rect(screen, (black), wall.rect)
        print(walls[15].get_UL_corner()[1])
        print(walls[15].get_BL_corner()[1])
        print('')
        pygame.display.update()
        clock.tick(30)
        


# In[9]:


gameloop()

# In[ ]:

'''
corners for both classes are calculated wrong and for some reason, when corrected, it completely fucks up the sensors

 - thinking of switching the corner calculations to based off of the origin coords of the objects, and fix sensors from
 there.
'''


