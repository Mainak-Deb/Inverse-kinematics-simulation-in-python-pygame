import pygame,sys,random
from pygame.locals import *
import math
pygame.init()
screenlenth=800
screen=pygame.display.set_mode((screenlenth,screenlenth))
line=20

x=300
y=300

sx=.8
sy=1
r=25

x0=400
y0=800

count_length=25

l_w=10

def resang(x1,y1,x2,y2):
    return math.atan2(y2-y1,x2-x1)

ax=0
ay=0
arr=[]
for i in range(count_length):
    arrx=400
    arry=350
    arr.append([arrx,arry])
    
line_length=15



running=True

while running:
    screen.fill((10,10,5))
    
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
                running=False
        if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    running=False
   
    x+=sx
    y+=sy
    
    if((x>=screenlenth-r) or (x<=r)):
        sx=sx*(-1)
    if((y>=screenlenth-r) or (y<=r)):
        sy=sy*(-1)
                
       
    pygame.draw.circle(screen,(int(x/4)+60,int(y/5)+55,int(((x*y)**(.5))/5)+55),(int(x),int(y)),int(r),15)

    posx=x+ax
    posy=y+ay
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
        
        pygame.draw.line(screen,(int(random.randint(0,255)), int(random.randint(0,255)), int(random.randint(0,255))),(arr[i][0]-ax,arr[i][1]-ay),(arr[i+1][0]-ax,arr[i+1][1]-ay),int(((l_w/count_length)*i)+3))
        posx=arr[i][0];posy=arr[i][1]   
        
            
    pygame.display.update()