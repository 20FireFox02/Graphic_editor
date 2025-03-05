import pygame as pg
from constant_module import *

class Parab_alg:
    def draw_line(display,b_crd,e_crd,check):
        b=e_crd[1]-b_crd[1]
        
        if b!=0:
            a=e_crd[0]-b_crd[0]
            lim=b_crd[1]+50
            if b>0:ty=-1
            else:ty=1
        #pg.draw.rect(display,BLACK,(b_crd[0]*PIXEL,b_crd[1]*PIXEL,PIXEL,PIXEL))
        #print(b_crd,e_crd)

            delta=a**2*(1+2*abs(b))-b**2
        #print(delta)
        #print([x,y])
            x=b_crd[0]
            y=b_crd[1]+abs(b)
            print(y,y-abs(b))
            pg.draw.rect(display,BLACK,(x*PIXEL,(y-abs(b))*PIXEL,PIXEL,PIXEL))
            def deqz(x,y,delta):
                return x+1,y+1,delta+(2*(y-b_crd[1])+1)*a**2-(2*(x-b_crd[0])+1)*b**2
            while y-abs(b)<lim:
                if delta<0:
                    d=2*delta+2*(x-b_crd[0])*b**2+b**2
                    if d<=0:
                        y+=1
                        delta=delta+a**2*(2*(y-b_crd[1])+1)
                    else:x,y,delta=deqz(x,y,delta)
                elif delta>0:
                    d=2*delta-2*(y-b_crd[1])*a**2-a**2
                    if d>0:
                        x+=1
                        delta=delta-b**2*(2*(x-b_crd[0])+1)
                    else:x,y,delta=deqz(x,y,delta)
                else:x,y,delta=deqz(x,y,delta)
            #print([x,y])
                pg.draw.rect(display,BLACK,(x*PIXEL,(b_crd[1]+b_crd[1]*ty-(y-abs(b))*ty)*PIXEL,PIXEL,PIXEL))
                pg.draw.rect(display,BLACK,((b_crd[0]-x+b_crd[0])*PIXEL,(b_crd[1]+b_crd[1]*ty-(y-abs(b))*ty)*PIXEL,PIXEL,PIXEL))
                #check

#a=Brz_circle_alg
#a.draw_line((0,0),(0,8))
