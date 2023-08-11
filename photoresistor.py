import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)
'''SCREEN_WIDTH = 1075
SCREEN_HEIGHT = 625
pygame.init()
pygame.display.set_caption("PBL Project!!")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()'''
#pin_to_circuit = 17

def rc_time (pin_to_circuit):
    count = 0

    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    t.sleep(0.01)
    GPIO.setup(pin_to_circuit, GPIO.IN)

    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

'''try:
    while True:
        print rc_time(pin_to_circuit)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

class Fire_extinguisher(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("Extinguisher1.png").convert_alpha()
    def draw(self,x,y):
        screen.blit(self.image, (x, y))

class Background(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("Ground.jpg").convert_alpha()
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

if __name__ == "__main__":
    Extinguisher = Fire_extinguisher()
    Background = Background()
    while True:
        t.sleep(1)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        Background.draw()
        Extinguisher.draw(117,90)
        Extinguisher.draw(350,307)
        Extinguisher.draw(530,535)
        Extinguisher.draw(815,375)
        pygame.display.update()
'''
