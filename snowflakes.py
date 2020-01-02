import pygame,sys,random

SNOW_NUMBER       = 500
SNOW_SIZE_MAX     = 15
SNOW_BEGIN_Y      = -50
SNOW_SPEED_MAX    = 3
SCREEN_W,SCREEN_H = 1024,768
class Snow(object):
    def __init__(self,d):
        self.r = random.randint(1,SNOW_SIZE_MAX)
        rgb = d/SNOW_NUMBER * 250 + 5
        self.c = (rgb,rgb,rgb)
        self.x = random.randint(0,SCREEN_W)
        self.y = random.randint(0,SCREEN_H + SNOW_BEGIN_Y)
        self.speedX = 0
        self.speedY = d/SNOW_NUMBER * SNOW_SPEED_MAX
        self.flag = random.randint(0,1)
        return
    def draw(self,screen):
        x0,y0 = self.x,self.y
        r = self.r
        pygame.draw.line(screen, self.c, (int(round(x0 + r * 0.865)), int(round(y0 - r * 0.5))),\
                        (int(round(x0 - r * 0.865)), int(round(y0 + r * 0.5))), 3)
        pygame.draw.line(screen, self.c, (int(round(x0 + r * 0.865)), int(round(y0 + r * 0.5))),\
                        (int(round(x0 - r * 0.865)), int(round(y0 - r * 0.5))), 3)
        pygame.draw.line(screen, self.c,(int(round(x0)), int(round(y0 - r))),\
                        (int(round(x0)), int(round(y0+r))), 3)
        r *= 0.8
        polygon = ((int(round(x0)),int(round(y0-r))),(int(round(x0+r*0.865)),int(round(y0-r*0.5))),\
                   (int(round(x0+r*0.866)), int(round(y0+r*0.5))),(int(round(x0)), int(round(y0+r))),\
                   (int(round(x0-r*0.866)), int(round(y0+r*0.5))),(int(round(x0-r*0.866)),int(round(y0-r*0.5))))
        pygame.draw.lines(screen, self.c, True, polygon, 1)
        r = 0.5 * self.r
        polygon = ((int(round(x0)),int(round(y0-r))),(int(round(x0+r*0.865)),int(round(y0-r*0.5))),\
                   (int(round(x0+r*0.866)), int(round(y0+r*0.5))),(int(round(x0)), int(round(y0+r))),\
                   (int(round(x0-r*0.866)), int(round(y0+r*0.5))),(int(round(x0-r*0.866)), int(round(y0-r*0.5))))
        pygame.draw.lines(screen,self.c,True,polygon,1)
        return
    def move(self):
        self.x += self.speedX
        self.y += self.speedY
        if self.y > SCREEN_H + self.r:
            self.y = SNOW_BEGIN_Y
        return

# initialize snowflakes
snowList = []
for d in range(SNOW_NUMBER):
    snow = Snow(d)
    snowList.append(snow)

# main
pygame.init()
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption("Snowflakes Simulator")
clock = pygame.time.Clock()
backgroundImg = pygame.transform.scale(pygame.image.load("backgroundImg.jpg"), (SCREEN_W,SCREEN_H)) 
while True:
    screen.blit(backgroundImg, (0,0))
    for snow in snowList:
        snow.move()
        snow.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(100)
