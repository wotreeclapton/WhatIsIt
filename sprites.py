#Sprite classes for game 
import pygame as pg
import random
from methods import *

class Spritesheet:
	def __init__(self, filename):
		self.spritesheet = pg.image.load(filename).convert_alpha()

	def get_image(self, x, y, width, height):
		#Grab an image from the sheet
		image = pg.Surface((width, height), pg.SRCALPHA)
		image.blit(self.spritesheet, (0,0), (x, y, width, height))
		return image

class Number_mobs(pg.sprite.Sprite):
	def __init__(self, game, xpos, ypos, colour):
		pg.sprite.Sprite.__init__(self)
		self.game = game
		# self.image = self.number_images[0]
		self.image = pg.Surface((50,50))
		self.image.fill(colour)
		self.rect = self.image.get_rect()
		self.rect.x = xpos
		self.rect.y = ypos

	def update(self):
		pass

	def load_images(self):
		self.number_images = []