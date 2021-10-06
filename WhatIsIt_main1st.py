'''
WHAT IS IT APP LAUNCHER developed by Mr Steven J walden
    Sept. 2020
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import sys
#from PyQt5.QtWidgets import QApplication, QPushButton

from Guis_and_sprites import StartUpGui
from methods import dark_theme, light_theme
from Whatisit_app import *


__author__ = 'Mr Steven J Walden'
__version__ = '1.3.0'

class Main_Gui():
	def __init__(self):
		self.app = QtWidgets.QApplication(sys.argv)

		# self.Setup = QtWidgets.QMainWindow()

		self.ui = StartUpGui()
		# self.ui.setupUi(self.Setup)
		# self.icon = QtGui.QIcon()
		self.load_data()
		# self.Setup.setWindowIcon(self.icon)

		#connect buttons
		self.ui.DarkModeButton.clicked.connect(self.theme_choice)
		self.ui.StartGameButtonBox.accepted.connect(self.start_okaybutton_clicked)
		self.ui.StartGameButtonBox.rejected.connect(self.start_closebutton_clicked)
		self.ui.EasyModeButton.clicked.connect(self.easy_mode_button_clicked)
		self.ui.HardModeButton.clicked.connect(self.hard_mode_button_clicked)
		self.ui.LoadImagesButton.clicked.connect(self.load_images_button_clicked)

		self.ui.show()
		sys.exit(self.app.exec_())

	def theme_choice(self):
		if self.ui.DarkModeButton.isChecked():
			dark_theme(self.app)
			self.ui.DarkModeButton.setText("Light")
		else:
			light_theme(self.app)
			self.ui.DarkModeButton.setText("Dark")

	def load_data(self):
		#Load all image graphics
		pass

	def easy_mode_button_clicked(self):
		if self.ui.EasyModeButton.isChecked():
			self.ui.HardModeButton.setChecked(False)
		else:
			self.ui.EasyModeButton.setChecked(True)

	def hard_mode_button_clicked(self):
		if self.ui.HardModeButton.isChecked():
			self.ui.EasyModeButton.setChecked(False)
		else:
			self.ui.HardModeButton.setChecked(True)

	def load_images_button_clicked(self):
		print("load")

	def start_okaybutton_clicked(self):
		if self.ui.HardModeButton.isChecked():
			print("Hard mode")
		if self.ui.EasyModeButton.isChecked():
			print("Easy mode")
		#creat an instance of the main game app
		self.app = Game()

		while self.app.running:
			self.app.new(self.ui) #pass through the gui instance to hide after pygame set up
			self.ui.show()
			pg.quit()
		

	def start_closebutton_clicked(self):
		self.app.exit()


if __name__ == "__main__":
	print("Author:", __author__)
	print("App version:",__version__)

	Main_Gui()