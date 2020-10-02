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

class Number_mobs(pg.sprite.Sprite):
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
		# self.number_mobs = []
		# for y in range (14):
		# 	for x in range(20):
		# 		self.number_mobs.append(self.game.sprite_sheet.get_image(x * 50, y * 50, 50, 50))
		self.number_mobs = [self.game.sprite_sheet.get_image(0, 0, 50, 50), self.game.sprite_sheet.get_image(50, 0, 50, 50), self.game.sprite_sheet.get_image(100, 0, 50, 50), self.game.sprite_sheet.get_image(150, 0, 50, 50), self.game.sprite_sheet.get_image(200, 0, 50, 50), self.game.sprite_sheet.get_image(250, 0, 50, 50),self.game.sprite_sheet.get_image(300, 0, 50, 50), self.game.sprite_sheet.get_image(350, 0, 50, 50), self.game.sprite_sheet.get_image(400, 0, 50, 50), self.game.sprite_sheet.get_image(450, 0, 50, 50), self.game.sprite_sheet.get_image(500, 0, 50, 50), self.game.sprite_sheet.get_image(550, 0, 50, 50),self.game.sprite_sheet.get_image(600, 0, 50, 50), self.game.sprite_sheet.get_image(650, 0, 50, 50), self.game.sprite_sheet.get_image(700, 0, 50, 50), self.game.sprite_sheet.get_image(750, 0, 50, 50), self.game.sprite_sheet.get_image(800, 0, 50, 50), self.game.sprite_sheet.get_image(850, 0, 50, 50), self.game.sprite_sheet.get_image(900, 0, 50, 50), self.game.sprite_sheet.get_image(950, 0, 50, 50), 

		self.game.sprite_sheet.get_image(0, 50, 50, 50), self.game.sprite_sheet.get_image(50, 50, 50, 50), self.game.sprite_sheet.get_image(100, 50, 50, 50), self.game.sprite_sheet.get_image(150, 50, 50, 50), self.game.sprite_sheet.get_image(200, 50, 50, 50), self.game.sprite_sheet.get_image(250, 50, 50, 50),self.game.sprite_sheet.get_image(300, 50, 50, 50), self.game.sprite_sheet.get_image(350, 50, 50, 50), self.game.sprite_sheet.get_image(400, 50, 50, 50), self.game.sprite_sheet.get_image(450, 50, 50, 50), self.game.sprite_sheet.get_image(500, 50, 50, 50), self.game.sprite_sheet.get_image(550, 50, 50, 50),self.game.sprite_sheet.get_image(600, 50, 50, 50), self.game.sprite_sheet.get_image(650, 50, 50, 50), self.game.sprite_sheet.get_image(700, 50, 50, 50), self.game.sprite_sheet.get_image(750, 50, 50, 50), self.game.sprite_sheet.get_image(800, 50, 50, 50), self.game.sprite_sheet.get_image(850, 50, 50, 50), self.game.sprite_sheet.get_image(900, 50, 50, 50), self.game.sprite_sheet.get_image(950, 50, 50, 50), 

		self.game.sprite_sheet.get_image(0, 100, 50, 50), self.game.sprite_sheet.get_image(50, 100, 50, 50), self.game.sprite_sheet.get_image(100, 100, 50, 50), self.game.sprite_sheet.get_image(150, 100, 50, 50), self.game.sprite_sheet.get_image(200, 100, 50, 50), self.game.sprite_sheet.get_image(250, 100, 50, 50),self.game.sprite_sheet.get_image(300, 100, 50, 50), self.game.sprite_sheet.get_image(350, 100, 50, 50), self.game.sprite_sheet.get_image(400, 100, 50, 50), self.game.sprite_sheet.get_image(450, 100, 50, 50), self.game.sprite_sheet.get_image(500, 100, 50, 50), self.game.sprite_sheet.get_image(550, 100, 50, 50),self.game.sprite_sheet.get_image(600, 100, 50, 50), self.game.sprite_sheet.get_image(650, 100, 50, 50), self.game.sprite_sheet.get_image(700, 100, 50, 50), self.game.sprite_sheet.get_image(750, 100, 50, 50), self.game.sprite_sheet.get_image(800, 100, 50, 50), self.game.sprite_sheet.get_image(850, 100, 50, 50), self.game.sprite_sheet.get_image(900, 100, 50, 50), self.game.sprite_sheet.get_image(950, 100, 50, 50),

		self.game.sprite_sheet.get_image(0, 150, 50, 50), self.game.sprite_sheet.get_image(50, 150, 50, 50), self.game.sprite_sheet.get_image(100, 150, 50, 50), self.game.sprite_sheet.get_image(150, 150, 50, 50), self.game.sprite_sheet.get_image(200, 150, 50, 50), self.game.sprite_sheet.get_image(250, 150, 50, 50),self.game.sprite_sheet.get_image(300, 150, 50, 50), self.game.sprite_sheet.get_image(350, 150, 50, 50), self.game.sprite_sheet.get_image(400, 150, 50, 50), self.game.sprite_sheet.get_image(450, 150, 50, 50), self.game.sprite_sheet.get_image(500, 150, 50, 50), self.game.sprite_sheet.get_image(550, 150, 50, 50),self.game.sprite_sheet.get_image(600, 150, 50, 50), self.game.sprite_sheet.get_image(650, 150, 50, 50), self.game.sprite_sheet.get_image(700, 150, 50, 50), self.game.sprite_sheet.get_image(750, 150, 50, 50), self.game.sprite_sheet.get_image(800, 150, 50, 50), self.game.sprite_sheet.get_image(850, 150, 50, 50), self.game.sprite_sheet.get_image(900, 150, 50, 50), self.game.sprite_sheet.get_image(950, 150, 50, 50),

		self.game.sprite_sheet.get_image(0, 200, 50, 50), self.game.sprite_sheet.get_image(50,200, 50, 50), self.game.sprite_sheet.get_image(100, 200, 50, 50), self.game.sprite_sheet.get_image(150, 200, 50, 50), self.game.sprite_sheet.get_image(200, 200, 50, 50), self.game.sprite_sheet.get_image(250, 200, 50, 50),self.game.sprite_sheet.get_image(300, 200, 50, 50), self.game.sprite_sheet.get_image(350, 200, 50, 50), self.game.sprite_sheet.get_image(400, 200, 50, 50), self.game.sprite_sheet.get_image(450, 200, 50, 50), self.game.sprite_sheet.get_image(500, 200, 50, 50), self.game.sprite_sheet.get_image(550, 200, 50, 50),self.game.sprite_sheet.get_image(600, 200, 50, 50), self.game.sprite_sheet.get_image(650, 200, 50, 50), self.game.sprite_sheet.get_image(700, 200, 50, 50), self.game.sprite_sheet.get_image(750, 200, 50, 50), self.game.sprite_sheet.get_image(800, 200, 50, 50), self.game.sprite_sheet.get_image(850, 200, 50, 50), self.game.sprite_sheet.get_image(900, 200, 50, 50), self.game.sprite_sheet.get_image(950, 200, 50, 50),

		self.game.sprite_sheet.get_image(0, 250, 50, 50), self.game.sprite_sheet.get_image(50,250, 50, 50), self.game.sprite_sheet.get_image(100, 250, 50, 50), self.game.sprite_sheet.get_image(150, 250, 50, 50), self.game.sprite_sheet.get_image(200, 250, 50, 50), self.game.sprite_sheet.get_image(250, 250, 50, 50),self.game.sprite_sheet.get_image(300, 250, 50, 50), self.game.sprite_sheet.get_image(350, 250, 50, 50), self.game.sprite_sheet.get_image(400, 250, 50, 50), self.game.sprite_sheet.get_image(450, 250, 50, 50), self.game.sprite_sheet.get_image(500, 250, 50, 50), self.game.sprite_sheet.get_image(550, 250, 50, 50),self.game.sprite_sheet.get_image(600, 250, 50, 50), self.game.sprite_sheet.get_image(650, 250, 50, 50), self.game.sprite_sheet.get_image(700, 250, 50, 50), self.game.sprite_sheet.get_image(750, 250, 50, 50), self.game.sprite_sheet.get_image(800, 250, 50, 50), self.game.sprite_sheet.get_image(850, 250, 50, 50), self.game.sprite_sheet.get_image(900, 250, 50, 50), self.game.sprite_sheet.get_image(950, 250, 50, 50),

		self.game.sprite_sheet.get_image(0, 300, 50, 50), self.game.sprite_sheet.get_image(50,300, 50, 50), self.game.sprite_sheet.get_image(100, 300, 50, 50), self.game.sprite_sheet.get_image(150, 300, 50, 50), self.game.sprite_sheet.get_image(200, 300, 50, 50), self.game.sprite_sheet.get_image(250, 300, 50, 50),self.game.sprite_sheet.get_image(300, 300, 50, 50), self.game.sprite_sheet.get_image(350, 300, 50, 50), self.game.sprite_sheet.get_image(400, 300, 50, 50), self.game.sprite_sheet.get_image(450, 300, 50, 50), self.game.sprite_sheet.get_image(500, 300, 50, 50), self.game.sprite_sheet.get_image(550, 300, 50, 50),self.game.sprite_sheet.get_image(600, 300, 50, 50), self.game.sprite_sheet.get_image(650, 300, 50, 50), self.game.sprite_sheet.get_image(700, 300, 50, 50), self.game.sprite_sheet.get_image(750, 300, 50, 50), self.game.sprite_sheet.get_image(800, 300, 50, 50), self.game.sprite_sheet.get_image(850, 300, 50, 50), self.game.sprite_sheet.get_image(900, 300, 50, 50), self.game.sprite_sheet.get_image(950, 300, 50, 50),

		self.game.sprite_sheet.get_image(0, 350, 50, 50), self.game.sprite_sheet.get_image(50,350, 50, 50), self.game.sprite_sheet.get_image(100, 350, 50, 50), self.game.sprite_sheet.get_image(150, 350, 50, 50), self.game.sprite_sheet.get_image(200, 350, 50, 50), self.game.sprite_sheet.get_image(250, 350, 50, 50),self.game.sprite_sheet.get_image(300, 350, 50, 50), self.game.sprite_sheet.get_image(350, 350, 50, 50), self.game.sprite_sheet.get_image(400, 350, 50, 50), self.game.sprite_sheet.get_image(450, 350, 50, 50), self.game.sprite_sheet.get_image(500, 350, 50, 50), self.game.sprite_sheet.get_image(550, 350, 50, 50),self.game.sprite_sheet.get_image(600, 350, 50, 50), self.game.sprite_sheet.get_image(650, 350, 50, 50), self.game.sprite_sheet.get_image(700, 350, 50, 50), self.game.sprite_sheet.get_image(750, 350, 50, 50), self.game.sprite_sheet.get_image(800, 350, 50, 50), self.game.sprite_sheet.get_image(850, 350, 50, 50), self.game.sprite_sheet.get_image(900, 350, 50, 50), self.game.sprite_sheet.get_image(950, 350, 50, 50)]