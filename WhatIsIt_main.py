#! python 3
'''
WHAT IS IT APP LAUNCHER developed by Mr Steven J walden
    Sept. 2020
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''
'''
make a number pic sprite class


'''
from os import path ,environ
import pygame as pg
import random
from methods import *
from sprites import Number_mobs, Spritesheet


__author__ = 'Mr Steven J Walden'
__version__ = '1.0.0'

class Game(object):
	"""docstring for Game"""
	def __init__(self):
		#Initialize game window, etc		
		#set game screen placement
		environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (COMX,COMY)
		pg.mixer.pre_init(44100, -16, 1, 512)
		pg.init()

		#Set logo and gamescreen etc	
		self.win = pg.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
		self.win_rect = self.win.get_rect()
		self.logo = pg.image.load(path.join(IMG_FOLDER, 'eplogo_small.png'))
		pg.display.set_icon(self.logo)
		pg.display.set_caption(f"{GAMENAME} Version {__version__}")
		self.clock = pg.time.Clock()

		self.load_data()
		self.background_pic(bg_pic_number = 0)

		#Define game variables
		self.running = True
		self.bg_pic_number = 1

	def load_data(self):
		#Load all image graphics
		self.bgpic_list = [pg.image.load(path.join(IMG_FOLDER, f"Picture{x + 1}.png")) for x in range (15)]
		self.sprite_sheet = Spritesheet(path.join(IMG_FOLDER, "What_is_it_game_images.png"))
 		#Load all games sounds

	def background_pic(self, bg_pic_number):
		self.bgpic = self.bgpic_list[bg_pic_number]
		self.bgpic_rect = self.bgpic.get_rect()
		self.bgpic_scaled = pg.transform.scale(self.bgpic, (self.bgpic_rect.fit(self.win_rect)[2], self.bgpic_rect.fit(self.win_rect)[3]))
		self.bgpic_scaled_rect = self.bgpic_scaled.get_rect()
		self.bgpic_scaled_rect.centery = int(SCREENHEIGHT / 2)

	def create_picmobs(self):
		self.picmob_list = []
		for i in range(8):
			for x in range(20):
				self.picmob = Number_mobs(game = g, xpos = 50* x, ypos = 50* i, img = x + (i * 20))
				self.all_sprites.add(self.picmob)
				self.picmob_list.append(self.picmob)

	def new(self):
		#Start a new game
		self.show_start_screen()
		self.all_sprites = pg.sprite.Group()
		self.picmob_group = pg.sprite.Group()
		# self.numpic = Number_mobs(game = g, xpos = 0, ypos = 0, colour = self.c_list[random.randrange(len(self.c_list))])
		self.create_picmobs()
		# self.all_sprites.add(self.numpic)
		self.run()

	def run(self):
		#Game loop
		while self.running:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

	def update(self):
		#Game loop - update
		self.all_sprites.update()

	def events(self):
		#Game loop - events
		for event in pg.event.get():#exit loop
			if event.type == pg.QUIT:
				if self.running:
					self.running = False
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					if self.running:
						self.running = False
				if event.key == pg.K_SPACE:
					self.bg_pic_number +=1
					if self.bg_pic_number >= len(self.bgpic_list):
						self.bg_pic_number = 0
					self.background_pic(bg_pic_number = self.bg_pic_number)

	def draw(self):
		#Game loop - draw
		self.win.fill(BLACK)
		self.win.blit(self.bgpic_scaled, (self.bgpic_scaled_rect.x, self.bgpic_scaled_rect.y))
		self.all_sprites.draw(self.win)
		pg.display.update()

	def show_start_screen(self):
		#Game start screen
		pass

	def show_go_screen(self):
		#Game over/continue screen
		pass


g = Game()

if __name__ == '__main__':
	g.new()



pg.quit()



