'''
WHAT IS IT APP LAUNCHER developed by Mr Steven J walden
    Sept. 2020
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''
'''
place mob image before re loading the mobs to increase the changing picture speed
Center portrait pictures

'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import sys
import os
from os.path import expanduser

from Guis_and_sprites import StartUpGui
from methods import dark_theme, light_theme
from Whatisit_app import *


__author__ = 'Mr Steven J Walden'
__version__ = '1.3.0'

class Main_Gui():
	def __init__(self):
		self.gui_app = QtWidgets.QApplication(sys.argv)

		# self.Setup = QtWidgets.QMainWindow()

		self.ui = StartUpGui()
		# self.ui.setupUi(self.Setup)
		# self.icon = QtGui.QIcon()
		self.picture_list = []
		# self.Setup.setWindowIcon(self.icon)

		#connect buttons
		self.ui.DarkModeButton.clicked.connect(self.theme_choice)
		self.ui.StartGameButtonBox.accepted.connect(self.start_okaybutton_clicked)
		self.ui.StartGameButtonBox.rejected.connect(self.start_closebutton_clicked)
		self.ui.EasyModeButton.clicked.connect(self.easy_mode_button_clicked)
		self.ui.HardModeButton.clicked.connect(self.hard_mode_button_clicked)
		self.ui.LoadImagesButton.clicked.connect(self.load_images_button_clicked)
		self.ui.SelectFolderButton.clicked.connect(self.select_folder_button_clicked)

		self.ui.show()
		sys.exit(self.gui_app.exec_())

	def theme_choice(self):
		if self.ui.DarkModeButton.isChecked():
			dark_theme(self.gui_app)
			self.ui.DarkModeButton.setText("Light")
		else:
			light_theme(self.gui_app)
			self.ui.DarkModeButton.setText("Dark")

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
		self.picture_list.clear()
		try:
			#Open folder browser window and choose image files
			self.my_files = QtWidgets.QFileDialog.getOpenFileNames(self.ui, "Select Image Files", expanduser("~"), "Images (*.jpg *.png)")
			for x in range (len(self.my_files[0])):
				if len(self.picture_list) < 10:
					self.picture_list.append(self.my_files[0][x])
		except FileNotFoundError:
			#Stops crash if no folder selected
			pass

	def select_folder_button_clicked(self):
		self.picture_list.clear()
		try:
			#Open folder browser window and choose a folder
			self.my_dir = QtWidgets.QFileDialog.getExistingDirectory(self.ui, "Choose a folder", expanduser("~"), QtWidgets.QFileDialog.ShowDirsOnly)
			# List all files in a directory using listdir()
			for file in os.listdir(self.my_dir):
				if len(self.picture_list) < 10:
					if file.endswith(".png") or file.endswith(".jpg"):
						self.picture_list.append(os.path.join(self.my_dir, file))
				else:
					break
		except FileNotFoundError:
			#Stops crash if no folder selected
			pass

	def start_okaybutton_clicked(self):
		if self.ui.HardModeButton.isChecked():
			print("Hard mode")
		if self.ui.EasyModeButton.isChecked():
			print("Easy mode")
		if len(self.picture_list) > 0:
			#creat an instance of the main game app
			self.game_app = Game(__version__, self.picture_list)

			while self.game_app.running:
				self.game_app.new(self.ui) #pass through the gui instance to hide after pygame set up
				self.ui.show()
				pg.quit()
		else:
			self.message_boxes()


	def start_closebutton_clicked(self):
		self.gui_app.exit()

	def message_boxes(self):
		self.msgbox = QMessageBox()
		self.msgbox.setWindowIcon(QtGui.QIcon("img/Ep_window_icon.ico"))
		self.msgbox.setWindowTitle("No Pictures Selected!")
		self.msgbox.setDefaultButton(QMessageBox.Ok)
		self.msgbox.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)

		self.msgbox.setText('Please choose 1 to 10 pictues.')
		self.msgbox.setIcon(QMessageBox.Warning)
		self.msgbox.setStandardButtons(QMessageBox.Ok)

		self.msgbox.exec()

if __name__ == "__main__":
	print("Author:", __author__)
	print("App version:",__version__)

	Main_Gui()