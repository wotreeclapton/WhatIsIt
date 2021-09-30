##! python 3
'''
WHAT IS IT APP LAUNCHER developed by Mr Steven J walden
    Sept. 2020
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''

#Gui's and Sprite classes for game 
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
#from PyQt5.QtWidgets import QWidget
import pygame as pg
from methods import *

class StartUpGui(QtWidgets.QWidget):
	"""docstrbing for MyApp"""
	def __init__(self, parent=None):
		super(StartUpGui, self).__init__(parent)
		self.initUI()

	def initUI(self):
		#Set up GUI
		self.resize(180, 272)
		self.setMinimumSize(180, 272)
		self.setMaximumSize(180, 272)
		self.setWindowIcon(QtGui.QIcon("img/Ep_window_icon.ico"))
		self.setWindowTitle("What is it?")

		self.add_buttons()
		self.tab_order()

	def add_buttons(self):
		bfont = QtGui.QFont()
		bfont.setPointSize(14)
		bfont.setBold(True)
		bfont.setItalic(True)

		self.EasyModeButton = QtWidgets.QPushButton(self)
		self.EasyModeButton.setGeometry(10, 28, 160, 60)
		# self.EasyModeButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.EasyModeButton.setCheckable(True)
		self.EasyModeButton.setChecked(True)
		self.EasyModeButton.setFont(bfont)
		self.EasyModeButton.setText("Easy Mode")

		self.HardModeButton = QtWidgets.QPushButton(self)
		self.HardModeButton.setGeometry(10, 98, 160, 60)
		# self.HardModeButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.HardModeButton.setCheckable(True)
		self.HardModeButton.setFont(bfont)
		self.HardModeButton.setText("Hard Mode")

		self.LoadImagesButton = QtWidgets.QPushButton(self)
		self.LoadImagesButton.setGeometry(10, 168, 160, 60)
		# self.LoadImagesButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.LoadImagesButton.setFont(bfont)
		self.LoadImagesButton.setText("Load Images")

		#Button for switchiong to darkmode
		bfont.setPointSize(8)
		bfont.setBold(False)
		self.DarkModeButton = QtWidgets.QPushButton(self)
		self.DarkModeButton.setGeometry(130, 4, 40, 20)
		self.DarkModeButton.setFocusPolicy(QtCore.Qt.NoFocus)		
		self.DarkModeButton.setCheckable(True)
		self.DarkModeButton.setFont(bfont)
		self.DarkModeButton.setText("Dark")

		#Button box setup for OKay and cancel buttons
		self.StartGameButtonBox = QtWidgets.QDialogButtonBox(self)
		self.StartGameButtonBox.setGeometry(12, 238, 156, 23)
		self.StartGameButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)

	def tab_order(self):
		self.setTabOrder(self.EasyModeButton, self.HardModeButton)
		self.setTabOrder(self.HardModeButton, self.LoadImagesButton)
		self.setTabOrder(self.StartGameButtonBox, self.EasyModeButton)

class Spritesheet:
	def __init__(self, filename):
		self.spritesheet = pg.image.load(filename).convert_alpha()

	def get_image(self, x, y, width, height):
		#Grab an image from the sheet
		image = pg.Surface((width, height), pg.SRCALPHA)
		image.blit(self.spritesheet, (0,0), (x, y, width, height))
		return image

class NumberMobs(pg.sprite.Sprite):
	def __init__(self, spritesheet, xpos, ypos, img):
		pg.sprite.Sprite.__init__(self)
		#self.game = game
		self.sprite_sheet = spritesheet
		self.load_images()
		self.image = self.number_mobs[img]
		# self.image = pg.Surface((50,50))
		# self.image.fill(colour)
		self.rect = self.image.get_rect()
		self.rect.x = xpos
		self.rect.y = ypos

	def update(self):
		pass

	def load_images(self):
		self.number_mobs = []
		for y in range (14):
			for x in range(20):
				self.number_mobs.append(self.sprite_sheet.get_image(x * 50, y * 50, 50, 50))

class WrongAnswer(pg.sprite.Sprite):
	"""docstring for WrongAnswer"""
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		# self.game = game
		self.img_num = 1
		self.image = pg.image.load(path.join(IMG_FOLDER, f"Wrong{self.img_num}.png")).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.centerx = SCREENWIDTH / 2
		self.rect.centery = SCREENHEIGHT / 2
		self.frame_rate = 100
		self.img_last_update = pg.time.get_ticks()

	def update(self):
		#Change image
		img_now = pg.time.get_ticks()
		if img_now - self.img_last_update >= self.frame_rate:
			self.img_last_update = img_now
			self.img_num += 1
			if self.img_num > 13:
				self.img_num = 13
				self.kill()
			self.image = pg.image.load(path.join(IMG_FOLDER, f"Wrong{self.img_num}.png")).convert_alpha()
			self.rect = self.image.get_rect()
			self.rect.centerx = SCREENWIDTH / 2
			self.rect.centery = SCREENHEIGHT / 2
		
class RightAnswer(WrongAnswer):
	"""Inherent class from WrongAnswer"""
	def __init__(self):
		super(RightAnswer, self).__init__()
		self.image = pg.image.load(path.join(IMG_FOLDER, f"Right{self.img_num}.png")).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.centerx = SCREENWIDTH / 2
		self.rect.centery = SCREENHEIGHT / 2
		self.frame_rate = 100

	def update(self):
		#Change image
		img_now = pg.time.get_ticks()
		if img_now - self.img_last_update >= self.frame_rate:
			self.img_last_update = img_now
			self.img_num += 1
			if self.img_num > 19:
				self.img_num = 19
				self.kill()
			self.image = pg.image.load(path.join(IMG_FOLDER, f"Right{self.img_num}.png")).convert_alpha()
			self.rect = self.image.get_rect()
			self.rect.centerx = SCREENWIDTH / 2
			self.rect.centery = SCREENHEIGHT / 2
		
#Runn Gui
# if __name__ == '__main__':
# 	app = QtWidgets.QApplication(sys.argv)
# 	main_app = StartUpGui()
# 	main_app.show()


# sys.exit(app.exec_())
