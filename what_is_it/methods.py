'''
WHAT IS IT APP - Methods 
	Developed by Mr Steven J walden
    Aug. 2025
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''

from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from what_is_it.sprites import NumberMobs


def dark_theme(app):
	app.setStyle("Fusion")

	dark_palette = QPalette()

	dark_palette.setColor(QPalette.Window,QColor(53,53,53))
	dark_palette.setColor(QPalette.WindowText, Qt.white)
	dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
	dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
	dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
	dark_palette.setColor(QPalette.ToolTipText, Qt.white)
	dark_palette.setColor(QPalette.Text, Qt.white)
	dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
	dark_palette.setColor(QPalette.ButtonText, Qt.white)
	dark_palette.setColor(QPalette.BrightText, Qt.red)
	dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
	dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
	dark_palette.setColor(QPalette.HighlightedText, Qt.black)

	app.setPalette(dark_palette)

	app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

def light_theme(app):

	app.setStyle("Fusion")

	light_palette = QPalette()

	light_palette.setColor(QPalette.Window,QColor(225,225,225))
	light_palette.setColor(QPalette.WindowText, QtCore.Qt.black)
	light_palette.setColor(QPalette.Base, QColor(240, 240, 240))
	light_palette.setColor(QPalette.AlternateBase, QColor(225, 225, 225))
	light_palette.setColor(QPalette.ToolTipBase, QtCore.Qt.black)
	light_palette.setColor(QPalette.ToolTipText, QtCore.Qt.black)
	light_palette.setColor(QPalette.Text, QtCore.Qt.black)
	light_palette.setColor(QPalette.Button, QColor(225, 225, 225))
	light_palette.setColor(QPalette.ButtonText, QtCore.Qt.black)
	light_palette.setColor(QPalette.BrightText, QtCore.Qt.red)
	light_palette.setColor(QPalette.Link, QColor(251, 255, 255))
	light_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
	light_palette.setColor(QPalette.HighlightedText, QtCore.Qt.white)

	app.setPalette(light_palette)

	app.setStyleSheet("QToolTip { color: #706b67; background-color: #fffefa; border: 1px solid grey; }")

def create_picmobs(game, game_mode):
	picmob_list = []

	# Set variables for creating numbermobs and setting highest number
	if game_mode == "Easy":
			size_pos = 77
			across = 13
			down = 9
			max_num = 117
	elif game_mode == "Medium":
		size_pos = 59
		across = 17
		down = 12
		max_num = 204
	elif game_mode == "Hard":
		size_pos = 50
		across = 20
		down = 14
		max_num = 280
	else:
		return [], 0

	for i in range(down):  # Normally 12/ 14
		for x in range(across):
			picmob = NumberMobs(spritesheet=game.resource_manager.get_image(f"{game_mode}_spritesheet"), xpos=size_pos * x,
										ypos=size_pos * i, width=size_pos, height=size_pos)
			game.picmob_group.add(picmob)
			picmob_list.append(picmob)
	return picmob_list, max_num

# def choose_number():
# 	for item in self.iplist:
# 		self.chosen_numb += item
# 	try:
# 		if int(self.chosen_numb) >= 1 and int(self.chosen_numb) <= self.max_num:
# 			# remove the sprite
# 			self.picmob_list[int(self.chosen_numb) - 1].kill()
# 	except ValueError:
# 		pass
# 	self.chosen_numb = ""
# 	self.iplist.clear()

