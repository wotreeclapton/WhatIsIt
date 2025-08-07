'''
WHAT IS IT APPLICATION - Resource Manager 
	Developed by Mr Steven J walden
    Aug. 2025
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''

import pygame as pg
from os import path
import what_is_it.constants as const

class ResourceManager:
	def __init__(self):
		self.images = {}
		self.sprite_images = {}
		self.sounds = {}
        
	def load_image(self, name, filename, scale=None, convert_mode=None):
		# Load an image from the image folder.
		image_path = path.join(const.IMG_FOLDER, filename)
		try:
			image = pg.image.load(image_path)

			# Apply conversion mode
			if convert_mode == "convert":
				image = image.convert()
			elif convert_mode == "convert_alpha":
				image = image.convert_alpha()

			#scale the image if needed
			if scale:
				image = pg.transform.scale(image, scale)

			# Store the loaded image in the dictionary
			self.images[name] = image
		except pg.error as e:
			print(f"Error loading image {filename}: {e}")
			self.images[name] = None  # Assign None to indicate loading failure

	def get_image(self, name):
		# Retrieves a loaded image.
		if name in self.images:
			return self.images[name]
		else:
			print(f"Image not found: {name}")
			return None
        
	def load_spritesheet_image(self, name, x, y, width, height, scale=None):
		# Retrieves an image from the spritesheet
		image = pg.Surface((width, height), pg.SRCALPHA)
		image.blit(self.images.get(name), (0, 0), (x, y, width, height))
		# Scale the image if needed
		if scale:
			image = pg.transform.scale(image, scale)

		return image
	
	def get_sprite_image(self, name):
		# returns a sprite image.
		return self.sprite_images.get(name)

	def load_sound(self, name, filename):
		# Load a sound from the specified folder.
		sound_path = path.join(const.SOUND_FOLDER, filename)
		try:
			self.sounds[name] = pg.mixer.Sound(sound_path)
		except pg.error as e:
			print(f"Error loading sound {filename}: {e}")

	def get_sound(self, name):
		# Retrieves a loaded sound.
		sound = self.sounds.get(name)
		if sound is None:
			raise ValueError(
				f"Sound '{name}' not found. Make sure it is loaded correctly.")
		return sound

	# def play_sound(self, name):
	# 	sound = self.get_sound(name)
	# 	if sound:
	# 		sound.play()

	def load_all_resources(self):
		# Load all images and sounds
		self.load_images()
		# self.load_sounds()

	def load_images(self):
		#Load all images
		images_with_alpha = [
			("wrong1", "Wrong1.png"),
			("wrong2", "Wrong2.png"),
			("wrong3", "Wrong3.png"),
			("wrong4", "Wrong4.png"),
			("wrong5", "Wrong5.png"),
			("wrong6", "Wrong6.png"),
			("wrong7", "Wrong7.png"),
			("wrong8", "Wrong8.png"),
			("wrong9", "Wrong9.png"),
			("wrong10", "Wrong10.png"),
			("wrong11", "Wrong11.png"),
			("wrong12", "Wrong12.png"),
			("wrong13", "Wrong13.png"),
			("easy_spritesheet", "Easy_mode_image.png"),
			("medium_spritesheet", "Med_mode_image.png"),
			("hard_spritesheet", "Hard_mode_image.png")
		]

		images_from_spritesheet = [
			("easy1", (0, 0), (77, 77), "easy_spritesheet"),
			("easy2", (77, 0), (77, 77), "easy_spritesheet"),
			("easy3", (154, 0), (77, 77), "easy_spritesheet"),
			("easy4", (231, 0), (77, 77), "easy_spritesheet"),
			("easy5", (308, 0), (77, 77), "easy_spritesheet"),
			("easy6", (385, 0), (77, 77), "easy_spritesheet"),
			("easy7", (462, 0), (77, 77), "easy_spritesheet"),
			("easy8", (539, 0), (77, 77), "easy_spritesheet"),
			("easy9", (616, 0), (77, 77), "easy_spritesheet"),
			("easy10", (693, 0), (77, 77), "easy_spritesheet"),
			("easy11", (770, 0), (77, 77), "easy_spritesheet"),
			("easy12", (847, 0), (77, 77), "easy_spritesheet"),
			("easy13", (924, 0), (77, 77), "easy_spritesheet"),
			("easy14", (0, 77), (77, 77), "easy_spritesheet"),
			("easy15", (77, 77), (77, 77), "easy_spritesheet"),
			("easy16", (154, 77), (77, 77), "easy_spritesheet"),
			("easy17", (231, 77), (77, 77), "easy_spritesheet"),
			("easy18", (308, 77), (77, 77), "easy_spritesheet"),
			("easy19", (385, 77), (77, 77), "easy_spritesheet"),
			("easy20", (462, 77), (77, 77), "easy_spritesheet"),
			("easy21", (539, 77), (77, 77), "easy_spritesheet"),
			("easy22", (616, 77), (77, 77), "easy_spritesheet"),
			("easy23", (693, 77), (77, 77), "easy_spritesheet"),
			("easy24", (770, 77), (77, 77), "easy_spritesheet"),
			("easy25", (847, 77), (77, 77), "easy_spritesheet"),
			("easy26", (924, 77), (77, 77), "easy_spritesheet"),
			("easy27", (0, 154), (77, 77), "easy_spritesheet"),
			("easy28", (77, 154), (77, 77), "easy_spritesheet"),
			("easy29", (154, 154), (77, 77), "easy_spritesheet"),
			("easy30", (231, 154), (77, 77), "easy_spritesheet"),
			("easy31", (308, 154), (77, 77), "easy_spritesheet"),
			("easy32", (385, 154), (77, 77), "easy_spritesheet"),
			("easy33", (462, 154), (77, 77), "easy_spritesheet"),
			("easy34", (539, 154), (77, 77), "easy_spritesheet"),
			("easy35", (616, 154), (77, 77), "easy_spritesheet"),
			("easy36", (693, 154), (77, 77), "easy_spritesheet"),
			("easy37", (770, 154), (77, 77), "easy_spritesheet"),
			("easy38", (847, 154), (77, 77), "easy_spritesheet"),
			("easy39", (924, 154), (77, 77), "easy_spritesheet"),
			("easy40", (0, 231), (77, 77), "easy_spritesheet"),
			("easy41", (77, 231), (77, 77), "easy_spritesheet"),
			("easy42", (154, 231), (77, 77), "easy_spritesheet"),
			("easy43", (231, 231), (77, 77), "easy_spritesheet"),
			("easy44", (308, 231), (77, 77), "easy_spritesheet"),
			("easy45", (385, 231), (77, 77), "easy_spritesheet"),
			("easy46", (462, 231), (77, 77), "easy_spritesheet"),
			("easy47", (539, 231), (77, 77), "easy_spritesheet"),
			("easy48", (616, 231), (77, 77), "easy_spritesheet"),
			("easy49", (693, 231), (77, 77), "easy_spritesheet"),
			("easy50", (770, 231), (77, 77), "easy_spritesheet"),
			("easy51", (847, 231), (77, 77), "easy_spritesheet"),
			("easy52", (924, 231), (77, 77), "easy_spritesheet"),
			
		]

		# Load images that need convert_alpha()
		for name, filename, *scale in images_with_alpha:
			scale = scale[0] if scale else None
			self.load_image(name, filename, scale, convert_mode="convert_alpha")

		# Load images from a spritesheet
		for name, coords, size, sheet, *scale in images_from_spritesheet:
			x, y = coords[0], coords[1]
			width, height = size[0], size[1]
			scale = scale[0] if scale else None
			image = self.load_spritesheet_image(sheet, x, y, width, height, scale)
			self.sprite_images[name] = image


