#! python 3
'''
WHAT IS IT APP LAUNCHER developed by Mr Steven J walden
    Sept. 2020
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''
'''
stop spcae bar moving picture more than once
Easy and hard mode
randomize pictures

'''
from os import path ,environ
import pygame as pg
import random
from methods import *
from sprites import NumberMobs, Spritesheet, WrongAnswer, RightAnswer
import time


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
		
		#Define game variables
		self.running = True
		self.bg_pic_number = 0
		self.iplist = []
		self.chosen_numb = ""

		self.read_piclist()
		self.load_data()
		self.create_random_number_list()
		self.background_pic(bg_pic_number = self.rand_num_list[self.bg_pic_number])


	def load_data(self):
		#Load all image graphics
		self.bgpic_list = [pg.image.load(path.join(PIC_FOLDER, f"{self.picture_list[x]}.png")) for x in range (len(self.picture_list))]
		# self.bgpic_list = [pg.image.load(path.join(PIC_FOLDER, f"Picture{x + 1}.png")) for x in range (len(self.picture_list))]
		self.sprite_sheet = Spritesheet(path.join(IMG_FOLDER, "What_is_it_game_images.png"))
		#Load all games sounds
		self.wrong_sound = pg.mixer.Sound(path.join(SOUND_FOLDER, "Wrong.wav"))
		self.right_sound = pg.mixer.Sound(path.join(SOUND_FOLDER, "Right.wav"))

	def create_random_number_list(self):
		self.rand_num_list = [i for i in range(len(self.bgpic_list))]
		random.shuffle(self.rand_num_list)

	def background_pic(self, bg_pic_number):
		self.bgpic = self.bgpic_list[bg_pic_number]
		self.bgpic_rect = self.bgpic.get_rect()
		self.bgpic_scaled = pg.transform.scale(self.bgpic, (self.bgpic_rect.fit(self.win_rect)[2], self.bgpic_rect.fit(self.win_rect)[3]))
		self.bgpic_scaled_rect = self.bgpic_scaled.get_rect()
		self.bgpic_scaled_rect.centery = int(SCREENHEIGHT / 2)
		print(f"{bg_pic_number + 1} {self.picture_list[bg_pic_number]}")

	def create_picmobs(self):
		self.picmob_list = []
		for i in range(14): #Normally 14
			for x in range(20):
				self.picmob = NumberMobs(game = g, xpos = 50* x, ypos = 50* i, img = x + (i * 20))
				self.picmob_group.add(self.picmob)
				self.picmob_list.append(self.picmob)

	def read_piclist(self):
		#Prints out a list of pictures from the list to the console
		self.picture_list = []
		with open("picture_list.txt" ,"r") as file:
			for line in file:
				self.picture_list.append(line[:-1])
				print(line[:-1])

	def choose_number(self):
		for item in self.iplist:
			self.chosen_numb += item
		try:
			if int(self.chosen_numb) >= 1 and int(self.chosen_numb) <= 280:
				#remove the sprite
				self.picmob_list[int(self.chosen_numb) - 1].kill()
		except ValueError:
			pass
		self.chosen_numb = ""
		self.iplist.clear()

	def new(self):
		#Start a new game
		# self.show_start_screen()
		self.answer_sprites = pg.sprite.Group()
		self.picmob_group = pg.sprite.Group()
		self.create_picmobs()
		# print(time.strftime("%M Minuets %S Seconds"))
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
		self.picmob_group.update()
		self.answer_sprites.update()

	def events(self):
		#Game loop - events
		for event in pg.event.get():#exit loop
			if event.type == pg.QUIT:
				if self.running:
					self.running = False
			elif event.type == pg.KEYDOWN:
				self.iplist.append(event.unicode)
				if event.key == pg.K_ESCAPE:
					if self.running:
						self.running = False
				if event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
					self.choose_number()
				# if event.key == pg.K_UP:
				# 	self.bg_pic_number +=1
				# 	if self.bg_pic_number > len(self.bgpic_list) - 1:
				# 		self.bg_pic_number = 0
				# 	self.background_pic(bg_pic_number = self.bg_pic_number)
				# 	self.iplist.clear()
				# if event.key == pg.K_DOWN:
				# 	self.bg_pic_number -=1
				# 	if self.bg_pic_number < 0:
				# 		self.bg_pic_number = len(self.bgpic_list) - 1
				# 	self.background_pic(bg_pic_number = self.bg_pic_number)
				# 	self.iplist.clear()
					
				if len(self.picmob_group) < 280: #Stops reveal if no numbers have been chosen
					if event.key == pg.K_SPACE:
						# self.bg_pic_number = random.randrange(start=1, stop=len(self.bgpic_list))
						self.bg_pic_number +=1
						if self.bg_pic_number >= len(self.bgpic_list):
							self.bg_pic_number = 0
						self.picmob_group.empty()
						self.background_pic(bg_pic_number = self.rand_num_list[self.bg_pic_number])
						self.create_picmobs()
						self.iplist.clear()
					if event.key == pg.K_y:
						#Correct answer function
						self.right_pic = RightAnswer(game = g)
						self.answer_sprites.add(self.right_pic)
						self.right_sound.play()
						self.picmob_group.empty()
						self.iplist.clear()
					if event.key == pg.K_n:
						#Incorrect answer
						self.wrong_pic = WrongAnswer(game = g)
						self.answer_sprites.add(self.wrong_pic)
						self.wrong_sound.play()
						self.iplist.clear()

	def draw(self):
		#Game loop - draw
		self.win.fill(BLACK)
		self.win.blit(self.bgpic_scaled, (self.bgpic_scaled_rect.x, self.bgpic_scaled_rect.y))
		self.picmob_group.draw(self.win)
		self.answer_sprites.draw(self.win)
		pg.display.update()

	def show_start_screen(self):
		#Game start screen
		pass

	def show_go_screen(self):
		#Game over/continue screen
		pass


g = Game()

if __name__ == '__main__':
	# print(time.strftime("%M Minuets %S Seconds"))
	g.new()



pg.quit()



