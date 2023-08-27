import pygame
WIDTH,HEIGHT=800,800
GREY=(128,128,128)
ROWS=int(input("Enter ROWs, COlumns"))
COLS=int(input())
SQUARE_SIZE=WIDTH//COLS
RED=(255,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)
CROWN=pygame.transform.scale(pygame.image.load('checkers/assets/crown.png'),(15,15))
