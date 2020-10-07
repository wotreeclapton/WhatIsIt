#Game option/settings
from os import path

GAMENAME = "What Is It App"

COMX = 380
COMY = 85
SCREENWIDTH = 1000
SCREENHEIGHT = 700
FPS = 60

#Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED =(255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (128,0,128)

POWERUP_TIME = 10000
MOVE_DELAY = 550

#set up game folders
GAME_FOLDER = path.dirname(__file__)
IMG_FOLDER = path.join(GAME_FOLDER, 'img')
SOUND_FOLDER = path.join(GAME_FOLDER, 'snd')
