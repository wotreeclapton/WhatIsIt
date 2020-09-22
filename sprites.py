#Sprite classes for game 
import pygame as pg
import random
from methods import *

class Spritesheet:
	def __init__(self, filename):
		pass

	def get_image(self, x, y, width, height):
		#Grab an image from the sheet
		pass

class Mobs(pg.sprite.Sprite):
	def __init__(self, game):
		pg.sprite.Sprite.__init__(self)
		self.game = game
		#self.image = pg.Surface((50,50))
		#self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		pass

	def update(self):
		pass

	def load_images(self):
		pass