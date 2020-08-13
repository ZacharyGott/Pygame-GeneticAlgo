# Packages and dependancies

import pygame
pygame.init()

# Basic Pygame attributes

size = width, height = 400, 600

black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


# Functions for the "Player" class to fill in data


def midpoint(side):
    # Finds midpoint using midpoint formula and returns as (x, y)

    return (round((side[0][0] + side[1][0]) / 2), round((side[0][1] + side[1][1]) / 2))

def distLeft():
    pass


def distFront():
    pass


def distRight():
    pass


def distObj():
    pass


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

    UL_corner = (xCent - 15, yCent + 15)
    UR_corner = (xCent + 15, yCent + 15)
    BR_corner = (xCent + 15, yCent - 15)
    BL_corner = (xCent - 15, yCent - 15)

    top = (UL_corner, UR_corner)
    left = (BL_corner, UL_corner)
    bottom = (BL_corner, BR_corner)
    right = (BR_corner, UR_corner)

    sensLeft = distLeft()
    sensFront = distFront()
    sensRight = distRight()
    sensObj = distObj()

    lMid = midpoint(left)
    tMid = midpoint(top)
    rMid = midpoint(right)

    fitness = 0


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


# Class for creating walls, obbjective and anything related

walls = []


class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 40, 40)

        self.xCent = pos[0] + 19
        self.yCent = pos[1] + 19

        self.UL_corner = (self.xCent - 15, self.yCent + 15)
        self.UR_corner = (self.xCent + 15, self.yCent + 15)
        self.BR_corner = (self.xCent + 15, self.yCent - 15)
        self.BL_corner = (self.xCent - 15, self.yCent - 15)

        self.top = (self.UL_corner, self.UR_corner)
        self.left = (self.BL_corner, self.UL_corner)
        self.bottom = (self.BL_corner, self.BR_corner)
        self.right = (self.BR_corner, self.UR_corner)

        self.topList = horizontalPoint(self.top)
        self.bottomList = horizontalPoint(self.bottom)
        self.leftList = verticlePoint(self.left)
        self.rightList = verticlePoint(self.right)


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
        dx += 40
    dy += 40
    dx = 0


# Function for the game loop

def gameloop():
    # function containing the loop for the main processes

    pass
