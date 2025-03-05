from constant_module import *

from wind_init_module import pg,display

#import wind_init_module as wi
from var_module import menu_nums
from menu_var_module import buttons,menus

def draw_button(menu):
    for button in buttons[menu]:
        pg.draw.rect(display,GRAY,[button.begin_crd[0],button.begin_crd[1],\
                                   button.size[0],button.size[1]])
def draw_menu():

    for menu_num in menu_nums:
        
        pg.draw.rect(display,DARK_GRAY,[menus[menu_num].begin_crd[0],menus[menu_num].begin_crd[1],\
                                        menus[menu_num].size[0],menus[menu_num].size[1]])
        try:
            draw_button(menu_num)
        except:
            print("No buttons")