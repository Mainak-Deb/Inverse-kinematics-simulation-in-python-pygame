import time
import pygame,sys,random
from pygame.locals import *
import math
pygame.init()
screenlenth=800
screen=pygame.display.set_mode((screenlenth,screenlenth))
pygame.display.set_caption("    FOLLOW 2   ")


x0=400
y0=800

count_length=40

def resang(x1,y1,x2,y2):
    return math.atan2(y2-y1,x2-x1)

ax=0
ay=0
arr=[]
for i in range(count_length):
    x=400
    y=350
    arr.append([x,y])
    
line_length=15


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
        posx=mice[0]+ax
        posy=mice[1]+ay
        #print(posx,posy) 
        
        phase=0
        for i in range(count_length):
            ang=(resang(posx,posy,arr[i][0],arr[i][1]))
            arr[i][0]=posx+(line_length*math.cos(phase+ang))
            arr[i][1]=posy+(line_length*math.sin(phase+ang))
            posx=arr[i][0];posy=arr[i][1]
        ax=arr[count_length-1][0]-x0
        ay=arr[count_length-1][1]-y0
        for i in range(count_length-1):
            
            pygame.draw.line(screen,(int(random.randint(0,255)), int(random.randint(0,255)), int(random.randint(0,255))),(arr[i][0]-ax,arr[i][1]-ay),(arr[i+1][0]-ax,arr[i+1][1]-ay),4)
            posx=arr[i][0];posy=arr[i][1]   
            
            
        pygame.display.update()                