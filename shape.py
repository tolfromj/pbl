import pygame
import time as t
import sys

red = (255, 0, 0)
blue =  (0, 0, 255)
yellow = (255, 255, 36)
white = (255, 255, 255)
black = (0, 0, 0)
SCREEN_WIDTH = 1075
SCREEN_HEIGHT = 625
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def cir_R(w, h, a, b, c):
        pygame.draw.circle(screen, red, [w, h], 15)
        pygame.draw.circle(screen, red, [w, h], a, 1)
        pygame.draw.circle(screen, red, [w, h], b-5, 1)
        pygame.draw.circle(screen, red, [w, h], c-10, 1)

def cir_B(w, h, a, b, c):
        pygame.draw.circle(screen, blue, [w, h], 15)
        pygame.draw.circle(screen, blue, [w, h], a, 1)
        pygame.draw.circle(screen, blue, [w, h], b-5, 1)
        pygame.draw.circle(screen, blue, [w, h], c-10, 1)
       
def rect_R(w,h,x,y):
        pygame.draw.rect(screen, yellow, [w, h, x, 20])

def rect_L(w,h,x,y):
        pygame.draw.rect(screen, yellow, [w, h, x, 20])
        
def rect_D(x,y):
        print("hi")
        
def rect_U(w,h,x,y):
        pygame.draw.rect(screen, yellow, [w, h, 20, y])

def poly_R(pos_x,pos_y):
        pygame.draw.polygon(screen, yellow, [[pos_x+50, pos_y+25],[pos_x+75, pos_y],[pos_x+50, pos_y-25]], 0)

def poly_L(pos_x,pos_y):
        pygame.draw.polygon(screen, yellow, [[pos_x+50, pos_y+25],[pos_x+25, pos_y+50],[pos_x+50, pos_y+75]], 0)
        
def poly_U(pos_x,pos_y):
        pygame.draw.polygon(screen, yellow, [[pos_x+50, pos_y+25],[pos_x+75, pos_y],[pos_x+100, pos_y+25]], 0)
