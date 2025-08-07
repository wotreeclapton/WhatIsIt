'''
WHAT IS IT APP LAUNCHER - Main GUI
	Developed by Mr Steven J walden
    Aug. 2025
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import os
from os.path import expanduser
import pygame as pg
from what_is_it.start_gui import StartUpGui
from what_is_it.methods import dark_theme, light_theme
from what_is_it.game_screen import Game
import what_is_it.constants as const


class Main_Gui():
	"""
	Main GUI application class for the 'What Is It' game launcher.
	Handles user interaction for selecting game mode, loading images,
	and starting the Pygame application.
	"""
	def __init__(self):
		"""
		Initializes the Main_Gui application, sets up the UI,
		and connects button signals to their respective slots.
		"""
		self.gui_app = QtWidgets.QApplication(sys.argv)

		self.ui = StartUpGui()
		self.picture_list = []
		self.game_mode = const.GAME_MODE_EASY  # Initialize with default game mode

		#connect buttons
		self.ui.DarkModeButton.clicked.connect(self.theme_choice)
		self.ui.StartGameButtonBox.accepted.connect(self.start_okaybutton_clicked)
		self.ui.StartGameButtonBox.rejected.connect(self.start_closebutton_clicked)
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

	def load_images_button_clicked(self):
		self.picture_list.clear()
		try:
			# Open folder browser window and choose image files
			# getOpenFileNames returns a tuple: (list_of_filenames, selected_filter)
			selected_files_data, _ = QtWidgets.QFileDialog.getOpenFileNames(
				self.ui, "Select Image Files", expanduser("~"), "Images (*.jpg *.png)")
			if selected_files_data:  # Check if the user selected any files
				self.picture_list.extend(selected_files_data)
		except FileNotFoundError:
			#Stops crash if no image selected
			pass

	def select_folder_button_clicked(self):
		self.picture_list.clear()
		try:
			# Open folder browser window and choose a folder
			selected_folder_path = QtWidgets.QFileDialog.getExistingDirectory(
				self.ui, "Choose a folder", expanduser("~"), QtWidgets.QFileDialog.ShowDirsOnly)
			if selected_folder_path:  # Check if a folder was selected
				for file_name in os.listdir(selected_folder_path):
					# Use lower() for case-insensitive check and tuple for multiple extensions
					if file_name.lower().endswith((".png", ".jpg")):
						self.picture_list.append(os.path.join(selected_folder_path, file_name))
		except FileNotFoundError:
			#Stops crash if no folder selected
			pass

	def start_okaybutton_clicked(self):
		if self.ui.HardModeButton.isChecked():
			self.game_mode = const.GAME_MODE_HARD
		elif self.ui.MediumModeButton.isChecked():
			self.game_mode = const.GAME_MODE_MEDIUM
		elif self.ui.EasyModeButton.isChecked():  # EasyModeButton is checked by default
			self.game_mode = const.GAME_MODE_EASY

		if len(self.picture_list) > 0:
			# Create an instance of the main game app.
			current_game_instance = Game(self.picture_list, self.game_mode)

			if current_game_instance.running:
				current_game_instance.new(self.ui)  # This method runs the game.
			# After the game session in new() concludes and returns:
			self.ui.show()  # Ensure the launcher GUI is visible again.
			pg.quit()
		else:
			self.message_boxes()
		
	def start_closebutton_clicked(self):
		self.gui_app.exit()

	def message_boxes(self):
		self.msgbox = QMessageBox(self.ui)  # Set parent to self.ui
		self.msgbox.setWindowIcon(QtGui.QIcon("img/Ep_window_icon.ico"))
		self.msgbox.setWindowTitle("No Pictures Selected!")
		self.msgbox.setDefaultButton(QMessageBox.Ok)
		self.msgbox.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)

		self.msgbox.setText('Please choose at least 1 picture.')
		self.msgbox.setIcon(QMessageBox.Warning)
		self.msgbox.setStandardButtons(QMessageBox.Ok)

		self.msgbox.exec()

if __name__ == "__main__":
	print("Author:", const.__author__)
	print("App version:",const.__version__)

	Main_Gui()