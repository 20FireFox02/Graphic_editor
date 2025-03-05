from button_module import Button
from menu_module import Menu
from button_funcs import *

EQUPM_BUTTON_SIZE=(40,40)
ALG_BUTTON_SIZE=(90,20)

buttons=[[Button((5,5),EQUPM_BUTTON_SIZE,lambda:set_menu()),\
          Button((5,50),EQUPM_BUTTON_SIZE,lambda:set_menu()),\
          Button((5,750),EQUPM_BUTTON_SIZE,lambda:True)],\
         [Button((50,5),ALG_BUTTON_SIZE,lambda:dda_btn()),\
          Button((50,30),ALG_BUTTON_SIZE,lambda:brz_btn()),\
          Button((50,55),ALG_BUTTON_SIZE,lambda:wu_btn())],\
         [Button((50,50),ALG_BUTTON_SIZE,lambda:brz_crcl_btn()),\
          Button((50,75),ALG_BUTTON_SIZE,lambda:ell_btn()),\
          Button((50,100),ALG_BUTTON_SIZE,lambda:gprbl_btn()),\
          Button((50,125),ALG_BUTTON_SIZE,lambda:prbl_btn())]]


menus=[Menu((0,0),(50,800)),Menu((45,0),(100,80)),Menu((45,45),(100,105))]
