import pygame
import pygame.mixer
import RPi.GPIO as GPIO
import threading
import shape
import photoresistor2
import time as t
import sys

SCREEN_WIDTH = 1075
SCREEN_HEIGHT = 625

red = (255, 0, 0)
blue =  (0, 0, 255)
yellow = (255, 255, 36)
white = (255, 255, 255)
black = (0, 0, 0)
'''-----------------Variable------------------'''
flame1 = 21
flame2 = 20
flame3 = 16
flame4 = 12
flame5 = 26
flame6 = 19
light1 = 17
light2 = 27
light3 = 22
a = 15
b = 15
c = 15
'''-----------------Defualt-------------------'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(flame1, GPIO.IN)
GPIO.setup(flame2, GPIO.IN)
GPIO.setup(flame3, GPIO.IN)
GPIO.setup(flame4, GPIO.IN)
GPIO.setup(flame5, GPIO.IN)
GPIO.setup(flame6, GPIO.IN)

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("PBL Project!!")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
'''------------------Screen-------------------'''
class Background(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("New_Ground.png").convert_alpha()
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
Background = Background()        

class Fire_extinguisher(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("Extinguisher1.png").convert_alpha()
    def draw(self, x, y):
        screen.blit(self.image, (x, y))        

Extinguisher = Fire_extinguisher()
'''-----------------Threading-----------------'''
class NewTime:
    def __init__(self):
        pass
    
    def rain(self):
        global a, b, c
        a += 1
        b += 1
        c += 1
        if a > 35:
            a = 15
        if b > 40:
            b = 15
        if c > 45:
            c = 15
        threading.Timer(0.05,self.rain).start()
        
    def Blink(self):
        global blink
        blink += 1
        threading.Timer(0.8,self.Blink).start()

    def Exting(self):
        global Exting1, Exting2, Exting3
        if photoresistor2.rc_time(light1) < 5000:
            Exting1 = 1
        else:
            Exting1 = 0
            
        if photoresistor2.rc_time(light2) < 5000:
            Exting2 = 1
        else:
            Exting2 = 0
            
        if photoresistor2.rc_time(light3) < 5000:
            Exting3 = 1
        else:
            Exting3 = 0
        threading.Timer(2,self.Exting).start()

New = NewTime()
'''---------------Fire_Detection--------------'''
def Fire1(flame1):
	global fire1
	fire1 += 1
GPIO.add_event_detect(flame1, GPIO.BOTH, callback=Fire1, bouncetime=300)

def Fire2(flame2):
	global fire2
	fire2 += 1
GPIO.add_event_detect(flame2, GPIO.BOTH, callback=Fire2, bouncetime=300)

def Fire3(flame3):
	global fire3
	fire3 += 1
GPIO.add_event_detect(flame3, GPIO.BOTH, callback=Fire3, bouncetime=300)

def Fire4(flame4):
	global fire4
	fire4 += 1
GPIO.add_event_detect(flame4, GPIO.BOTH, callback=Fire4, bouncetime=300)

def Fire5(flame5):
	global fire5
	fire5 += 1
GPIO.add_event_detect(flame5, GPIO.BOTH, callback=Fire5, bouncetime=300)

def Fire6(flame6):
	global fire6
	fire6 += 1
GPIO.add_event_detect(flame6, GPIO.BOTH, callback=Fire6, bouncetime=300)
'''------------------clear--------------------'''
def CLEAR():
    pygame.mixer.music.pause()
    global temp_x, temp_y, flag
    global a, b, c, pos_x, pos_y, x1, y1
    flag = 0
    pos_x = 0
    pos_y = 0
    temp_x = 0
    temp_y = 0
    x1 = 0
    y1 = 0
    a = 15
    b = 15
    c = 15
'''---------------Fire_Funtion----------------'''
def UP():
    global fire1, fire2, temp_x, temp_y, blink
    global a, b, c, pos_x, pos_y, x1, y1
    if 200 - pos_y > 150:
        pos_y += 2
        shape.poly_U(459, 199 - pos_y)
        shape.rect_U(523, 220 - pos_y, 0, 20+pos_y)
    else:
        if blink % 2 == 0:
            shape.poly_U(459, 199 - pos_y)
            shape.rect_U(523, 220 - pos_y, 0, 20+pos_y)

def right():
    global fire1, fire2, temp_x, temp_y, blink
    global a, b, c, pos_x, pos_y, x1, y1
    if 520 + pos_x < 770:
        pos_x += 4
        temp_x = pos_x
        shape.poly_R(510 + pos_x, 260)
        shape.rect_R(560, 250, pos_x + 10, 0)
    elif 210 - y1 > 140:
        y1 += 4
        shape.poly_U(750, 220 - y1)
        shape.rect_U(815, 240 - y1, 0, 30 + y1)
        shape.rect_R(560,250, temp_x + 10, 0)
    else:
        if blink % 2 == 0:
            shape.poly_U(750, 220 - y1)
            shape.rect_U(815, 240 - y1, 0, 30 + y1)
            shape.rect_R(560,250, temp_x + 10, 0)
'''----------------Fire_case------------------'''
def Fire_case():
    global fire1, fire2, temp_x, temp_y, blink, flag
    global a, b, c, pos_x, pos_y, x1, y1
    #-----------------CASE.1------------------#
    if fire1 % 2 == 1:
        shape.cir_R(320, 330, a, b, c)
        shape.cir_B(532, 260, a, b, c)
        if flag == 0:
            pygame.mixer.music.load("1.mp3")
            pygame.mixer.music.play(-1,0.0)
            flag = 1;
        UP()
        right()
    #-----------------CASE.2------------------#   
    elif fire2 % 2 == 1:
        shape.cir_R(810, 420, a, b, c)
        shape.cir_B(532, 260, a, b, c)
        UP()
        right()
        if flag == 0:
            pygame.mixer.music.load("2.mp3")
            pygame.mixer.music.play(-1,0.0)
            flag = 1;
    #-----------------CASE.3------------------#
    elif fire3 % 2 == 1:
        shape.cir_R(940, 250, a, b, c)
        shape.cir_B(532, 260, a, b, c)
        UP()
        if flag == 0:
            pygame.mixer.music.load("stairs.mp3")
            pygame.mixer.music.play(-1,0.0)
            flag = 1;
    #-----------------CASE.4------------------#
    elif fire4 % 2 == 1:
        shape.cir_R(130, 100, a, b, c)
        shape.cir_B(532, 260, a, b, c)
        UP()
        right()
        if flag == 0:
            pygame.mixer.music.load("3.mp3")
            pygame.mixer.music.play(-1,0.0)
            flag = 1;
    #-----------------CASE.5------------------#
    elif fire5 % 2 == 1:
        shape.cir_R(520, 550, a, b, c)
        shape.cir_B(532, 260, a, b, c)
        UP()
        right()
        if flag == 0:
            pygame.mixer.music.load("4.mp3")
            pygame.mixer.music.play(-1,0.0)
            flag = 1;
    #-----------------CASE.6------------------#
    elif fire6 % 2 == 1:
        shape.cir_R(590, 88, a, b, c)
        shape.cir_B(532, 260, a, b, c)
        right()
        if flag == 0:
            pygame.mixer.music.load("stairs.mp3")
            pygame.mixer.music.play(-1,0.0)
            flag = 1;
    else:
        CLEAR()
'''---------------Exting_case-----------------'''
def Exting_case():
    global Exting1, Exting2, Exting3
    #-----------------CASE.1------------------#
    if Exting1 == 0:
        Extinguisher.draw(117,90)
    #-----------------CASE.2------------------#
    if Exting2 == 0:
        Extinguisher.draw(350,307)
    #-----------------CASE.3------------------#        
    if Exting3 == 0:
        Extinguisher.draw(530,535)
'''-------------------main--------------------'''
if __name__ == "__main__":
    fire1 = 0
    fire2 = 0
    fire3 = 0
    fire4 = 0
    fire5 = 0
    fire6 = 0
    pos_x = 0
    pos_y = 0
    temp_x = 0
    temp_y = 0
    x1 = 0
    y1 = 0
    flag = 0
    blink = 0
    Exting1 = 0
    Exting2 = 0
    Exting3 = 0
    New.Blink()
    New.rain()
    New.Exting()
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        Background.draw()
        Exting_case()
        Fire_case()
        pygame.display.update()















