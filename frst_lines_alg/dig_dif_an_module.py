from wind_init_module import pg,display
from constant_module import BLACK,PIXEL
from classes.algoritm_module import Algoritm

class Dda(Algoritm):
    def draw_line(b_crd,e_crd,check):
        
        x,y=b_crd
        lenght=max(abs(e_crd[0]-x),abs(e_crd[1]-y))
        try:
            dx=(e_crd[0]-x)/lenght
            dy=(e_crd[1]-y)/lenght
        except:
            dx,dy=0,0
        x+=0.5*round(dx,0)
        y+=0.5*round(dy,0)

        pg.draw.rect(display,BLACK,(int(x)*PIXEL,int(y)*PIXEL,PIXEL,PIXEL))
        i=0
        while i<=lenght:
            
            pg.draw.rect(display,BLACK,(int(x)*PIXEL,int(y)*PIXEL,PIXEL,PIXEL))
            x+=dx
            y+=dy
            i+=1
            check()
