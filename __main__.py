from drawing.draw_module import *
import drawing.draw_module as dm
from sys import exit
import time

from wind_init_module import pg,clock
from drawing.draw_menu_module import draw_menu

from mouse_click_module import mouse_click

draw_click,checkout_click=False,False,False

draw_menu()
while True:

    for event in pg.event.get():

        if event.type is pg.QUIT:
            pg.quit()
            exit()
            
        elif event.type==pg.MOUSEBUTTONDOWN:
            if not mouse_click(event.pos):
                if 50<=event.pos[0]<=1000:
                    print("TOUCH")
                    draw_click=not draw_click
                if draw_click:
                    lines.append([event.pos[0]//PIXEL,event.pos[1]//PIXEL])
            """if 950<=mouse_pos[0]<=1000 and 0<=mouse_pos[1]<=50:
                menu_click = not menu_click
                draw(display,lambda:True,menu_click)
            elif menu_click:
                if 810<=mouse_pos[0]<=940 and 10<=mouse_pos[1]<=40:
                    
                    if dm.text==dm.dda_t:
                        dm.text,dm.n=dm.brz_t,1
                    elif dm.text==dm.brz_t:
                        dm.text,dm.n=dm.wu_t,2
                    else:
                        dm.text,dm.n=dm.dda_t,0
                    time.sleep(0.1)
                    draw(display,lambda:True,menu_click)
                elif 960<=mouse_pos[0]<=990 and 60<=mouse_pos[1]<=90:
                    checkout_click=not checkout_click
            else:
                draw_click=not draw_click"""

        elif event.type==pg.MOUSEMOTION:
            
            if draw_click:
                if abs(lines[-1][0][0]-event.pos[0]//PIXEL)>=1 \
                   or abs(lines[-1][0][1]-event.pos[1]//PIXEL)>=1:
                    lines[-1][1]=(event.pos[0]//PIXEL,event.pos[1]//PIXEL)
                    
                    def sleep():
                        time.sleep(0.1)
                        pg.display.update()
                    if checkout_click:
                        draw(lambda:sleep())
                    else:
                        draw(lambda:True)

        """
        elif event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                try:
                    lines.pop()
                    draw(display,lambda:True,menu_click)
                except:
                    pass
"""
    draw_menu()
    pg.display.update()
    clock.tick(FPS)







    """def draw():
        display.fill(WHITE)
        draw_menu()
        def sleep():
            time.sleep(0.1)
            pg.display.update()
        for line in  lines[:-1]:
            print("THERE")
            draw_alg[n].draw_line(display,line[0],line[1],lambda:0)
        try:
            if checkout_click:
                print("HERE")
                draw_alg[n].draw_line(display,lines[-1][0],line[-1][1],lambda:sleep())
            else:
                draw_alg[n].draw_line(display,lines[-1][0],lines[-1][1],lambda:0)
        except:
            pass"""
"""def draw_menu():
        if menu_click:
            pg.draw.rect(display,GRAY,[800,0,200,100])
            pg.draw.rect(display,WHITE,[960,60,30,30])
            pg.draw.rect(display,DARK_GRAY,[950,0,50,50])
            pg.draw.rect(display,WHITE,[810,10,130,30])
            display.blit(text,(810,15)) 
        else:
            pg.draw.rect(display,GRAY,[950,0,50,50])"""
