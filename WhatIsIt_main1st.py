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

__author__ = 'Mr Steven J Walden'
__version__ = '1.2.0'

class Main_Gui():
	def __init__(self):

		# self.Setup = QtWidgets.QMainWindow()

		self.ui = StartUpGui()
		# self.ui.setupUi(self.Setup)
		# self.icon = QtGui.QIcon()
		self.load_data()
		#dark_theme(app=app)
		# self.Setup.setWindowIcon(self.icon)

		#connect buttons
		self.ui.DarkModeButton.clicked.connect(self.theme_choice)
		self.ui.StartGameButtonBox.accepted.connect(self.start_okaybutton_clicked)
		self.ui.StartGameButtonBox.rejected.connect(self.start_closebutton_clicked)
		self.ui.EasyModeButton.clicked.connect(self.easy_mode_button_clicked)
		self.ui.HardModeButton.clicked.connect(self.hard_mode_button_clicked)
		self.ui.LoadImagesButton.clicked.connect(self.load_images_button_clicked)

		self.ui.show()
		sys.exit(app.exec_())

	def theme_choice(self):
		if self.ui.DarkModeButton.isChecked():
			dark_theme(app)
			self.ui.DarkModeButton.setText("Light")
		else:
			light_theme(app)
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

	def start_closebutton_clicked(self):
		app.exit()

	# def dark_theme(self):
	# 	self.app.setStyle("Fusion")

	# 	self.dark_palette = QPalette()

	# 	self.dark_palette.setColor(QPalette.Window,QColor(53,53,53))
	# 	self.dark_palette.setColor(QPalette.WindowText, Qt.white)
	# 	self.dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
	# 	self.dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
	# 	self.dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
	# 	self.dark_palette.setColor(QPalette.ToolTipText, Qt.white)
	# 	self.dark_palette.setColor(QPalette.Text, Qt.white)
	# 	self.dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
	# 	self.dark_palette.setColor(QPalette.ButtonText, Qt.white)
	# 	self.dark_palette.setColor(QPalette.BrightText, Qt.red)
	# 	self.dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
	# 	self.dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
	# 	self.dark_palette.setColor(QPalette.HighlightedText, Qt.black)

	# 	self.app.setPalette(self.dark_palette)

	# 	self.app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

	def start_button_clicked(self):
		#creat an instance of the main game app
		# app = App(self.countdown_time, self.sound_option, self.min_hand, self.scroll, self.hour_num, self.sec_num, self.music_choice)

		# while app.running:
		# 	app.new(self.Setup) #pass through the gui instance to close after pygame set up
		# 	self.Setup.show()
		# 	pg.quit()
		# self.Setup.hide()
		pass


if __name__ == "__main__":
	print("Author:", __author__)
	print("App version:",__version__)

	app = QtWidgets.QApplication(sys.argv)
	Main_Gui()