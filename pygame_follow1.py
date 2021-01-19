import pygame,sys
from pygame.locals import *
import math
pygame.init()
screenlenth=800
screen=pygame.display.set_mode((screenlenth,screenlenth))
pygame.display.set_caption("Line rotate")


x=400
y=350

def resang(x1,y1,x2,y2):
    
    return math.atan2(y2-y1,x2-x1)
fonts2=pygame.font.Font('freesansbold.ttf',35)

# def inverse_kinematics(sx,sy,c):
    
    
#     ex=sx+(line_length*math.cos(ang))
#     ey=sy+(line_length*math.sin(ang))


line_length=300


running=True
while running:
    
        screen.fill((0,0,0))       
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key==K_SPACE:
                    line_length+=5
                elif event.key==K_DOWN:
                    line_length-=5
        mice=pygame.mouse.get_pos()
        posx=mice[0]
        posy=mice[1]
        #print(posx,posy) 
        
        phase=0
        
        ang=(resang(posx,posy,x,y))
        x=posx+(line_length*math.cos(phase+ang))
        y=posy+(line_length*math.sin(phase+ang))
        pygame.draw.line(screen,(232, 30, 37),(x,y),(posx,posy),4)
        
        pygame.display.update()                