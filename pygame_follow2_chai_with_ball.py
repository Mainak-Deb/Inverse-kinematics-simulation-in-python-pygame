import time
import pygame,sys,random
from pygame.locals import *
import math
pygame.init()
screenlenth=800
screen=pygame.display.set_mode((screenlenth,screenlenth))
pygame.display.set_caption("    FOLLOW 2   ")


x=400
y=350

def resang(x1,y1,x2,y2):
    return math.atan2(y2-y1,x2-x1)

arr=[]
for i in range(120):
    x=400
    y=350
    arr.append([x,y])
    
line_length=12


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
        for i in range(120):
            ang=(resang(posx,posy,arr[i][0],arr[i][1]))
            arr[i][0]=posx+(line_length*math.cos(phase+ang))
            arr[i][1]=posy+(line_length*math.sin(phase+ang))
            pygame.draw.line(screen,(int(random.randint(0,255)), int(random.randint(0,255)), int(random.randint(0,255))),(arr[i][0],arr[i][1]),(posx,posy),4)
            posx=arr[i][0];posy=arr[i][1]
            
        pygame.draw.circle(screen,(int(random.randint(0,255)), int(random.randint(0,255)), int(random.randint(0,255))),(int(arr[i][0]),int(arr[i][1])),10)
            
            
            
        pygame.display.update()                