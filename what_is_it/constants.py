'''
WHAT IS IT APPLICATION - Constants 
    Developed by Mr Steven J walden
    Aug. 2025
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''
#Imports
from os import path

__author__ = 'Mr Steven J Walden'
__version__ = '1.6.0'

GAMENAME = "What Is It App"

# Game Modes
GAME_MODE_EASY = "Easy"
GAME_MODE_MEDIUM = "Medium"
GAME_MODE_HARD = "Hard"

COMX = 380
COMY = 85
SCREENWIDTH = 1000
SCREENHEIGHT = 700
FPS = 60

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

POWERUP_TIME = 10000
MOVE_DELAY = 550

# set up game folders
GAME_FOLDER = path.dirname(__file__)
IMG_FOLDER = path.join(GAME_FOLDER, 'img')
SOUND_FOLDER = path.join(GAME_FOLDER, 'snd')
# PIC_FOLDER = path.join(IMG_FOLDER, "game_pics")
