import pygame as pg
from constant_module import *
from algoritm_class_module import Algoritm

class Brz_alg(Algoritm):
    def draw_line(display,b_crd,e_crd,check):
        x,y=b_crd
        dx=e_crd[0]-x
        dy=e_crd[1]-y
        i=1
        pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))

        if dy<0:ty=-1
        else:ty=1
        if dx<0:tx=-1
        else:tx=1
        
        e=2*dy*ty-dx*tx

        """def draw():
            while i<=dy*ty:
                if e<=0:
                x+=PIXEL*tx
                e+=2*dy*ty
            y+=PIXEL*ty
            e-=2*dx*tx
            i+=PIXEL
            pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))"""
            
        if e>dx*tx:
            while i<=dy*ty:
                if e<=dx*tx:
                    x+=tx
                    e+=2*dy*ty
                y+=ty
                e-=2*dx*tx
                i+=1
                pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
                check()
        else:
            while i<=dx*tx:
                if e>=0:
                    y+=ty
                    e-=2*dx*tx
                x+=tx
                e+=2*dy*ty
                i+=1
                pg.draw.rect(display,BLACK,(x*PIXEL,y*PIXEL,PIXEL,PIXEL))
                check()

"""    while i<=dx:
        if e>=0:
            y+=PIXEL
            e-=2*dx
        x+=PIXEL
        e+=2*dy
        i+=PIXEL
        pg.draw.rect(display,BLACK,(x,y,PIXEL,PIXEL))"""
