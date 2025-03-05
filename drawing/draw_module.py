import pygame as pg
from frst_lines_alg.brezen_alg_module import *
from frst_lines_alg.dig_dif_an_module import *
from frst_lines_alg.wu_alg_module import *

from sec_lines_alg.brezen_circle_alg_module import *
from sec_lines_alg.ellipse_alg_module import *
from sec_lines_alg.giperb_alg_module import *
from sec_lines_alg.parab_alg_module import *

from wind_init_module import display
import var_module

lines=[]
#n=0
#draw_frst_line_alg=[Ellipse_alg,Dda,Brz_alg,Wu_alg]
#draw_sec_line_alg=[Parab_alg,Giperb_alg,Ellipse_alg,Brz_circle_alg]

drawing_alg=[Dda,Brz_alg,Wu_alg,Brz_circle_alg,Ellipse_alg,Giperb_alg,Parab_alg]
"""pg.font.init()
smallfont = pg.font.SysFont('Corbel',25) 
dda_t=smallfont.render('dda',True,BLACK)
brz_t=smallfont.render('brezen',True,BLACK)
wu_t=smallfont.render('wu',True,BLACK)

text=dda_t
"""
def draw(check):
    
    display.fill(WHITE)
    #draw_menu(display,menu_click)
    for line in  lines[:-1]:
        #draw_alg[n].draw_line(display,line[0],line[1],lambda:True)
        #draw_frst_line_alg[n].draw_line(display,line[0],line[1],lambda:True)
        drawing_alg[var_module.alg_num].draw_line(display,line[0],line[1],lambda:True)
    #draw_alg[n].draw_line(display,lines[-1][0],lines[-1][1],check)
    try:
        #draw_alg[n].draw_line(display,lines[-1][0],lines[-1][1],check)
        #draw_frst_line_alg[n].draw_line(display,lines[-1][0],lines[-1][1],check)
        drawing_alg[var_module.alg_num].draw_line(display,lines[-1][0],lines[-1][1],lambda:True)
    except:
        print("Error last line drawing")
"""
def draw_menu(display,menu_click):
    #pg.draw.rect(display,DARK_GRAY,[0,0,50,800])
    #pg.draw.rect(display,GRAY,[5,5,40,40])
    #pg.draw.rect(display,GRAY,[5,50,40,40])
    if menu_click:
        pg.draw.rect(display,GRAY,[800,0,200,100])
        pg.draw.rect(display,WHITE,[960,60,30,30])
        pg.draw.rect(display,DARK_GRAY,[950,0,50,50])
        pg.draw.rect(display,WHITE,[810,10,130,30])
        display.blit(text,(810,15)) 
    else:
        pg.draw.rect(display,GRAY,[950,0,50,50])


#print("a"[-1])
"""