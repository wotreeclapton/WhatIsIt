'''
WHAT IS IT APPLICATION - Main Game 
	Developed by Mr Steven J walden
    Aug. 2025
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''

import pygame as pg
import random
import logging
import what_is_it.constants as const
from os import path ,environ
from what_is_it.sprites import NumberMobs, Spritesheet, WrongAnswer, RightAnswer
from what_is_it.resource_manager import ResourceManager
from what_is_it.methods import create_picmobs


class Game(object):
	"""docstring for Game"""
	def __init__(self, picture_list, game_mode):
		#setup logger
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.DEBUG)
		self.formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
		self.file_handler = logging.FileHandler('Error_Log')
		# self.file_handler.setLevel(logging.ERROR)
		self.file_handler.setFormatter(self.formatter)
		self.logger.addHandler(self.file_handler)

		# Initialize the clock and resources
		self.clock = pg.time.Clock()
		self.resource_manager = ResourceManager()

		#Define game variables
		self.picture_list = picture_list
		self.game_mode = game_mode
		self.running = True
		self.bg_pic_number = 0
		self.iplist = []
		self.chosen_numb = ""
		self._initialize_game()

		# #Set variables for creating numbermobs and setting highest number
		# if self.game_mode == "Easy":
		# 	self.size_pos = 77
		# 	self.across = 13
		# 	self.down = 9
		# 	self.max_num = 117
		# if self.game_mode == "Medium":
		# 	self.size_pos = 59
		# 	self.across = 17
		# 	self.down = 12
		# 	self.max_num = 204
		# if self.game_mode == "Hard":
		# 	self.size_pos = 50
		# 	self.across = 20
		# 	self.down = 14
		# 	self.max_num = 280

		# self.read_piclist()
		self.load_data()
		self.create_random_number_list()
		self.background_pic(bg_pic_number = self.rand_num_list[self.bg_pic_number])

	def _initialize_game(self):
		#set game screen placement
		environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (const.COMX,const.COMY)
		pg.mixer.pre_init(44100, -16, 1, 512)
		pg.init()
		self.win = pg.display.set_mode((const.SCREENWIDTH,const.SCREENHEIGHT))
		self.win_rect = self.win.get_rect()
		self.load_resources()

	def load_resources(self):
		try:
			self.logo = pg.image.load(path.join(const.IMG_FOLDER, 'eplogo_small.png'))
		except pg.error as e:
			print(f"Failed to load logo: {e}")
		pg.display.set_icon(self.logo)
		pg.display.set_caption(f"{const.GAMENAME} Version {const.__version__}")
		self.resource_manager.load_all_resources()

	def load_data(self):
		#Load all image graphics
		# self.sprite_sheet = Spritesheet(path.join(const.IMG_FOLDER, f"{self.game_mode}_mode_image.png"))
		#Load all games sounds
		self.wrong_sound = pg.mixer.Sound(path.join(const.SOUND_FOLDER, "Wrong.wav"))
		self.right_sound = pg.mixer.Sound(path.join(const.SOUND_FOLDER, "Right.wav"))

	def create_random_number_list(self):
		self.rand_num_list = [i for i in range(len(self.picture_list))]
		random.shuffle(self.rand_num_list)

	def background_pic(self, bg_pic_number):
		#insert try and except here
		try:
			self.bgpic = pg.image.load(self.picture_list[bg_pic_number]).convert()
		except Exception as e:
			self.logger.error(f"{str(e)} at line 87 image load")
			self.bg_pic_number += 1
			if self.bg_pic_number >= len(self.picture_list):
				self.bg_pic_number = 0
			self.bgpic = pg.image.load(self.picture_list[bg_pic_number]).convert()

		self.bgpic_rect = self.bgpic.get_rect()
		self.bgpic_scaled = pg.transform.scale(self.bgpic, (self.bgpic_rect.fit(self.win_rect)[2], self.bgpic_rect.fit(self.win_rect)[3]))
		self.bgpic_scaled_rect = self.bgpic_scaled.get_rect()
		self.bgpic_scaled_rect.centery = int(const.SCREENHEIGHT / 2)
		self.bgpic_scaled_rect.centerx = int(const.SCREENWIDTH / 2)
		print(f"{bg_pic_number + 1} {self.picture_list[bg_pic_number][:-4]}")

	# def create_picmobs(self):
	# 	self.picmob_list = []

	# 	for i in range(self.down): #Normally 12/ 14
	# 		for x in range(self.across):
	# 			self.picmob = NumberMobs(spritesheet = self.sprite_sheet, xpos = self.size_pos* x, ypos = self.size_pos* i, width= self.size_pos, height= self.size_pos)
	# 			self.picmob_group.add(self.picmob)
	# 			self.picmob_list.append(self.picmob)

	def choose_number(self):
		for item in self.iplist:
			self.chosen_numb += item
		try:
			if int(self.chosen_numb) >= 1 and int(self.chosen_numb) <= self.max_num:
				#remove the sprite
				self.picmob_list[int(self.chosen_numb) - 1].kill()
		except ValueError:
			pass
		self.chosen_numb = ""
		self.iplist.clear()

	def new(self, gui):
		#Start a new game
		self.answer_sprites = pg.sprite.Group()
		self.picmob_group = pg.sprite.Group()
		self.picmob_list, self.max_num = create_picmobs(self, self.game_mode)
		gui.hide()

		self.run()

	def run(self):
		#Game loop
		while self.running:
			self.clock.tick(const.FPS)
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
				self.handle_quit()
			elif event.type == pg.KEYDOWN:
				self.iplist.append(event.unicode)
				if event.key == pg.K_ESCAPE or event.key == pg.K_q:
					self.handle_quit()
				if event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
					self.choose_number()
					
				if len(self.picmob_group) < 280: #Stops reveal if no numbers have been chosen
					if event.key == pg.K_SPACE:
						self.bg_pic_number +=1
						if self.bg_pic_number >= len(self.picture_list):
							self.bg_pic_number = 0
						self.picmob_group.empty()
						self.background_pic(bg_pic_number = self.rand_num_list[self.bg_pic_number])
						self.create_picmobs()
						self.iplist.clear()
					if event.key == pg.K_y:
						#Correct answer function
						self.right_pic = RightAnswer(self ,game_mode= self.game_mode)
						self.answer_sprites.add(self.right_pic)
						self.right_sound.play()
						self.picmob_group.empty()
						self.iplist.clear()
					if event.key == pg.K_n:
						#Incorrect answer
						self.wrong_pic = WrongAnswer(self)
						self.answer_sprites.add(self.wrong_pic)
						self.wrong_sound.play()
						self.iplist.clear()

	def handle_quit(self):
		"""Handles the quit event"""
		if self.running:
			self.running = False

	def draw(self):
		#Game loop - draw
		self.win.fill(const.BLACK)
		try:
			self.win.blit(self.bgpic_scaled, (self.bgpic_scaled_rect.x, self.bgpic_scaled_rect.y))
		except Exception as e:
			self.logger.error(str(e))
			self.bg_pic_number += 1
			if self.bg_pic_number >= len(self.picture_list):
				self.bg_pic_number = 0
			self.background_pic(bg_pic_number=self.rand_num_list[self.bg_pic_number])
			self.win.blit(self.bgpic_scaled, (self.bgpic_scaled_rect.x, self.bgpic_scaled_rect.y))

		self.picmob_group.draw(self.win)
		self.answer_sprites.draw(self.win)
		pg.display.update()

# g = Game()

# if __name__ == '__main__':
# 	# print(time.strftime("%M Minuets %S Seconds"))
# 	g.new()



# pg.quit()



