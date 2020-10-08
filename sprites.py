#Sprite classes for game 
import pygame as pg
from methods import *

class Spritesheet:
	def __init__(self, filename):
		self.spritesheet = pg.image.load(filename).convert_alpha()

	def get_image(self, x, y, width, height):
		#Grab an image from the sheet
		image = pg.Surface((width, height), pg.SRCALPHA)
		image.blit(self.spritesheet, (0,0), (x, y, width, height))
		return image

class NumberMobs(pg.sprite.Sprite):
	def __init__(self, game, xpos, ypos, img):
		pg.sprite.Sprite.__init__(self)
		self.game = game
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
				self.number_mobs.append(self.game.sprite_sheet.get_image(x * 50, y * 50, 50, 50))

class WrongAnswer(pg.sprite.Sprite):
	"""docstring for WrongAnswer"""
	def __init__(self, game):
		pg.sprite.Sprite.__init__(self)
		self.game = game
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
	def __init__(self, game):
		super(RightAnswer, self).__init__(game)
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
		


