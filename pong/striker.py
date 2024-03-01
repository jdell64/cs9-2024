import pygame
from globals import HEIGHT, screen, font20

class Striker:

    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = self.original_posx = posx 
        self.posy = self.original_posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        self.geekRect = pygame.Rect(posx, posy, width, height)
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    def reset(self):
        self.posx = self.original_posx
        self.posy = self.original_posy
        
    # Used to display the object on the screen
    def display(self):
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)
  
    def update(self, yFac):
        self.posy = self.posy + self.speed*yFac
 
        # Restricting the striker to be below
        # the top surface of the screen
        if self.posy <= 0:
            self.posy = 0
        # Restricting the striker to be above
        # the bottom surface of the screen
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT-self.height
 
        # Updating the rect with the new values
        self.geekRect = (self.posx, self.posy, self.width, self.height)
    
    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
 
        screen.blit(text, textRect)
 
    def getRect(self):
        return self.geekRect