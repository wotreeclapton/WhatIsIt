#Game option/settings
from os import path

from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

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
#PIC_FOLDER = path.join(IMG_FOLDER, "game_pics")

def dark_theme(app):
	app.setStyle("Fusion")

	dark_palette = QPalette()

	dark_palette.setColor(QPalette.Window,QColor(53,53,53))
	dark_palette.setColor(QPalette.WindowText, Qt.white)
	dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
	dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
	dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
	dark_palette.setColor(QPalette.ToolTipText, Qt.white)
	dark_palette.setColor(QPalette.Text, Qt.white)
	dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
	dark_palette.setColor(QPalette.ButtonText, Qt.white)
	dark_palette.setColor(QPalette.BrightText, Qt.red)
	dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
	dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
	dark_palette.setColor(QPalette.HighlightedText, Qt.black)

	app.setPalette(dark_palette)

	app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

def light_theme(app):
	app.setStyle("Fusion")

	light_palette = QPalette()

	light_palette.setColor(QPalette.Window,QColor(225,225,225))
	light_palette.setColor(QPalette.WindowText, QtCore.Qt.black)
	light_palette.setColor(QPalette.Base, QColor(240, 240, 240))
	light_palette.setColor(QPalette.AlternateBase, QColor(225, 225, 225))
	light_palette.setColor(QPalette.ToolTipBase, QtCore.Qt.black)
	light_palette.setColor(QPalette.ToolTipText, QtCore.Qt.black)
	light_palette.setColor(QPalette.Text, QtCore.Qt.black)
	light_palette.setColor(QPalette.Button, QColor(225, 225, 225))
	light_palette.setColor(QPalette.ButtonText, QtCore.Qt.black)
	light_palette.setColor(QPalette.BrightText, QtCore.Qt.red)
	light_palette.setColor(QPalette.Link, QColor(251, 255, 255))
	light_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
	light_palette.setColor(QPalette.HighlightedText, QtCore.Qt.white)

	app.setPalette(light_palette)

	app.setStyleSheet("QToolTip { color: #706b67; background-color: #fffefa; border: 1px solid grey; }")