'''
WHAT IS IT APP LAUNCHER - Sprite classes
	Developed by Mr Steven J walden
    Aug. 2025
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''

from os import path
import pygame as pg
import what_is_it.constants as const



class Spritesheet:
	def __init__(self, filename):
		try:
			self.spritesheet = pg.image.load(filename).convert_alpha()
		except Exception as e:
			print(f"Error loading spritesheet {filename}: {e}")

	def get_image(self, x, y, width, height):
		#Grab an image from the sheet
		image = pg.Surface((width, height), pg.SRCALPHA)
		image.blit(self.spritesheet, (0,0), (x, y, width, height))
		return image

class NumberMobs(pg.sprite.Sprite):
	def __init__(self, spritesheet, xpos, ypos, width, height):
		pg.sprite.Sprite.__init__(self)
		self.sprite_sheet = spritesheet
		self.image = self.sprite_sheet.get_image(xpos, ypos, width, height)
		self.rect = self.image.get_rect(topleft=(xpos, ypos))
		self.rect.x = xpos
		self.rect.y = ypos

class WrongAnswer(pg.sprite.Sprite):
	"""Sprite for displaying a 'Wrong Answer' animation sequence."""
	def __init__(self, game):
		pg.sprite.Sprite.__init__(self)
		self.game = game
		self.img_num = 1
		self.image = self.game.resource_manager.get_image("wrong1")
		self.rect = self.image.get_rect()
		self.rect.centerx = const.SCREENWIDTH / 2
		self.rect.centery = const.SCREENHEIGHT / 2
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
			self.image = self.game.resource_manager.get_image(f"wrong{self.img_num}")
			self.rect = self.image.get_rect()
			self.rect.centerx = const.SCREENWIDTH / 2
			self.rect.centery = const.SCREENHEIGHT / 2

class RightAnswer(WrongAnswer):
	"""Inherent class from WrongAnswer"""
	def __init__(self, game, game_mode):
		super(RightAnswer, self).__init__(game)
		self.game_mode = game_mode
		self.image = pg.image.load(path.join(const.IMG_FOLDER, f"{self.game_mode}_mode_image.png")).convert()
		self.rect = self.image.get_rect()
		self.rect.centerx = const.SCREENWIDTH / 2
		self.rect.centery = const.SCREENHEIGHT / 2
		self.frame_rate = 100
		self.alpha_num = 255

	def update(self):
		#Change image alpha
		img_now = pg.time.get_ticks()
		if img_now - self.img_last_update >= self.frame_rate:
			self.img_last_update = img_now
			self.alpha_num -= 12
			if self.alpha_num < 10:
				self.alpha_num = 10
				self.kill()
			self.image.set_alpha(self.alpha_num)
			self.rect = self.image.get_rect()
			self.rect.centerx = const.SCREENWIDTH / 2
			self.rect.centery = const.SCREENHEIGHT / 2


#Run Gui
# if __name__ == '__main__':
# 	app = QtWidgets.QApplication(sys.argv)
# 	main_app = StartUpGui()
# 	main_app.show()


# sys.exit(app.exec_())
