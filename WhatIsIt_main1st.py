#! python 3
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


class Main_Gui():
	def __init__(self):

		self.app = QtWidgets.QApplication(sys.argv)

		self.Setup = QtWidgets.QMainWindow()

		self.ui = Ui_Setup()
		self.ui.setupUi(self.Setup)
		self.icon = QtGui.QIcon()
		self.load_data()
		self.dark_theme()
		self.Setup.setWindowIcon(self.icon)

		self.Setup.show()
		sys.exit(self.app.exec_())

	def load_data(self):
		#Load all image graphics
		pass

	def dark_theme(self):
		self.app.setStyle("Fusion")

		self.dark_palette = QPalette()

		self.dark_palette.setColor(QPalette.Window,QColor(53,53,53))
		self.dark_palette.setColor(QPalette.WindowText, Qt.white)
		self.dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
		self.dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
		self.dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
		self.dark_palette.setColor(QPalette.ToolTipText, Qt.white)
		self.dark_palette.setColor(QPalette.Text, Qt.white)
		self.dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
		self.dark_palette.setColor(QPalette.ButtonText, Qt.white)
		self.dark_palette.setColor(QPalette.BrightText, Qt.red)
		self.dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
		self.dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
		self.dark_palette.setColor(QPalette.HighlightedText, Qt.black)

		self.app.setPalette(self.dark_palette)

		self.app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

	def start_button_clicked(self):
		#creat an instance of the main clock app
		# app = App(self.countdown_time, self.sound_option, self.min_hand, self.scroll, self.hour_num, self.sec_num, self.music_choice)

		# while app.running:
		# 	app.new(self.Setup) #pass through the gui instance to close after pygame set up
		# 	self.Setup.show()
		# 	pg.quit()
		# self.Setup.hide()
		pass


if __name__ == "__main__":
	Main_Gui()
