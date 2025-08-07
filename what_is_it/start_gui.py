'''
WHAT IS IT APP LAUNCHER - Startup Gui
	Developed by Mr Steven J walden
    Aug. 2025
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''

from PyQt5 import QtWidgets, QtGui, QtCore
import what_is_it.constants as const



class StartUpGui(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(StartUpGui, self).__init__(parent)
		self.initUI()

	def initUI(self):
		# Set up GUI
		self.resize(310, 208)
		self.setMinimumSize(310, 208)
		self.setMaximumSize(310, 208)
		self.setWindowIcon(QtGui.QIcon(f"{const.IMG_FOLDER}/Ep_window_icon.ico"))
		self.setWindowTitle(const.GAMENAME)

		self.add_buttons()
		self.tab_order()

	def add_buttons(self):
		bfont = QtGui.QFont()
		bfont.setPointSize(14)
		bfont.setBold(True)
		bfont.setItalic(True)

		self.EasyModeButton = QtWidgets.QPushButton(self)
		self.EasyModeButton.setGeometry(10, 28, 90, 60)
		self.EasyModeButton.setCheckable(True)
		self.EasyModeButton.setChecked(True)
		self.EasyModeButton.setFont(bfont)
		self.EasyModeButton.setText("Easy\nMode")

		self.MediumModeButton = QtWidgets.QPushButton(self)
		self.MediumModeButton.setGeometry(110, 28, 90, 60)
		self.MediumModeButton.setCheckable(True)
		self.MediumModeButton.setFont(bfont)
		self.MediumModeButton.setText("Medium\nMode")

		self.HardModeButton = QtWidgets.QPushButton(self)
		self.HardModeButton.setGeometry(210, 28, 90, 60)
		self.HardModeButton.setCheckable(True)
		self.HardModeButton.setFont(bfont)
		self.HardModeButton.setText("Hard\nMode")

		self.LoadImagesButton = QtWidgets.QPushButton(self)
		self.LoadImagesButton.setGeometry(10, 98, 140, 60)
		self.LoadImagesButton.setFont(bfont)
		self.LoadImagesButton.setText("Load Images")

		self.SelectFolderButton = QtWidgets.QPushButton(self)
		self.SelectFolderButton.setGeometry(160, 98, 140, 60)
		self.SelectFolderButton.setFont(bfont)
		self.SelectFolderButton.setText("Select Folder")

		# Group for difficulty buttons to ensure mutual exclusivity
		self.difficulty_button_group = QtWidgets.QButtonGroup(self)
		self.difficulty_button_group.addButton(self.EasyModeButton)
		self.difficulty_button_group.addButton(self.MediumModeButton)
		self.difficulty_button_group.addButton(self.HardModeButton)

		# Button for switchiong to darkmode
		bfont.setPointSize(8)
		bfont.setBold(False)
		self.DarkModeButton = QtWidgets.QPushButton(self)
		self.DarkModeButton.setGeometry(10, 4, 40, 20)
		self.DarkModeButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.DarkModeButton.setCheckable(True)
		self.DarkModeButton.setFont(bfont)
		self.DarkModeButton.setText("Dark")

		# Button box setup for OKay and cancel buttons
		self.StartGameButtonBox = QtWidgets.QDialogButtonBox(self)
		self.StartGameButtonBox.setGeometry(142, 174, 156, 23)
		self.StartGameButtonBox.setStandardButtons(
			QtWidgets.QDialogButtonBox.Close | QtWidgets.QDialogButtonBox.Ok)

	def tab_order(self):
		self.setTabOrder(self.EasyModeButton, self.MediumModeButton)
		self.setTabOrder(self.HardModeButton, self.LoadImagesButton)
		self.setTabOrder(self.SelectFolderButton, self.StartGameButtonBox)
